from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import views
from geomat.feedback.serializers import FeedBackSerializer
from django.core.mail import send_mail
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


class FeedBackView(generics.GenericAPIView):
    serializer_class = FeedBackSerializer

    permission_classes = ()

    @swagger_auto_schema(responses={200:"The Views response is 200 if mail is sent"})
    def post(self, request, *args, **kwargs):
        serializer = FeedBackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer = serializer.data

        message = send_mail(subject=serializer["emailTitle"],
                            from_email= "{0} <{1}>".format(serializer["username"],serializer["userEmail"]),
                            message=serializer["emailContent"],
                            recipient_list=["geomatdigital@dlist.uni-frankfurt.de"],
                            fail_silently=False)
        if not message:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(data=serializer)

# Create your views here.
