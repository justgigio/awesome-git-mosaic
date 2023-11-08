
.PHONY: code-style
code-style:
	poetry run pycodestyle --statistics --ignore=E501,W503,E902 --count src

.PHONY: setup
setup:
	poetry install

.PHONY: test-only
test-only:
	poetry run py.test tests --no-cov

.PHONY: build
build:
	poetry build

.PHONY: mypy
mypy:
	poetry run mypy src

.PHONY: black-check
black-check:
	poetry run black --check --diff src

.PHONY: black
black:
	poetry run black src

.PHONY: isort-check
isort-check:
	poetry run isort --ac --check-only src

.PHONY: isort
isort:
	poetry run isort --ac src

.PHONY: check
check: code-style isort-check black-check mypy

.PHONY: format
format: isort black

.PHONY: test
test: check
	poetry run py.test tests --cov=. --cov-report xml --cov-report term --cov-report html --cov-fail-under=90
