import jwt
from auth.settings import JWT_SECRET
from rest_framework.exceptions import AuthenticationFailed

def ensure_logged_in(request):
    """
    Ensures that the request is authenticated and returns the payload
    of the decoded jwt token
    """
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('unable to find jwt token')

    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
    except jwt.PyJWTError as e:
        raise AuthenticationFailed(e.args[0])

    return payload
