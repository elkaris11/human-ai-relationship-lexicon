# Automation Design

## Intake

The issue form creates a structured proposal. `proposal-intake.yml` adds lifecycle labels and posts guidance.

## Analysis

`automation/analyze_proposal.py` performs deterministic, explainable checks:

- normalized spelling similarity using `difflib`
- token-set definition overlap using Jaccard similarity
- required-field checks for markdown seedling files
- Semantic Neighbor candidates rather than automatic duplicate rejection

This baseline deliberately avoids paid APIs. A future optional semantic service can add embeddings, but its model, version, thresholds, privacy behavior, and limitations must be documented.

## Voting

`vote-tally.yml` runs on a schedule or manual dispatch. It fetches open proposal issues, counts 👍 and 👎 reactions, calculates net support and opposition ratio, and adds or removes the `stage: ready-for-harvest` label when numeric eligibility is met.

## Promotion

`automation/promote_term.py` moves a reviewed seedling into `lexicon/terms/`, updates status metadata, and preserves proposal history. Promotion is a maintainer action after human review.

## Guardrails

- No automated acceptance or rejection.
- No sentiment analysis of contributor identity.
- No private data sent to third-party AI services by default.
- All thresholds are visible and version-controlled.
- Analyzer output is advisory and challengeable.
