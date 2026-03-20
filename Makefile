.PHONY: fmt typecheck check

fmt:
	uv run ruff format . && uv run ruff check --fix .

typecheck:
	uv run mypy .


check: fmt typecheck
