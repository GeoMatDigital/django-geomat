from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import views
from geomat.feedback.serializers import FeedBackSerializer
from django.core.mail import send_mail
from rest_framework import status


class FeedBackView(views.APIView):
    serializer_class = FeedBackSerializer

    permission_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = FeedBackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer = serializer.data

        send_mail(subject=serializer["emailTitle"], from_email=serializer["userEmail"], message=serializer["emailContent"],
                  recipient_list=["christian@elearning.physik.uni-frankfurt.de"], fail_silently=False)

        return Response()

# Create your views here.