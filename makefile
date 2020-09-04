test: lint unitTest coverage

lint:
	flake8 DnDinTDD

coverage:
	pytest --cov=. tests/

unitTest:
	pytest