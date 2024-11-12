from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from draw.serializers import DrawingSerializer
from draw.models import DrawingModel




class DrawingView(APIView):

    def get(self, request):
        qs = DrawingModel.objects.all()
        serializer = DrawingSerializer(qs, many=True, context={'request': request})

        return Response(serializer.data)

    def post(self, request):
        # Handle the POST request

        serializer = DrawingSerializer(data=request.data)

        print('REQUEST DATA: ', request.data, request.FILES)

        if serializer.is_valid():
            serializer.save()
        #     return Response(serializer.data, status=201)

        return Response(status=status.HTTP_200_OK)