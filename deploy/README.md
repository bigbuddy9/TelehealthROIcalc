# Putting the ROI calculator on your website

## Option A: its own page (simplest)
1. Upload `roi-calculator.html` to your site, e.g. `joinrubymd.com/roi-calculator.html`.
2. Link to it from your site or send investors the URL.

## Option B: inside an existing page
1. Do Option A first.
2. Paste `embed-snippet.html` into the page (Webflow Embed, WordPress Custom HTML, Framer Embed).
3. Change the `src` in the snippet to your uploaded URL. The frame resizes itself.

## Changing the numbers
Edit the `DEFAULTS` block in `index.html` (investment, financing, ad spend, costs),
then rebuild and re-upload:

    python3 scripts/build.py

The page is marked `noindex` so search engines don't list it. Remove that meta tag
in `scripts/build.py` if you want it public.
