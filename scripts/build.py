#!/usr/bin/env python3
"""Build the self-hosted RubyMD ROI calculator from index.html.

index.html is written as a page fragment (no <html>/<head>/<body>) so it can be
previewed as a claude.ai artifact. This wraps it into a complete HTML document
for your own website and adds a tiny script that reports the page height to a
parent page, so the iframe embed sizes itself.

Usage:  python3 scripts/build.py
Output: deploy/roi-calculator.html
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
src = (ROOT / "index.html").read_text(encoding="utf-8")

split_at = src.index('<div class="wrap">')
head_part, body_part = src[:split_at].strip(), src[split_at:].strip()

AUTO_HEIGHT = """<script>
/* Tell a parent page (iframe embed) how tall the calculator is. */
(function () {
  if (window.parent === window) return;
  var last = 0;
  function send() {
    var h = document.documentElement.scrollHeight;
    if (h !== last) { last = h; window.parent.postMessage({ type: 'rubymd-roi-height', height: h }, '*'); }
  }
  window.addEventListener('load', send);
  window.addEventListener('resize', send);
  if (window.ResizeObserver) new ResizeObserver(send).observe(document.body);
})();
</script>"""

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Projected clinic economics against the full cost of investment. Projections only, not guaranteed results.">
<meta name="robots" content="noindex">
<style>html {{ color-scheme: light; }} body {{ margin: 0; }} img {{ max-width: 100%; }} [hidden] {{ display: none !important; }}</style>
{head_part}
</head>
<body>
{body_part}
{AUTO_HEIGHT}
</body>
</html>
"""

out = ROOT / "deploy" / "roi-calculator.html"
out.parent.mkdir(exist_ok=True)
out.write_text(page, encoding="utf-8")
print(f"Wrote {out.relative_to(ROOT)} ({len(page):,} bytes)")
