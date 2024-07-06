.PHONY: gendiff
install:
				poetry install
build:
				poetry build
publish:
				poetry publish --dry-run
package-install:
				python3 -m pip install --user dist/*.whl
package-update:
				poetry build
				python3 -m pip install dist/*.whl --upgrade --user
lint:
				poetry run flake8 gendiff
help:
				poetry run gendiff --help