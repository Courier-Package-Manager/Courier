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

cov-integrity-check:
	curl https://keybase.io/codecovsecurity/pgp_keys.asc | gpg --no-default-keyring --keyring trustedkeys.gpg --import # One-time step

	curl -Os https://uploader.codecov.io/latest/linux/codecov

	curl -Os https://uploader.codecov.io/latest/linux/codecov.SHA256SUM

	curl -Os https://uploader.codecov.io/latest/linux/codecov.SHA256SUM.sig

	gpgv codecov.SHA256SUM.sig codecov.SHA256SUM

	shasum -a 256 -c codecov.SHA256SUM

	chmod +x codecov
	./codecov -t d54134f1-9646-4d26-9103-869ca53abad9

