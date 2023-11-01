
.PHONY: code-style
code-style:
	poetry run pycodestyle --statistics --ignore=E501,E902 --count domain/ gateways/ handlers/ infrastructure/ usecases/ tests/

.PHONY: setup
setup:
	poetry install

.PHONY: test
test: code-style
	poetry run py.test tests --cov=. --cov-report xml --cov-report term --cov-report html --cov-fail-under=90

.PHONY: build
build:
	poetry build
