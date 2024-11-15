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
        print('ID: ', id)

        try:
            if str(id) == '0':
                for item in DrawingModel.objects.all():
                    item.prw.delete()
                    item.webp.delete()
                    item.pdf.delete()
                    item.delete()
            else:
                qs = DrawingModel.objects.get(id=id)
                qs.prw.delete()
                qs.webp.delete()
                qs.pdf.delete()
                qs.delete()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response(status=status.HTTP_200_OK)


    def post(self, request):
        """ Загрузка чертежей в очередь """

        try:
            # Не работает с загрузкой из формы django
            for pdf_file in request.FILES.getlist('files'):
                print(f"Поле: {pdf_file}, Имя файла: {pdf_file.name}, Размер: {pdf_file.size}")

                # Бросаем исключение если файл не PDF
                if pdf_file.name.split('.')[-1] != 'pdf':
                    print('Неверный формат файла')
                    return Response({"error": "Неверный формат файла"},status=status.HTTP_400_BAD_REQUEST)
                
                pages = convert_from_bytes(pdf_file.read())
                for i, page in enumerate(pages):
                    output_name = f"{str(pdf_file.name).replace('.pdf','')}{i + 1}" if i > 0 else f"{str(pdf_file.name).replace('.pdf','')}"

                    webp_buffer = BytesIO()
                    page.save(webp_buffer, format='WEBP')
                    webp_buffer.seek(0)

                    # Получаем width и height изображения
                    width, height = page.size

                    webp_file = InMemoryUploadedFile(
                        file=webp_buffer,
                        field_name=None,
                        name=f'{output_name}.webp',
                        content_type='image/webp',
                        size=sys.getsizeof(webp_buffer),
                        charset=None,
                    )

                    prw_buffer = BytesIO()
                    thumbnail = page.copy()
                    thumbnail.thumbnail((420, 420))
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
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)