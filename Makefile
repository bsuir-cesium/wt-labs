.PHONY: fmt typecheck check lab1 lab2

fmt:
	uv run ruff format . && uv run ruff check --fix .

typecheck:
	uv run mypy .

lab1:
	cd lab1 && docker build -t lab1 . && docker run --rm -p 8080:80 lab1

lab2:
	cd lab2 && docker build -t lab2 . && docker run --rm -p 8080:80 lab2

check: fmt typecheck
