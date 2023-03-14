run:
	python -m black .
	python -m mypy src --config-file mypy.ini
	python -m coverage run -m pytest -s tests
	python -m coverage html
	python -m coverage report -m

black:
	python -m black .


blacken:
	python -m black .

lint:
	python -m pylint src/*.py

types:
	export MYPYPATH=buildconfig/stubs
	python -m mypy src --config-file mypy.ini

test:
	python -m coverage run -m pytest -s tests
	python -m coverage html
	python -m pylint src/*.py
	python -m coverage report -m

install:
	pip install -r requirements.txt
	# sh buildconfig/exports.sh
	@clear
	echo "Installation finished."
	echo "Please ensure you execute from inside ./src"
