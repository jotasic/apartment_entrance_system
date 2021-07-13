from rest_framework        import viewsets, permissions, pagination

from api.doors.models      import DoorUseLog
from api.doors.serializers import DoorUseLogSerializer

class DoorAdminViewSet(viewsets.ModelViewSet):
    queryset           = DoorUseLog.objects.all()
    serializer_class   = DoorUseLogSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field       = 'door_number'
    pagination_class   = pagination.LimitOffsetPagination