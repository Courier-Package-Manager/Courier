# Copyright (c) 2023 Joshua Rose

install:
	@sh libs/install.sh
	@python -m pip install -r requirements.txt
	@python -m pip install git+https://github.com/psf/black

lint:
	@echo "Getting active workflows"
