PYTHON_BIN=python3
PIP_BIN=pip3
MANAGE_FILE=manage.py
REQUIREMENTS_FILE=requirements.txt


help:
	@echo 'Makefile for Django Ecoleta Api                                            '
	@echo '                                                                           '
	@echo 'Usage:                                                                     '
	@echo '   make setup    install dependencies and execute migrations and fixtures  '
	@echo '   make run      run Django built-in server                                '


setup:
	@$(PIP_BIN) install -r $(REQUIREMENTS_FILE)
	@$(PYTHON_BIN) $(MANAGE_FILE) migrate
	@$(PYTHON_BIN) $(MANAGE_FILE) loaddata items

run:
	@$(PYTHON_BIN) $(MANAGE_FILE) runserver

test:
	@$(PYTHON_BIN) $(MANAGE_FILE) test $(app)
