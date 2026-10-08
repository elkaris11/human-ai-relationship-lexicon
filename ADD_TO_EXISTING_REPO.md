# Additions package instructions

This ZIP is an overlay for the existing `human-ai-relationship-lexicon` repository.

1. Extract the ZIP.
2. Copy the contents of `lexicon-repo-additions` into the root of the existing repository.
3. Allow Windows to merge folders and replace the existing partial `lexicon/INDEX.md` and `lexicon/SCHEMA.md`.
4. In VS Code Source Control, review the additions.
5. Stage all changes and commit with a message such as `Populate Community Edition v1.0 lexicon`.
6. Run `python automation/validate_repository.py` before publishing if Python dependencies are installed.

The package does not contain a `.git` directory and cannot overwrite repository history.
