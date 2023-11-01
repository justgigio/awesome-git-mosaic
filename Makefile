
.PHONY: code-style
code-style:
	pipenv run pycodestyle --statistics --ignore=E501,E902 --count domain/ gateways/ handlers/ infrastructure/ usecases/ tests/

.PHONY: setup
setup:
	pipenv install --dev

.PHONY: test
test: code-style
	pipenv run py.test tests --cov=. --cov-report xml --cov-report term --cov-report html --cov-fail-under=90

.PHONY: build
build:
	python3 -m build
