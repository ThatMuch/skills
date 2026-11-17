---
name: podcast-to-vertical-shorts
description: >-
  When cutting a long podcast or interview video (e.g. YouTube) into viral
  vertical shorts for TikTok, Reels or YouTube Shorts.
metadata:
  adapted_from: https://github.com/coreyhaines31/marketingskills
---
# Podcast to vertical shorts

Adapted from the marketingskills `video` skill (repurposing + edit anatomy), focused on long-form to short-form.

## 1. Source
1. Download with yt-dlp (<=1080p mp4) plus auto-subs in the episode language and info.json. On HTTP 429 or bot check, wait ~20 min and retry; never ship a 360p fallback.
2. If subs lack per-word timing, get word timestamps with faster-whisper (word_timestamps=True) on the clip's audio instead of estimating from lines. Word-sync matters.

## 2. Pick moments
- 20-60 s, self-contained, understandable with zero context.
- Shock or contrarian line within the first 2 s (no intro, no greeting). Concrete story > abstract talk.
- Prefer topics the channel's strategy prioritises; avoid themes that already flopped unless re-hooked.
- Tighten by cutting repeated lines, fillers, silences >0.5 s and interjections; segments may be reordered if meaning stays intact.
- Ending should loop: last line flows back into the first.

## 3. Edit spec (apply to every short)
- 1080x1920 9:16, H.264 + AAC.
- **Safe zone (platform UI):** keep all text and key face framing inside the content window. On a 1080×1920 canvas use margins top **250 px**, bottom **380 px**, left/right **120 px** each (content ≈ x 120–960, y 250–1540). Overlay a safe-zone template on check frames when available.
- Reframe: track faces (OpenCV; fall back to manual crop when caps/shadows break detection) and switch crop at every source camera cut. Prefer stable face framing; avoid aggressive punch-ins unless the moment needs it.
- Captions: always on (most social video is watched muted). Bold condensed font (e.g. Anton / Work Sans), uppercase, 1-3 words at a time, white with black outline, active word / keywords highlighted. Keep captions inside the safe zone (not in the bottom UI band). Fix auto-sub errors and drop fillers.
- Hook text at the top of the **content** zone from frame 1 (just below the top margin), wrapped to max 3 lines, fades ~3-3.5 s. Keep the hook compact: smaller type that does not dominate the frame or collide with YouTube Shorts UI.
- Authentic over polished; no AI-generated text in video (overlays only).
- Leave music to the publishing app unless asked.

## 4. Deliverables
- Three files per short: `_hookA` (hook A on screen), `_hookB` (alternate hook), `_clean` (subtitles, no hook text).
- Verify by extracting frames (start, hook, a camera cut, end): face centred, text inside safe zone, subs synced.
- Report per short: path, episode, theme, duration, source timestamps, hook A, hook B, and anything to check.

## 5. Optional: copy a reference edit
To match a viral edit's style, break the reference into a beat sheet (cut rhythm, caption style, punch-ins, on-screen text, sound) and its 3-5 signature moves, then apply those to your footage. Copy the grammar only, never footage, script or music.
