# Architecture

## Overview

```
Makefile + qtl CLI
        |
   filesystem plugins          packages (uv workspace)
   notebooks papers posts      qtl-core
   projects data datasets      qtl-lab
   models
        |
   artifacts/ (gitignored)
```

## Plugin pattern

Every unit of knowledge is a folder plugin under a typed root. Discovery is filesystem-first. `lab/registry.yaml` holds optional metadata.

## Publishing

Quarto website at repo root (`_quarto.yml`). Essay listing reads `posts/*/index.qmd`. Build to `_site/`. Publish with `make publish` (GitHub Pages).

## Scaling

- Infinite plugins via `make new-*`
- Shared conventions in `AGENTS.md`
- Data caches and compiled outputs stay in `artifacts/`
- Theory notebooks and academic papers can feed Quarto essays without leaving the vault

## Boundaries

- This lab: theory, pedagogy, papers, Quarto essays, research data
- Investment Research Lab: investment memos, alphas, reports, Quarto essays
- quant-trading / Terminal Trade: production systems and market UIs
