code-style:
	pipenv run pycodestyle --statistics --ignore=E501,E902 --count domain/ gateways/ handlers/ infrastructure/ usecases/ tests/

setup:
	pipenv install --dev

test: code-style
	pipenv run py.test tests --cov=. --cov-report xml --cov-report term --cov-report html --cov-fail-under=90
