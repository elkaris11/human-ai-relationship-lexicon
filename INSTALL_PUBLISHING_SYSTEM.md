# Install the booklet and GitHub Pages system

1. Copy the contents of this overlay into the root of the existing repository.
2. Add `build/` to the existing `.gitignore` file. The included `.gitignore-additions.txt` contains that line.
3. Optionally copy the text from `README_PUBLISHING_SNIPPET.md` into the main `README.md`.
4. Commit and push with a message such as `Add automatic booklet and Pages publishing`.
5. On GitHub, open **Settings → Pages**.
6. Under **Build and deployment**, set **Source** to **GitHub Actions**.
7. Open **Actions → Build booklets and deploy Pages → Run workflow**.
8. When the workflow succeeds, its deployment summary provides the public site link.

Every later qualifying push to `main` rebuilds and republishes the website and booklets.
