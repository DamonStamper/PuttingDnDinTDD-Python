test: lint unitTest coverage

lint:
	flake8 DnDinTDD

coverage:
	pytest --junitxml=junit.xml --cov-config=setup.cfg --cov-report=xml --cov=DnDinTDD

unitTest:
	pytest