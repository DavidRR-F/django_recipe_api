from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from core.models import Recipe
from recipe import serializers

class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs"""
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permissions_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.filter(user=self.request.user).order_by('-id')
        else:
            raise PermissionDenied(detail='Authentication credentials were not provided.')
    
    
