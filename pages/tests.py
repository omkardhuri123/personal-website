from django.test import SimpleTestCase

# Create your tests here.
class HomepagesTests(SimpleTestCase):
    def test_url_exits_at_correct_location(self):
       responce = self.client.get('/')
       self.assertEqual(responce.status_code,200)

class AboutpagesTests(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        responce = self.client.get('/about/')
        self.assertEqual(responce.status_code,200)