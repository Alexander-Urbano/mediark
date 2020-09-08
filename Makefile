clean:
	find . -name '__pycache__' -exec rm -fr {} +
	rm -rf ./.cache
	rm -f .coverage
	rm -rf .mypy_cache

test:
	pytest

COVFILE ?= .coverage
PROJECT = mediark

coverage-application: 
	export COVERAGE_FILE=$(COVFILE); pytest --cov-branch \
	--cov=$(PROJECT)/application tests/application/ \
	--cov-report term-missing -x -s -W ignore::DeprecationWarning \
	-o cache_dir=/tmp/mediark/cache

coverage: 
	export COVERAGE_FILE=$(COVFILE); pytest --cov-branch \
	--cov=$(PROJECT) tests/ --cov-report term-missing -x -s -vv \
	-W ignore::DeprecationWarning -o cache_dir=/tmp/mediark/cache

update:
	pip-review --auto
	pip freeze > requirements.txt

serve:
	python -m $(PROJECT) serve

serve-dev:
	export instark_MODE=DEV; python -m $(PROJECT) serve

PART ?= patch

version:
	bump2version $(PART) mediark/__init__.py --tag --commit

install-all:
	pip install -r requirements.txt

uninstall-all:
	pip freeze | xargs pip uninstall -y

upgrade:
	pip-review --local --auto
	pip freeze > requirements.txt

deploy:
	ansible-playbook -c local -i localhost, setup/deploy.yml

local:
	./setup/local.sh

update:
	git clean -xdf
	git reset --hard
	git checkout master
	git pull --all