# Quarto publishing

Posts are Quarto essays under `posts/<slug>/index.qmd`. This replaces Substack.

## Workflow

```bash
make new-post NAME=risk-neutral-pricing DOMAIN=asset_pricing
# edit posts/risk-neutral-pricing/index.qmd
# set draft: false when ready

make preview    # local site
make render     # build _site/
make publish    # GitHub Pages (first time needs gh auth + Pages enabled)
```

## Front matter

```yaml
---
title: "Risk-neutral pricing"
description: "..."
author: "Le Tri Nhan"
date: 2026-11-21
categories: [theory, asset-pricing]
draft: false
---
```

Draft posts (`draft: true`) stay out of the published listing when you render with Quarto's draft rules; keep `config.yaml` `status: draft` until you ship.

## Publish target

Default: GitHub Pages via `quarto publish gh-pages`.

1. Repo Settings → Pages → Source: `gh-pages` branch
2. `make publish`
3. Site URL: `https://letrinhandn.github.io/quant-theory-lab`

Alternative: [Quarto Pub](https://quartopub.com) with `quarto publish quarto-pub`.

## Install

Quarto CLI is expected on `PATH`, or at `~/.local/bin/quarto`.

Env templates live in `docs/env.example` (not `.env.example`) so Quarto does not treat empty keys as required.
