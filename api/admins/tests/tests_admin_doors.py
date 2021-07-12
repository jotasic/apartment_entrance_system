from rest_framework                  import status
from rest_framework.test             import APITestCase
from django.contrib.auth.models      import User
from rest_framework.authtoken.models import Token

from api.doors.models                import DoorUseLog

class AdminDoorTestCase(APITestCase):
    def setUp(self):
        self.user  = User.objects.create(username='admin', password='some-strong-password')
        self.token = Token.objects.create(user=self.user)
        DoorUseLog.objects.create(id=1, door_number='1201', password='1004', fee=100)
        self.api_authentication()
        
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_door_list_authenticated(self):
        response = self.client.get('/api/admin/doors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [{'door_number':'1201', 'password':'1004', 'fee':100}])
    
    def test_door_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/admin/doors/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)