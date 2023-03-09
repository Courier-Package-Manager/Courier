# Copyright (c) 2023 Joshua Rose
.ONESHELL:

all:
	@clear
	@python -m pip install -r requirements.txt
	@clear
	echo "Installation finished."
	echo "Please ensure you execute from inside ./src"



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

