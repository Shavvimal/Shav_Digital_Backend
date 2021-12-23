from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from contact.models import ContactPost
from contact.serializers import ContactPostSerializer

class ContactPostListView(ListAPIView):
    queryset = ContactPost.objects.order_by('-date_created')
    serializer_class = ContactPostSerializer
    lookup_field = 'name'
    permission_classes = (permissions.AllowAny, )

class ContactPostEndView(CreateAPIView):
    serializer_class = ContactPostSerializer
    queryset = ContactPost.objects.all()
    permission_classes = (permissions.AllowAny, )
