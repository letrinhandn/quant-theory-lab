# AGENTS.md — Quant Theory Lab

Read this first. This repo is an infinite knowledge vault for quantitative finance theory.

## Mental model

```
NOTEBOOKS          PAPERS            POSTS (Substack)     PROJECTS
notebooks/<slug>/  papers/<slug>/    posts/<slug>/        projects/<slug>/
  *.ipynb            chapters/         draft.md             run.py + config.yaml
  config.yaml        config.yaml       config.yaml

DATA               DATASETS          MODELS
data/<slug>/       datasets/<slug>/  models/<slug>/
  manifest.yaml      config.yaml       config.yaml
```

One CLI: `python -m qtl_lab.cli` (alias `qtl` after `uv sync`)

## Commands

```bash
make setup
make doctor
make list

make new-notebook NAME=heston-pde DOMAIN=derivatives
make new-paper NAME=local-vol-notes DOMAIN=derivatives
make new-post NAME=what-is-risk-neutral DOMAIN=asset_pricing
make new-project NAME=calib-demo DOMAIN=derivatives
make new-data NAME=yahoo-options DOMAIN=derivatives
make new-dataset NAME=bsm-toy-panel DOMAIN=asset_pricing
make new-model NAME=black-scholes-merton DOMAIN=derivatives
```

## Directory contract

| Path | Purpose | Required |
|------|---------|----------|
| `notebooks/<slug>/` | Jupyter theory | `config.yaml`, notebook file |
| `papers/<slug>/` | Academic paper | `config.yaml`, `chapters/` or manuscript |
| `posts/<slug>/` | Substack / essay | `config.yaml`, `draft.md` |
| `projects/<slug>/` | Runnable research | `config.yaml`, `run.py` |
| `data/<slug>/` | Data source | `manifest.yaml` |
| `datasets/<slug>/` | Curated pack | `config.yaml` |
| `models/<slug>/` | Model card | `config.yaml`, notes |

Slug rules: kebab-case, lowercase, no leading `_`.

## Artifacts

Use `qtl_core.paths`. Outputs go under `artifacts/` (gitignored).

```
artifacts/data/
artifacts/notebooks/
artifacts/papers/
artifacts/posts/
artifacts/projects/
artifacts/runs/
```

## Anti-patterns

- Hardcode `artifacts/` paths
- Commit `.env` or large raw dumps
- Put one-off scripts at repo root (extend CLI / plugins)
- Mix live brokerage production into this theory vault
