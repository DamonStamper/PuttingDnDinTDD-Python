test: unitTestCoverage lint

lint:
	flake8 DnDinTDD

unitTestCoverage:
	pytest --junitxml=junit.xml --cov-config=setup.cfg --cov-report=xml --cov=DnDinTDD