from rest_framework          import status, serializers
from rest_framework.views    import APIView
from rest_framework.response import Response

from .serializers            import DoorUseLogSerializer, DoorSearchSerializer
from .models                 import DoorUseLog

class DoorSearchAPIView(APIView):
    def post(self, request):
        try:
            serializer = DoorSearchSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            door_use_log = DoorUseLog.objects.get(door_number=serializer.data['door_number'], 
                                                    password=serializer.data['password'])
            serializer = DoorUseLogSerializer(instance=door_use_log, many=False)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except DoorUseLog.DoesNotExist:
            return Response({'message':'INVALID_INPUT'}, status=status.HTTP_400_BAD_REQUEST)

        except serializers.ValidationError:
            return Response({'message':'INVALID_INPUT'}, status=status.HTTP_400_BAD_REQUEST)