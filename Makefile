IMAGE_NAME=rainbow-fatcat
PROJECT_DIR=rainbow_fatcat
LOCALE_DIR=${PROJECT_DIR}/locale

.PHONY: help
.SILENT: load-env

help: # Show this help message.
	@grep -E '^[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: # Install requirements of project.
	poetry install

freeze: # Export the requirements.txt file.
	poetry export --without-hashes -f requirements.txt --output requirements.txt

lint: # Lint the code.
	flake8

type-check: # Check the type.
	mypy

start: # Start the bot.
	python rainbow_fatcat/app.py

build-image: babel-compile # Build docker image.
	docker build -t $(IMAGE_NAME) . --no-cache

run-image: load-env # Run docker image.
	docker top $(IMAGE_NAME) || \
	docker run -d --name $(IMAGE_NAME) --env FATCAT_SECRET=${FATCAT_SECRET} $(IMAGE_NAME)

stop-container: # Stop container.
	docker stop $(IMAGE_NAME) && \
	docker rm $(IMAGE_NAME)

babel-extract: # Extract the strings need to be translated.
	pybabel extract ${PROJECT_DIR} -o ${LOCALE_DIR}/base.pot

babel-init: # Initialize locale catelog.
	for locale in ja en zh ; do \
		pybabel init -l $$locale -i ${LOCALE_DIR}/base.pot -d ${LOCALE_DIR} ; \
	done

babel-compile: # Compile catelog.
	pybabel compile -d ${LOCALE_DIR}

babel-update: # Update catelog.
	pybabel update -i ${LOCALE_DIR}/base.pot -d ${LOCALE_DIR}

load-env: # Load environment variable from .env file.
	if [ -f ".env" ]; then \
		export $(cat .env | xargs); \
	else \
		echo "No .env file."; \
	fi

format: # Format the code.
	black .

update-deps:
	poetry update;

update-requirements: update-deps freeze
