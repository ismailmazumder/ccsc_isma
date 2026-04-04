# CCSC GitHub Pages Search Site

This repository includes a static search page for CCSC profiles.

## Deploying to GitHub Pages

1. Ensure the repository contains:
   - `index.html` or `main.html`
   - `all_profiles.json`
   - `ccsc_love_pre_test/` folder with the `pic.jpg` files in each ID folder

2. Push the repository to GitHub.
3. Enable GitHub Pages for the repository from the `main` branch.
4. Open the published site URL.

## How it works

- The page is fully client-side JavaScript.
- It loads `all_profiles.json` with profile data.
- It displays images from `ccsc_love_pre_test/<ID>/pic.jpg`.

## Usage

- Open the site URL.
- Type a name or ID in the search box.
- Results are filtered in the browser.

## Notes

- No Python is required for GitHub Pages deployment.
- If the page cannot load, make sure files are in the repo and the site is served via GitHub Pages.
