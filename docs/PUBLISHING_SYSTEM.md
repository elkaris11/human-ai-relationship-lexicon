# Publishing System

The Markdown files in `lexicon/terms/` are the source of truth.

## Generated outputs

`automation/build_publications.py` creates:

- `build/Human_AI_Relationship_Lexicon.docx`
- `build/Human_AI_Relationship_Lexicon.md`
- `build/site/`, the static website

The GitHub Pages workflow converts the Word booklet to PDF, adds all three downloads to the website, uploads a workflow artifact, and deploys the site.

## Local build

```powershell
python -m pip install -r requirements-publications.txt
python automation/build_publications.py
```

If LibreOffice is installed, create the PDF locally:

```powershell
& "C:\Program Files\LibreOffice\program\soffice.exe" --headless --convert-to pdf --outdir build build\Human_AI_Relationship_Lexicon.docx
```

Generated files in `build/` should not be committed. GitHub Actions rebuilds them from the source files.

## Activate GitHub Pages

After pushing this system, open repository **Settings → Pages**. Under **Build and deployment**, select **GitHub Actions** as the source. Then open **Actions** and manually run **Build booklets and deploy Pages**, or push a qualifying change to `main`.

## Create a versioned release

Create and push a tag such as `v1.0.0`. The release workflow builds DOCX, PDF, and Markdown editions, creates the release, and attaches the files.
