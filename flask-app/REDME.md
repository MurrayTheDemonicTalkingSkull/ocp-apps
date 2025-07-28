# Set environment variable
APP_FILE=app.py

oc new-project python-app
oc new-app python:3.11~https://github.com/youruser/python-hello --name=python-hello
oc expose svc/python-hello
