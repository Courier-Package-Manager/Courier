python -m black .
python -m mypy src --config-file mypy.ini
python -m coverage run -m pytest -s tests
python -m coverage html
python -m coverage report -m
