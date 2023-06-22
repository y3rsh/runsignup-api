#!make

ENV ?= prod

$(info $$ENV is [${ENV}])

$(if $(findstring $(ENV), prod),,$(error unknown environment "$(ENV)" specified))

ENV_FILE = $(ENV).env

-include $(ENV_FILE)
export

reqs:
	@poetry export -f requirements.txt -o requirements.txt


.PHONY: black
black:
	@poetry run python -m black .

.PHONY: black-check
black-check:
	@poetry run python -m black . --check

.PHONY: ruff
ruff:
	@poetry run python -m ruff . --fix

.PHONY: ruff-check
ruff-check:
	@poetry run python -m ruff .

.PHONY: lint
lint: black-check ruff-check

.PHONY: format
format: | black ruff

.PHONY: run
run:
	@poetry run python ./runsignup_api/runsignup_client.py
