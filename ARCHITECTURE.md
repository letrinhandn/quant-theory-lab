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

## Scaling

- Infinite plugins via `make new-*`
- Shared conventions in `AGENTS.md`
- Data caches and compiled outputs stay in `artifacts/`
- Theory notebooks and academic papers can feed Substack posts without leaving the vault

## Boundaries

- This lab: theory, pedagogy, papers, essays, research data
- Investment Research Lab: investment memos and idea pipeline
- quant-trading / Terminal Trade: production systems and market UIs
