# Copyright (c) 2023 Joshua Rose

install:
	# @sh build/scripts/install.sh
	@python -m pip install -r requirements.txt
	@python -m pip install git+https://github.com/psf/black

lint:
	@python -m flake8 . --ignore F401 --show-source --statistics
	@python -m flake8 src --count --exit-zero --max-complexity=10 --max-line-length=79 --statistics

test:
	python -m coverage run -m unittest tests/test_unit_core.py

coverage:
	coverage report -m
  
upload:
	@sh upload-token.sh