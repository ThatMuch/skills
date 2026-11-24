#!/usr/bin/env python3
"""Check skill frontmatter and keep the README index in sync.

Usage:
  python3 scripts/validate_skills.py
  python3 scripts/validate_skills.py --write-index

Requires PyYAML. No other third-party packages.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML est requis : pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
README = ROOT / "README.md"
INDEX_START = "<!-- skills-index:start -->"
INDEX_END = "<!-- skills-index:end -->"

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
EXAMPLE_DOMAIN_RE = re.compile(r"@(?:[A-Za-z0-9-]+\.)*example\.(?:com|org|net)$", re.IGNORECASE)
SECRET_RE = re.compile(
    r"(?<![A-Za-z0-9])("
    r"sk-[A-Za-z0-9]{8,}|ghp_[A-Za-z0-9]{20,}|gho_[A-Za-z0-9]{20,}"
    r"|github_pat_[A-Za-z0-9_]{20,}|xox[baprs]-[A-Za-z0-9-]{10,}|AKIA[0-9A-Z]{16}"
    r")"
)
PLACEHOLDER_RE = re.compile(r"<(?:[A-Z][A-Z0-9_]{2,})>")
DESCRIPTION_MAX = 1024
ONELINER_MAX = 140

SCAN_SUFFIXES = {".md", ".json", ".yml", ".yaml", ".txt", ".py"}


def split_frontmatter(text: str, path: Path) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: le fichier ne commence pas par un frontmatter YAML")
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError(f"{path}: frontmatter non fermé")
    data = yaml.safe_load(parts[1])
    if not isinstance(data, dict):
        raise ValueError(f"{path}: le frontmatter doit être un objet YAML")
    return data, parts[2]


def oneliner(description: str) -> str:
    collapsed = " ".join(description.split())
    collapsed = collapsed.replace("|", "\\|")
    if len(collapsed) <= ONELINER_MAX:
        return collapsed
    cut = collapsed[: ONELINER_MAX - 1].rsplit(" ", 1)[0]
    return cut + "…"


def iter_skills() -> list[tuple[str, str, Path, dict, str]]:
    found: list[tuple[str, str, Path, dict, str]] = []
    if not SKILLS_DIR.is_dir():
        raise ValueError("dossier skills/ introuvable")
    for path in sorted(SKILLS_DIR.rglob("SKILL.md")):
        relative = path.relative_to(SKILLS_DIR)
        if len(relative.parts) != 3:
            raise ValueError(
                f"{path}: attendu skills/<categorie>/<slug>/SKILL.md, obtenu {relative}"
            )
        category, slug, _ = relative.parts
        data, body = split_frontmatter(path.read_text(encoding="utf-8"), path)
        found.append((category, slug, path, data, body))
    if not found:
        raise ValueError("aucune skill trouvée")
    return found


def validate_skill(category: str, slug: str, path: Path, data: dict, body: str) -> list[str]:
    errors: list[str] = []
    name = data.get("name")
    description = data.get("description")
    if not isinstance(name, str) or not name.strip():
        errors.append(f"{path}: frontmatter `name` manquant")
    elif not NAME_RE.match(name):
        errors.append(f"{path}: `name` doit être en kebab-case ({name!r})")
    elif name != slug:
        errors.append(f"{path}: `name` ({name}) ≠ dossier ({slug})")
    if not isinstance(description, str) or not description.strip():
        errors.append(f"{path}: frontmatter `description` manquant")
    else:
        collapsed = " ".join(description.split())
        if len(collapsed) > DESCRIPTION_MAX:
            errors.append(
                f"{path}: `description` dépasse {DESCRIPTION_MAX} caractères ({len(collapsed)})"
            )
    if PLACEHOLDER_RE.search(path.read_text(encoding="utf-8")) and "## À personnaliser" not in body:
        errors.append(f"{path}: des placeholders sont présents sans section « À personnaliser »")
    if not NAME_RE.match(category):
        errors.append(f"{path}: catégorie invalide ({category})")
    return errors


def render_index(skills: list[tuple[str, str, Path, dict, str]]) -> str:
    rows = [
        "| Skill | Catégorie | Description |",
        "| --- | --- | --- |",
    ]
    for category, slug, path, data, _body in sorted(skills, key=lambda item: (item[0], item[1])):
        description = data.get("description")
        line = oneliner(description if isinstance(description, str) else "")
        link = path.relative_to(ROOT).as_posix()
        rows.append(f"| [{slug}]({link}) | {category} | {line} |")
    return "\n".join(rows)


def check_index(expected: str, write: bool) -> list[str]:
    text = README.read_text(encoding="utf-8")
    if INDEX_START not in text or INDEX_END not in text:
        return [f"{README.name}: marqueurs {INDEX_START} / {INDEX_END} introuvables"]
    pattern = re.compile(
        re.escape(INDEX_START) + r"\n.*?\n" + re.escape(INDEX_END),
        re.DOTALL,
    )
    replacement = f"{INDEX_START}\n{expected}\n{INDEX_END}"
    if not pattern.search(text):
        return [f"{README.name}: bloc d'index mal formé"]
    updated = pattern.sub(replacement, text, count=1)
    if write:
        if updated != text:
            README.write_text(updated, encoding="utf-8")
            print(f"index mis à jour dans {README.name}")
        return []
    if updated != text:
        return [
            f"{README.name}: l'index ne correspond pas aux skills "
            "(relancer avec --write-index)"
        ]
    return []


def scan_secrets() -> list[str]:
    errors: list[str] = []
    roots = [SKILLS_DIR, ROOT / "templates", README, ROOT / "CONTRIBUTING.md", ROOT / "NOTICE.md"]
    files: list[Path] = []
    for root in roots:
        if root.is_file():
            files.append(root)
        elif root.is_dir():
            files.extend(path for path in root.rglob("*") if path.is_file())
    for path in files:
        if path.suffix.lower() not in SCAN_SUFFIXES and path.name not in {"README.md", "NOTICE.md"}:
            continue
        # Textes de licence tiers (LICENSE.txt, polices OFL) : adresses d'auteurs publiques, à ne pas modifier.
        if path.name.upper().startswith("LICENSE") or path.stem.upper().endswith("-OFL"):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        relative = path.relative_to(ROOT)
        for match in EMAIL_RE.finditer(text):
            if EXAMPLE_DOMAIN_RE.search(match.group(0)):
                continue  # adresse d'exemple réservée (RFC 2606), pas une donnée personnelle
            errors.append(f"{relative}: adresse e-mail ({match.group(0)})")
        for match in SECRET_RE.finditer(text):
            errors.append(f"{relative}: secret potentiel ({match.group(0)[:8]}…)")
        if str(relative).startswith("skills/") and "/workspace/" in text:
            errors.append(f"{relative}: chemin /workspace/ (utiliser un placeholder)")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write-index",
        action="store_true",
        help="réécrire le tableau d'index du README entre les marqueurs",
    )
    args = parser.parse_args()
    errors: list[str] = []
    try:
        skills = iter_skills()
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1
    for category, slug, path, data, body in skills:
        errors.extend(validate_skill(category, slug, path, data, body))
    errors.extend(scan_secrets())
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    index_errors = check_index(render_index(skills), write=args.write_index)
    if index_errors:
        for error in index_errors:
            print(error, file=sys.stderr)
        return 1
    print(f"{len(skills)} skills valides")
    return 0


if __name__ == "__main__":
    sys.exit(main())
