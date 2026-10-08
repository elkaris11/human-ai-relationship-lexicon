# Contributing

## Proposing a seedling

Use the **New term proposal** issue form. Include:

- term and pronunciation, if unclear
- part of speech
- one-sentence definition
- natural example sentence
- why the term fills a language gap
- suggested category
- possible Semantic Neighbors
- usage boundaries or risks

## What happens next

The proposal receives `stage: seed`, then automated analysis. If complete, maintainers move it to `stage: germinating` in the Thinkgarden. Community members test the word in discussion and vote on the proposal issue.

## Semantic Neighbors, not duplicate panic

Definition overlap does not automatically disqualify a term. A proposal may be:

- an exact duplicate
- a spelling variant
- a register variant, such as professional versus playful
- a narrower or broader term
- a regional or community variant
- a true synonym worth cross-listing

Accepted entries include a **Semantic Neighbors** section explaining the relationship.

## Pull requests

- One term or governance change per pull request when practical.
- Do not edit vote totals by hand.
- Run `python automation/validate_repository.py` before submitting.
- Explain why the revision improves clarity, usefulness, or governance.

## Human authority

Automation may classify, compare, summarize, and flag. Maintainers and the community make final decisions.
