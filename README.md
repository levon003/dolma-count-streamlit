# Dolma counts

Simple Streamlit app showing word counts for AI2's Dolma dataset.

View the app here: https://dolma-count-levon003.streamlit.app/

Read more: https://blog.allenai.org/dolma-3-trillion-tokens-open-llm-corpus-9a0ff4b8da64

## Local development setup

### First-time setup

This repository uses Conda to manage two dependencies: Python and Poetry. ([This SO post](https://stackoverflow.com/a/71110028) provides more context on using Conda and Poetry together.)

Install conda or miniconda. Then, create the needed environment, called `dolma-count`.

```bash
conda env create -f conda-environment.yml
```

Note that the environment file can't be called `environment.yml` because of how Streamlit resolves dependencies.

### Python development

1. Activate the conda environment: `conda activate dolma-count`
2. Use `make install` to install all needed dependencies (including the pre-commit hooks).

Ideally, the Makefile would activate the needed conda environment, but I don't actually know enough `make` to add that.

### Other useful commands

 - `poetry run <command>` - Run the given command, e.g. `poetry run pytest`.
 - `source $(poetry env info --path)/bin/activate` - An alternative to `poetry shell` that's less buggy in conda environments.
 - `poetry add <package>` - Add the given package as a dependency. Use flag `-G dev` to add it as a development dependency.
 - `conda remove -n dolma-count --all` - Tear it all down, so first-time setup can be repeated.

 ### "Dolma"

 According to AI2's blog post, Dolma stands for "Data to feed OLMo's Appetite". For me, it immediately made me think of the Armenian/Ottoman dish ["dolma"](https://en.wikipedia.org/wiki/Dolma). I used the stone emoji 🪨 as the app icon to evoke the "dolma rock" that my father used to weight the wrapped bundles down while boiling.
