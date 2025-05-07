from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Supplier, Inventory

class InventoryViewsTest(TestCase):
    def setUp(self):
        # Create test data
        self.supplier = Supplier.objects.create(name='Test Supplier')
        self.inventory = Inventory.objects.create(
            name='Test Item',
            description='Test Description',
            note='Test Note',
            stock=10,
            availability=True,
            supplier=self.supplier
        )
        self.client = APIClient()

    def test_inventory_list_view(self):
        """Test the inventory list page returns 200 OK"""
        response = self.client.get(reverse('inventory_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/list.html')
        self.assertContains(response, 'Test Item')
        self.assertContains(response, 'Test Supplier')

    def test_inventory_detail_view(self):
        """Test the inventory detail page returns 200 OK"""
        response = self.client.get(reverse('inventory_detail', args=[self.inventory.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/detail.html')
        self.assertContains(response, 'Test Item')
        self.assertContains(response, 'Test Description')

    def test_inventory_api_list(self):
        """Test the inventory API list endpoint returns 200 OK"""
        response = self.client.get('/api/inventory/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['name'], 'Test Item')

    def test_inventory_api_detail(self):
        """Test the inventory API detail endpoint returns 200 OK"""
        response = self.client.get(f'/api/inventory/{self.inventory.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'Test Item')

    def test_inventory_api_filter(self):
        """Test the inventory API filtering by name"""
        # Create another inventory item
        Inventory.objects.create(
            name='Another Item',
            description='Another Description',
            note='Another Note',
            stock=5,
            availability=True,
            supplier=self.supplier
        )

        # Test filtering by name
        response = self.client.get('/api/inventory/?search=Test')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['name'], 'Test Item')

        # Test filtering with non-existent name
        response = self.client.get('/api/inventory/?search=Nonexistent')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 0)

    def test_invalid_inventory_detail(self):
        """Test accessing non-existent inventory detail returns 404"""
        response = self.client.get(reverse('inventory_detail', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_invalid_inventory_api_detail(self):
        """Test accessing non-existent inventory API detail returns 404"""
        response = self.client.get('/api/inventory/999/')
        self.assertEqual(response.status_code, 404)
