# Copyright (c) 2023 Joshua Rose
install:
	# @sh build/scripts/install.sh
	@clear
	@python -m pip install -r requirements.txt
	@python -m pip install git+https://github.com/psf/black

lint:
	@clear
	@python -m pylint src/*.py

cov:
	@clear
	# ============= RUNNING NEW TEST =============== #
	@python -m coverage run -m unittest discover
	# ============= REPORT =============== #
	@python -m coverage report -m
	@python -m coverage html

