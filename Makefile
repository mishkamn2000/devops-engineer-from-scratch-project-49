install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games

format:
	uv run ruff format brain_games

check:
	uv run ruff check --output-format=github brain_games
