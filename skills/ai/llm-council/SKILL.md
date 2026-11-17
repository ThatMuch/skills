---
name: llm-council
description: >-
  When the user wants several LLMs' opinions on a question, a decision
  cross-checked by a 'council' of models, or asks to run the LLM Council
  (karpathy/llm-council method): independent answers, anonymized peer ranking,
  then a chairman synthesis.
metadata:
  adapted_from: https://github.com/karpathy/llm-council
---
# LLM Council (based on github.com/karpathy/llm-council)

## À personnaliser

| Réglage | Quoi mettre | Où |
| --- | --- | --- |
| `OPENROUTER_API_KEY` | Clé API OpenRouter utilisée pour interroger le conseil | variable d'environnement de l'agent (`process.env`), jamais dans ce dépôt |

La liste de modèles par défaut se surcharge dans la conversation. On ne la fige pas ici avec un compte personnel.

Three stages: independent opinions, anonymized peer review, chairman synthesis.

## Setup
- Preferred: OpenRouter API key in `process.env.OPENROUTER_API_KEY` (ask for it with a secret request if missing). Endpoint `https://openrouter.ai/api/v1/chat/completions`, OpenAI-compatible.
- Default council (adjust to the latest models available on OpenRouter): `openai/gpt-5.1`, `google/gemini-3-pro-preview`, `anthropic/claude-sonnet-4.5`, `x-ai/grok-4`. Chairman: `google/gemini-3-pro-preview`. The user may override the list.
- Fallback without a key: run each council member as an independent background subagent with a distinct perspective, never sharing answers before stage 2, and say clearly it is a simulated council, not distinct models.

## Stage 1: first opinions
Send the user's question unchanged to every council model in parallel. Keep each successful answer with its model name; drop failures.

## Stage 2: anonymized review
Label answers Response A, B, C... (keep a private label-to-model map). Send each model the question plus all labeled answers with this instruction: evaluate each response (strengths, weaknesses), then end with exactly:
```
FINAL RANKING:
1. Response X
2. Response Y
```
Parse the FINAL RANKING block from each reply. Compute the aggregate ranking as the average position of each response across reviewers (lower is better).

## Stage 3: chairman synthesis
Give the chairman the question, all stage-1 answers (with model names) and all stage-2 reviews, and ask for a single best final answer that weighs the individual answers, the peer rankings, and points of agreement or disagreement.

## Delivery
Lead with the chairman's final answer. Then a short table of the aggregate ranking (model, average rank), and one or two lines on where the models disagreed. Offer the full individual answers on request. Never invent a model's output; report any model that failed.
