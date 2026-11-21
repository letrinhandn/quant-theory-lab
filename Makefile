.PHONY: help setup sync doctor list \
        new-notebook new-paper new-post new-project new-data new-dataset new-model \
        preview render publish quarto-doctor \
        lint test

REPO := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
QTL := cd $(REPO) && uv run --python 3.12 python -m qtl_lab.cli
QUARTO ?= $(shell command -v quarto 2>/dev/null || echo $(HOME)/.local/bin/quarto)

NAME ?=
DOMAIN ?= general
KIND ?=

help:
	@echo "Quant Theory Lab"
	@echo ""
	@echo "  make setup                 Install workspace"
	@echo "  make doctor                Health check"
	@echo "  make list                  List all plugins"
	@echo "  make new-notebook NAME=x   Theory Jupyter notebook"
	@echo "  make new-paper NAME=x      Academic paper"
	@echo "  make new-post NAME=x       Quarto essay post"
	@echo "  make new-project NAME=x    Research project"
	@echo "  make new-data NAME=x       Data source manifest"
	@echo "  make new-dataset NAME=x    Curated dataset pack"
	@echo "  make new-model NAME=x      Model card / derivation"
	@echo "  make preview               Quarto live preview"
	@echo "  make render                Build Quarto site to _site/"
	@echo "  make publish               Publish to GitHub Pages (when ready)"
	@echo "  make quarto-doctor         Quarto install check"
	@echo "  make lint                  Ruff"
	@echo "  make test                  Pytest"

setup sync:
	cd $(REPO) && uv sync --all-groups

doctor:
	$(QTL) doctor

list:
	$(QTL) list

new-notebook:
	@test -n "$(NAME)" || (echo "NAME= required" && exit 1)
	$(QTL) new notebook $(NAME) --domain $(DOMAIN)

new-paper:
	@test -n "$(NAME)" || (echo "NAME= required" && exit 1)
	$(QTL) new paper $(NAME) --domain $(DOMAIN)

new-post:
	@test -n "$(NAME)" || (echo "NAME= required" && exit 1)
	$(QTL) new post $(NAME) --domain $(DOMAIN)

new-project:
	@test -n "$(NAME)" || (echo "NAME= required" && exit 1)
	$(QTL) new project $(NAME) --domain $(DOMAIN)

new-data:
	@test -n "$(NAME)" || (echo "NAME= required" && exit 1)
	$(QTL) new data $(NAME) --domain $(DOMAIN)

new-dataset:
	@test -n "$(NAME)" || (echo "NAME= required" && exit 1)
	$(QTL) new dataset $(NAME) --domain $(DOMAIN)

new-model:
	@test -n "$(NAME)" || (echo "NAME= required" && exit 1)
	$(QTL) new model $(NAME) --domain $(DOMAIN)

quarto-doctor:
	@$(QUARTO) --version
	cd $(REPO) && $(QUARTO) check

preview:
	cd $(REPO) && $(QUARTO) preview

render:
	cd $(REPO) && $(QUARTO) render

publish:
	cd $(REPO) && $(QUARTO) publish gh-pages --no-prompt

lint:
	cd $(REPO) && uv run ruff check packages

test:
	cd $(REPO) && uv run pytest
