.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"
VERSION := 0.1.1
help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

test: ## run tests quickly with the default Python
	poetry run pytest

dist: clean ## builds source and wheel package
	#poetry run python setup.py sdist
	#poetry run python setup.py bdist_wheel
	poetry build
	ls -lht dist

hist: ## show commit incremental changelog
	# https://commitizen-tools.github.io/commitizen/
	#pip install commitizen -i https://pypi.tuna.tsinghua.edu.cn/simple
	#cz bump --dry-run --increment patch
	cz ch --incremental --dry-run

pypi: clean ## package and upload a release
	cz bump --yes -ch -cc --increment patch --dry-run
	poetry publish --build --skip-existing --dry-run

bump: ## bump version.
	# https://commitizen-tools.github.io/commitizen/
	# https://keepachangelog.com/zh-CN/
	#cz bump --dry-run --yes -ch -cc --increment {MAJOR,MINOR,PATCH}
	@cz bump --yes -ch -cc --increment patch --dry-run

# DO NOT DELETE
