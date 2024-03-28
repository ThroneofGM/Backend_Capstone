from django.test import TestCase, Client
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User

class MenuViewTest(TestCase):

    def setUp(self):
        self.menu_1 = Menu.objects.create(id=11,title="IceCream", price=80, inventory=20)
        self.menu_2 = Menu.objects.create(id=12,title="Rolls", price=20, inventory=10)
    
   
    def test_getall(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.client.force_login(user)
        response = self.client.get("http://127.0.0.1:8000/restaurant/menu/")
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many = True)
        self.assertEqual(response.status_code, 200)  # Check the status code
        self.assertEqual(response.data, serializer.data) 