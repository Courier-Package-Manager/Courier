# Copyright (c) 2023 Joshua Rose

install:
	# @sh build/scripts/install.sh
	@python -m pip install -r requirements.txt
	@python -m pip install git+https://github.com/psf/black

lint:
	@python -m flake8 . --ignore F401 --show-source --statistics
	@python -m flake8 src --count --exit-zero --max-complexity=10 --max-line-length=79 --statistics

coverage:
	curl -X POST --data-binary @codecov.yml https://codecov.io/validate
	coverage report -m

test:
	@python -m coverage run -m unittest discover
	@python -m coverage report 
	@python -m coverage html
