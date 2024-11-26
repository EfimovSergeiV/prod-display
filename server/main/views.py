import os

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.core.files.uploadedfile import InMemoryUploadedFile


class ControlView(APIView):
    """ Управление сервером """

    def get(self, request):
        os.system("sudo /usr/sbin/shutdown now")
        return Response(status=status.HTTP_200_OK)
