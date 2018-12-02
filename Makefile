.PHONY: format test

SRC_DIR ?= src

format:
	black --line-length=120 $(SRC_DIR)

test:
	py.test --cov=. --cov-branch --verbose src/