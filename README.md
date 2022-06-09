# Flask Rest API to Iris ML
An example of rest api to use a machine learning model.

## Create a virtual environment
```
$ virtualenv flaskvenv
$ source flaskvenv/bin/activate
```

## Installing the dependencies
```
$ pip install -r requirements.txt
```

## Running the APP
- Localy
```
$ export FLASK_APP=src/app/server
$ flask run
```
- Dockerized
```
$ docker build --tag server-quickstart .
$ docker run server-quickstart:latest
```

## Utility Commands
To check lib versions
```
$ pip list
```