from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from yaml import serialize
import rest_framework.permissions

from api.serializers import UserSerializer, GroupSerializer
from .serializers import ItemSerializer
from base.models import Item


@api_view(['GET'])
# @permission_classes((permissions.AllowAny,))
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    # Returns as JSON data
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    # Returns as JSON data
    return Response(serializer.data)


# ViewSets define the view behavior.

# Rather than write multiple views we're grouping together all the common 
# behavior into classes called ViewSets. We can easily break these down into 
# individual views if we need to, but using viewsets keeps the view logic 
# nicely organized as well as being very concise.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]