from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


from .serializers import RegisterSerializer

@api_view(['POST'])
def register_user(request):
    serializer=RegisterSerializer(
        data=request.data
    )

    if serializer.is_valid():

        serializer.save()

        return Response({
            'message:User registered successfully'
        })
    return Response(serializer.errors)

@api_view(['GET'])
@permission_classes([IsAuthenticated])

def profile(request):
    return Response({
        'username':request.user.username,
        'email':request.user.email
    })


# Create your views here.
