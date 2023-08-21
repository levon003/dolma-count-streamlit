.PHONY: help install ensure-poetry install-precommits install-kernel test run-streamlit build-docker run-docker

help:
	@echo "Relevant targets are 'install' and 'test'."

install:
	@$(MAKE) ensure-poetry
	@$(MAKE) install-precommits
	@$(MAKE) install-kernel

ensure-poetry:
	@if [ "$(shell which poetry)" = "" ]; then \
		echo "Did you activate the outer conda environment? Run: conda activate dolma-count"; \
		exit 1; \
	else \
		echo "Found existing Poetry installation at $(shell which poetry)."; \
	fi
	@poetry install

install-precommits:
	@poetry run pre-commit autoupdate
	@poetry run pre-commit install --overwrite --install-hooks

install-kernel:
	@poetry run ipython kernel install --user --name=dolma-count

jupyter:
	@echo "Assuming Jupyter lab is installed and configured globally."
	@jupyter lab

test:
	@poetry run pytest --cov=src --cov-report term-missing


run-streamlit:
	@streamlit run src/streamlit_app.py --server.port 8080 --
