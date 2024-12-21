from rest_framework.response import Response
from rest_framework import status
from functools import wraps
from .utils import verify_google_access_token

def google_auth_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return Response({'error': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        token = auth_header.split(' ')[1]

        idinfo = verify_google_access_token(token)
        if not idinfo:
            return Response({'error': 'Invalid or expired token.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        request.user_info = idinfo
        return func(request, *args, **kwargs)
    
    return wrapper