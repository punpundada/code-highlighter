from rest_framework import generics ,permissions , renderers
from . import models
from . import serializers
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

class SnippetListView(generics.ListCreateAPIView):
    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetsSerializers
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class snippetDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetsSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetailsView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


@api_view(["GET"])
def api_root(request,format=None):
    return Response({
        "users":reverse("user_list",request=request,format=format),
        "snippets":reverse("Snippets_list",request=request,format=format)
    })

class SnippetHighlighted(generics.GenericAPIView):
    queryset = models.Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)
    def get(self,request,*args,**kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)