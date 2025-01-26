install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest -vv --cov=hello test_hello.py
	#python -m pytest -vvv --cov=hello --cov=greeting \
	#	--cov=smath --cov=web tests
	#python -m pytest --nbval notebook.ipynb	#tests our jupyter notebook
	#python -m pytest -v tests/test_web.py #if you just want to test web

format:
	black *.py

lint:
	pylint --disable=R,C *.py

all: install lint test format