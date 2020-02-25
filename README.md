# flask-microservice-example
Python Flask app with basic structure and example of  API

## Ways to start up:

---

### 1. without Docker
Install requirements
```
pip install -r requirements.txt
```
Run tests:
```
python -m unittest server/tests/*.py
```
Start server: (in case of `ModuleNotFoundError`, run `export PYTHONPATH=.`)
```
python server/app.py
```
Visit: [API documentation](http://0.0.0.0:8080)

---

### 2. with Docker
Run Docker compose
```
docker-compose up
```
Visit: [API documentation](http://0.0.0.0:8080)



