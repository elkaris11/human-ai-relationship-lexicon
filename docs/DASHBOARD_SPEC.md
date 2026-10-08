# Lexicon Dashboard Specification

## Goal

Generate a public, read-only snapshot of the Core Lexicon and Thinkgarden without replacing proposal issues as the source of voting truth.

## Summary cards

- Accepted Core Terms
- Active Seedlings
- Germinating Terms
- Growing Terms
- Ready for Harvest
- Harvested This Release
- Composted or Withdrawn

## Lists

- Newest seedlings
- Terms approaching the end of incubation
- Terms numerically eligible for harvest review
- Most referenced Semantic Neighbors
- Latest accepted terms
- Contributors, subject to privacy and attribution choices

## Seedling fields

- term
- category
- stage
- proposal issue
- submitted date
- planned incubation end
- support and opposition reaction counts
- net vote
- opposition ratio
- candidate Semantic Neighbors
- maintainer review status

## Generation rules

- Generate from repository files and public GitHub issue metadata.
- Never expose private contributor information.
- Clearly label automated analysis as advisory.
- Do not display a term as accepted until a maintainer completes harvest review.
- Preserve archived outcomes for transparency.
