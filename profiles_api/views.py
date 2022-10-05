from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete',
            'que onda perro',
            'soy una response',
            'jejeje'
        ]
        return Response({'message' : 'Hello!', 'an_anpiview' : an_apiview})


