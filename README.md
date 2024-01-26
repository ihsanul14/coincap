# Coincap
Simple API server to get some cryptocurrency latest price in IDR based on https://docs.coincap.io.
1. Build a JSON REST API service using Python FASTAPI as a backend of a cryptocurrencies price tracker web app.
2. Use https://docs.coincap.io as a source of the price.
3. Use SQLite as database.
4. Implement REST API endpoints to do:
- Signup (email, password, password confirmation)
- Signin (email and password). API user will get a JWT Token to identify user.
- Authenticated user can signout.
- Authenticated user can show user list of tracked coins (name of coin andprice in rupiah)
- Authenticated user can add coin to tracker.
- Authenticated user can remove coin from tracker.

# API Details
- POST `/api/signup` : signup a user
- POST `/api/signin` : signin a user to get authentication token
- POST `/api/logout` : logout an authenticated user
- DELETE `/api/user/delete` : delete a user
- GET `/api/tracker` : get list of coins for authenticated user
- POST `/api/tracker` : add/update token list for authenticated user
- DELETE `/api/tracker/{id}` : delete a token for authenticated user

# How to Run (locally)

1. clone the repository `git clone https://github.com/ihsanul14/coincap.git`
2. cd to `coincap` project
3. create a virtual environemnt `python -m venv venv`
4. activate the virtual environment
5. download dependecies `python -m pip install -r requirements.txt`
6. run the service `python ./main.py`
6. access the swagger in `http://localhost:8000/docs`

# How to Run (Docker)

1. clone the repository `git clone https://github.com/ihsanul14/coincap.git`
2. cd to `coincap` project
3. install docker (if not installed)
4. run `docker build -t coincap`
5. run the service `docker run -d --name coincap -p 8000:8000 coincap`
6. access the swagger in `http://localhost:8000/docs`

# Unit Testing
```
pytest --cov
```

# Vulnerability Checking
```
bandit -r . -x "./venv,./tests"
```