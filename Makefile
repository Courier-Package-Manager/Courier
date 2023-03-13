run:
	black .
	mypy --check-untyped-defs src
	coverage run -m pytest -s tests
	coverage html
	coverage report -m

black:
	black .


blacken:
	black .

lint:
	pylint src/*.py

types:
	mypy --check-untyped-defs src

test:
	coverage run -m pytest -s tests
	coverage html
	pylint src/*.py
	coverage report -m

install:
	pip install -r requirements.txt
	sh buildconfig/exports.sh
	@clear
	echo "Installation finished."
	echo "Please ensure you execute from inside ./src"

