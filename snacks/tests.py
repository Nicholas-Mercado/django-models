from django.test import TestCase
from django.urls import reverse


class SnackTests(TestCase):
    
    def test_snack_list_status(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        

    def test_snack_list_templates_home(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')
        


