from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
import requests

class NextAuthTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return None
        
        token = auth_header.split(" ")[1]

        headers = {
            'Authorization': f'{token}',
            'Content-Type': 'application/json'
        }

        try:
            response = requests.post(
                'http://localhost:3000/api/auth/verify',
                headers=headers,
                json={'token': token},
            )
            if response.status_code != 200:
                raise AuthenticationFailed('Invalid token')
            
            user_data = response.json()
            print(user_data)
            return (user_data, None)
        except Exception as e:
            raise AuthenticationFailed(f'Token verification failed: {e}')