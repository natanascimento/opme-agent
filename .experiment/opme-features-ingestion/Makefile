SHELL := /bin/bash

.PHONY: help install run clean logs test lint format docker-build docker-run docker-shell
.DEFAULT: help

# Variables
PYTHON := python
UV := uv
SRC_DIR := src
VENV_DIR := .venv

help:
	@echo "OPME Ingestion - Makefile Commands"
	@echo "=================================="
	@echo ""
	@echo "make install"
	@echo "          Install project dependencies using uv"
	@echo "----------"
	@echo "make run"
	@echo "          Run the scraping process"
	@echo "----------"
	@echo "make clean"
	@echo "          Clean temporary files, cache, and logs"
	@echo "----------"
	@echo "make logs"
	@echo "          Show the latest log file"
	@echo "----------"
	@echo "make lint"
	@echo "          Run linter checks"
	@echo "----------"
	@echo "make format"
	@echo "          Format code with black"
	@echo "----------"
	@echo "make docker-build"
	@echo "          Build Docker image"
	@echo "----------"
	@echo "make docker-run"
	@echo "          Run scraping in Docker container"
	@echo "----------"
	@echo "make docker-shell"
	@echo "          Open shell in Docker container"
	@echo "----------"

install:
	@echo "Installing dependencies..."
	@echo "----------"
	$(UV) sync

run:
	@echo "Running OPME scraping..."
	@echo "----------"
	$(UV) run python -m $(SRC_DIR)

clean:
	@echo "Cleaning temporary files..."
	@echo "----------"
	find $(SRC_DIR) -type d -name "__pycache__" -exec rm -r {} + 2>/dev/null || true
	find $(SRC_DIR) -type f -name "*.pyc" -delete 2>/dev/null || true
	find $(SRC_DIR) -type f -name "*.pyo" -delete 2>/dev/null || true
	find $(SRC_DIR) -type f -name "*.pyd" -delete 2>/dev/null || true
	rm -rf $(SRC_DIR)/**/__pycache__ 2>/dev/null || true
	@echo "Cleaned Python cache files"
	@echo "----------"

clean-logs:
	@echo "Cleaning log files..."
	@echo "----------"
	rm -rf logs/*.log 2>/dev/null || true
	@echo "Cleaned log files"
	@echo "----------"

clean-all: clean clean-logs
	@echo "All temporary files cleaned"
	@echo "----------"

logs:
	@echo "Latest log file:"
	@echo "----------"
	@ls -t logs/*.log 2>/dev/null | head -1 | xargs cat 2>/dev/null || echo "No log files found"

lint:
	@echo "Running linter..."
	@echo "----------"
	$(UV) run ruff check $(SRC_DIR) || true

format:
	@echo "Formatting code..."
	@echo "----------"
	$(UV) run ruff format $(SRC_DIR) || true

test:
	@echo "Running tests..."
	@echo "----------"
	@echo "No tests configured yet"

docker-build:
	@echo "Building Docker image..."
	@echo "----------"
	docker build -t opme-ingestion:latest .

docker-run:
	@echo "Running OPME scraping in Docker..."
	@echo "----------"
	docker run --rm \
		-v $$(pwd)/logs:/app/logs \
		-v $$(pwd)/../datalake:/app/../datalake \
		opme-ingestion:latest

docker-shell:
	@echo "Opening shell in Docker container..."
	@echo "----------"
	docker run --rm -it \
		-v $$(pwd)/logs:/app/logs \
		-v $$(pwd)/../datalake:/app/../datalake \
		opme-ingestion:latest /bin/bash

