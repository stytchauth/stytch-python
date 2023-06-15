.PHONY: help
help:
	@echo "Available commands"
	@grep -E '^[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) | sort


.PHONY: tests
tests:  # Run the unit tests
	python3 -m unittest

# A useful alias
.PHONY: test
test: tests # alias for tests

.PHONY: lint
lint: # Run the autoformatter and type checker
	black . && mypy .
