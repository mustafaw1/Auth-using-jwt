# Auth API using JWT

You can install the project using pipenv by running `pipenv install`. You must have python3.10 installed to run this project. Alternatively you can
install all the dependencies using `pip install -r requirements.txt`. It's advisable to use PostMan to test the api or a http cli client like `httpie` that will print both the request and response headers. You can also use our postman collection (postman-auth-collection.json) in this repo that we used to our client.

Steps to test auth-api
## Running the server
You can run the server using `python manage.py runserver`

## Registering a new user
Register a new user by sending a POST request to http://127.0.0.1:8000/api/register
```json
{
   "name" : "abc",
   "email": "someone@gmail.com",
   "password": "124"
}
```

You should get a response for a newly created user.
```json
{
    "id": 4,
    "name": "abc",
    "email": "someone@gmail.com"
}
```

## Logging in
Send a POST request to http://127.0.0.1:8000/api/login to login as a user

```json
{
    "email": "someone@gmail.com",
    "password": "124"
}
```
You should see the JWT token being set in the response headers.

## Running an autheticated request
Send a GET request http://127.0.0.1:8000/api/user to fetch the details of the current logged in user. You should get a valid response like.
```json
{
    "id": 4,
    "name": "abc",
    "email": "someone@gmail.com"
}
```
