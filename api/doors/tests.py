import json

from rest_framework                  import status
from rest_framework.test             import APITestCase

from api.doors.models                import DoorUseLog

class AdminDoorTestCase(APITestCase):
    def setUp(self):
        DoorUseLog.objects.create(id=1, door_number='1201', password='1004', fee=100)

    def test_search_fee_success(self):
        data     = {'door_number' : '1201', 'password' : '1004'}

        response = self.client.post('/api/public/door',
                                    data=json.dumps(data),
                                    content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
                                'door_number' : '1201', 'password' : '1004', 
                                'fee': 100
                        })
    
    def test_search_fee_failed(self):
        data     = {'door_number':'1201', 'password':'1111'}

        response = self.client.post('/api/public/door', 
                                    data=json.dumps(data), 
                                    content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)