from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from inventory_app.models import Inventory, Supplier


class InventoryViewTests(TestCase):

    def setUp(self):
        self.supplier = Supplier.objects.create(
            name='HP'
        )
        self.inventory = Inventory.objects.create(
            name='laptop',
            description='laptop',
            note='laptop',
            stock=3,
            availability=True,
            supplier=self.supplier
        )

    def test_url_exists(self):
        response = self.client.get("/inventory")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('inventory'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('inventory'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory_app/inventory_list.html')

    def test_has_an_object_list(self):
        response = self.client.get(reverse('inventory'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'inventory_app/inventory_list.html')


class InventoryDetailViewTests(TestCase):

    def setUp(self):
        self.supplier = Supplier.objects.create(
            name='HP'
        )
        self.inventory = Inventory.objects.create(
            name='laptop',
            description='laptop',
            note='laptop',
            stock=3,
            availability=True,
            supplier=self.supplier
        )

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('inventory_detail', kwargs={'pk': self.inventory.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory_app/inventory_detail.html')

    def test_has_an_object(self):
        response = self.client.get(reverse('inventory_detail', kwargs={'pk': self.inventory.id}))
        self.assertEqual(response.status_code, 200)


class InventoryAPIViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.supplier = Supplier.objects.create(
            name='HP'
        )
        self.inventory = []
        self.inventory.append(Inventory.objects.create(name='laptop', description='laptop', note='laptop', stock=3,
                                                       availability=True, supplier=self.supplier))
        self.inventory.append(Inventory.objects.create(name='laptop 1', description='laptop', note='laptop', stock=3,
                                                       availability=True, supplier=self.supplier))

    def test_inventory_api(self):
        url = reverse('inventory_api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        inventory_expected_list = self.inventory
        inventory_result_list = response.data['result']
        self.assertEqual(len(inventory_result_list), len(inventory_expected_list))

        for i in range(len(inventory_expected_list)):
            inventory_exp = inventory_expected_list[i]
            inventory_res = inventory_result_list[i]

            self.assertEqual(inventory_exp.name, inventory_res['name'])
            self.assertEqual(inventory_exp.availability, inventory_res['availability'])
            self.assertEqual(inventory_exp.supplier.name, inventory_res['supplier'])
