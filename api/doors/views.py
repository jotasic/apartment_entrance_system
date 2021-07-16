from django.http.response import Http404
from rest_framework          import status, serializers
from rest_framework.views    import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404 


from .serializers            import DoorUseLogSerializer, DoorSearchSerializer
from .models                 import DoorUseLog

class DoorSearchAPIView(APIView):
    def post(self, request):
        try:
            serializer = DoorSearchSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            obj = get_object_or_404(DoorUseLog, door_number=serializer.data['door_number'], 
                                                    password=serializer.data['password'])

            serializer = DoorUseLogSerializer(instance=obj, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except Http404:
            return Response({'message':'INVALID_INPUT'}, status=status.HTTP_401_UNAUTHORIZED)

        except serializers.ValidationError:
            return Response({'message':'INVALID_INPUT'}, status=status.HTTP_401_UNAUTHORIZED)