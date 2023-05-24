from rest_framework import (
    viewsets,
    mixins
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework.exceptions import PermissionDenied

from core.models import (
    Recipe,
    Tag,
    Ingredient
)
from recipe import serializers

class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs"""
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # if self.request.user.is_authenticated:
        return self.queryset.filter(user=self.request.user).order_by('-id')
        # else:
        #     raise PermissionDenied(
        #         detail='Authentication credentials were not provided.'
        #     )
            
    def get_serializer_class(self):
        """Return the serializer class for request"""
        if self.action == 'list':
            return serializers.RecipeSerializer
        return self.serializer_class
    
    def perform_create(self, serializer):
        """Create a new recipe"""
        serializer.save(user=self.request.user)
    
class TagViewSet(mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin, 
                 mixins.ListModelMixin, 
                 viewsets.GenericViewSet):
    """Manage Tags in Database"""
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Filter queryset by authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-name')
    
class IngredientViewSet(mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin, 
                        viewsets.GenericViewSet):
    """Manage Ingredients in Database"""
    serializer_class = serializers.IngredientSerializer
    queryset = Ingredient.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Filter queryset by authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-name')