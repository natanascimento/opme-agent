SHELL := /bin/bash

.PHONY: help setup setup-info setup-down api-logs install
.DEFAULT: help

help:
	@echo "make setup"
	@echo "          Setup project"
	@echo "----------"
	@echo "make setup-info"
	@echo "          View infrastructure status"
	@echo "----------"
	@echo "make setup-down"
	@echo "          Removing the infrastructure"
	@echo "----------"
	@echo "make api-logs"
	@echo "          Read logs on docker container"
	@echo "----------"
	@echo "make install"
	@echo "          Install packages"
	@echo "----------"

build-api:
	@echo "Building docker image of api"
	@echo "----------"
	docker build -t agent-api:latest api/

build-chat:
	@echo "Building docker image of chat"
	@echo "----------"
	docker build -t agent-chat:latest chat/

build: build-api build-chat
	@echo "Setting up the project ..."
	@echo "----------"
	docker compose up -d

down:
	@echo "Removing infrastructure ..."
	@echo "----------"
	docker compose down