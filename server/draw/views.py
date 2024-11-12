from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from draw.serializers import DrawingSerializer
from draw.models import DrawingModel

from pdf2image import convert_from_path
from PIL import Image



from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image
from io import BytesIO
import sys


from django.core.files.uploadedfile import InMemoryUploadedFile

class DrawingView(APIView):
    """ Приём чертежей в очередь, отображение """

    serializer_class = DrawingSerializer

    def get(self, request):
        qs = DrawingModel.objects.all()
        serializer = self.serializer_class(qs, many=True, context={'request': request})

        return Response(serializer.data)
    

    def delete(self, request):
        """ Удаление по ID """
        id = request.data.get('id')

        if id:
            try:
                DrawingModel.objects.get(id=id).delete()
                return Response(status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)


    def post(self, request):
        # Handle the POST request
        # serializer = self.serializer_class(data=request.data)
        print(f'REQUEST DATA: {request.data} FILES: {request.FILES}', )
        # if serializer.is_valid():
        #     print('SERIALIZER DATA: ', serializer.validated_data)
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)

        # pages = convert_from_path(pdf_path)

        # for i, page in enumerate(pages):

        # Не работает с загрузкой из формы django
        for pdf_file in request.FILES.getlist('files'):
            print(f"Поле: {pdf_file}, Имя файла: {pdf_file.name}, Размер: {pdf_file.size}")
            
            pages = convert_from_bytes(pdf_file.read())
            for i, page in enumerate(pages):
            # Генерируем путь для сохранения каждого изображения
                output_name = f"{str(pdf_file.name).replace('.pdf','')}{i + 1}" if i > 0 else f"{str(pdf_file.name).replace('.pdf','')}"
                print(f"Сохранено: {output_name}.webp")

                webp_buffer = BytesIO()
                page.save(webp_buffer, format='WEBP')
                webp_buffer.seek(0)  # Возвращаем указатель в начало файла

                # Получаем width и height изображения
                width, height = page.size

                print(f"Размеры изображения: {width}x{height}")

                webp_file = InMemoryUploadedFile(
                    file=webp_buffer,
                    field_name=None,
                    name=f'{output_name}.webp',
                    content_type='image/webp',
                    size=sys.getsizeof(webp_buffer),
                    charset=None,
                )

                
                # Превью можно сделать, изменив размер изображения
                prw_buffer = BytesIO()
                thumbnail = page.copy()
                thumbnail.thumbnail((420, 420))  # Пример размера превью
                thumbnail.save(prw_buffer, format='WEBP')
                prw_buffer.seek(0)

                prw_file = InMemoryUploadedFile(
                    file=prw_buffer,
                    field_name=None,
                    name=f'{output_name}_preview.webp',
                    content_type='image/webp',
                    size=sys.getsizeof(prw_buffer),
                    charset=None,
                )

                
                # Подготовка данных для сериализатора
                data = {
                    'name': f'{output_name}', 
                    'status': 'queue', 
                    'link': None, 
                    'webp': webp_file,
                    'webp_size': {'width': width, 'height': height},
                    'prw': prw_file,
                    'pdf': pdf_file
                }



                serializer = self.serializer_class(data=data)
                if serializer.is_valid():
                    print('SERIALIZER DATA: ', serializer.validated_data)
                    serializer.save()
                else:
                    print('SERIALIZER ERRORS: ', serializer.errors)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)