from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from lawyers.models import Lawyers
from lawyers.serializers import LawyerSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from .permissions import IsOwnerOrManager
from rest_framework.permissions import IsAuthenticated


User = get_user_model()


@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = LawyerSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            # Save lawyer instance
            user=serializer.save()

            # Generate and save token
            token = Token.objects.create(user=user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        # Check if fields are empty
        if not username and not password:
            return Response({'detail': 'Email and Password fields cannot be empty'}, status=status.HTTP_403_FORBIDDEN)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': 'Lawyer not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Check if the password is correct
        if not user.check_password(password):
            return Response(
                {'detail': 'Credentials do not match.'}
            )
        
        token, created = Token.objects.get_or_create(user=user)
        serializer = LawyerSerializer(instance=user)
        return Response({'token': token.key, 'user': serializer.data})
        
    
class LawyerListView(generics.ListAPIView):
    queryset = Lawyers.objects.all()
    serializer_class = LawyerSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrManager]