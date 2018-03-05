from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Product

class ProductTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email    = 'test@email.com',
            password = 'password'
        )

        self.product = Product.objects.create(
            item     = 'Turbo Tax Software',
            quantity = 1,
        )

    def test_string_representation(self):
        product = Product(item='Toilet Paper')
        self.assertEqual(str(product), product.item)

    def test_product_content(self):
        self.assertEqual(f'{self.product.item}', 'Turbo Tax Software')
        self.assertEqual(f'{self.product.quantity}', '1')

    def test_product_list_view(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '1')
        self.assertTemplateUsed(response, 'product_list.html')

    def test_product_detail_view(self):
        response = self.client.get('product/1/')
        no_response = self.client.get('product/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Turbo Tax Software')
        self.assertTemplateUsed(response, 'product_detail.html')
