IMAGE_NAME=rainbow-fatcat

.PHONY: help
.SILENT:

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
	python main.py

build-image: lint type-check freeze # Build docker image.
	docker build -t $(IMAGE_NAME) . --no-cache

run-image:
	docker run --env FATCAT_SECRET=${FATCAT_SECRET} $(IMAGE_NAME)
