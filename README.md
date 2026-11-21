# Quant Theory Lab

Infinite knowledge vault for **quantitative finance theory**.

Jupyter notebooks, academic papers, Quarto essays, model cards, data sources, curated datasets, and research projects. Scale by adding plugins. No hard limit.

Author: Le Tri Nhan

## Mental model

```
NOTEBOOKS     PAPERS        POSTS (Quarto)   PROJECTS      DATA / DATASETS / MODELS
theory .ipynb academic      site essays      experiments   manifests and packs
```

## Quick start

```bash
make setup
cp docs/env.example .env
make doctor
make list
```

### Add knowledge

```bash
make new-notebook NAME=heston-pde DOMAIN=derivatives
make new-paper NAME=local-vol-survey DOMAIN=derivatives
make new-post NAME=risk-neutral-pricing DOMAIN=asset_pricing
make new-project NAME=calib-sandbox DOMAIN=derivatives
make new-data NAME=fred-rates DOMAIN=fixed_income
make new-dataset NAME=bsm-toy DOMAIN=derivatives
make new-model NAME=black-scholes-merton DOMAIN=derivatives
```

### Publish essays (Quarto, not Substack)

```bash
make new-post NAME=risk-neutral-pricing
# edit posts/<slug>/index.qmd  → set draft: false
make preview
make render
make publish   # GitHub Pages when ready
```

See [docs/quarto.md](docs/quarto.md).

## Layout

```text
notebooks/   Jupyter theory
papers/      Academic articles and notes
posts/       Quarto essays (index.qmd)
projects/    Runnable research
data/        Data source manifests
datasets/    Curated packs
models/      Model cards and derivations
packages/    qtl-core, qtl-lab
lab/         Registry
_quarto.yml  Quarto website
_site/       Built site (gitignored)
artifacts/   Local outputs (gitignored)
```

## Current notebooks

| Plugin | Topic |
| --- | --- |
| [black-scholes-merton](notebooks/black-scholes-merton/) | Black-Scholes-Merton pricing |

## Related vaults

- [Investment Research Lab](https://github.com/letrinhandn/investment-research-lab)
- [Terminal Trade](https://github.com/letrinhandn/Terminal-Trade)
- Academic research monorepo (political economy and policy theory)

## License

MIT. Research and education only. Not investment advice.

> AI agents: read [AGENTS.md](AGENTS.md) first.
