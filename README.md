# Auth-using-jwt

Steps to test auth-api

1.First of all run the server using python manage.py runserver

2.Go to url http://127.0.0.1:8000/api/register and register by adding your credentials for example:
```json
{
   "name" : "abc",
   "email": "someone@gmail.com",
   "password": "124"
}
```
and send a **POST** request.

3.Now go to url http://127.0.0.1:8000/api/login to login as a user.

4.Got to url http://127.0.0.1:8000/api/user to get the user that is currently login.

5.Go to url http://127.0.0.1:8000/api/logout to logout from the current session
