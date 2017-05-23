
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import CrystalSystem, Handpiece, MineralType, Photograph


class ViewTestCase(TestCase):
    """ Test suite for the api views"""

    def setUp(self):
        """ Define test client and other stuff"""

        self.client = APIClient()
        self.handpiece = Handpiece.objects.create(name="testhandpiece", current_location="nowhere")
        self.crystalsystem = CrystalSystem.objects.create(crystal_system="HG", temperature="90")
        self.photograph = Photograph.objects.create(handpiece=self.handpiece, online_status=True)
        self.mineraltype = MineralType.objects.create(trivial_name="testmineraltype", minerals="many minerals")

    def test_api_can_get_a_handpiece(self):
        """ test the api can get a Handpiece."""

        handpiece = Handpiece.objects.get()
        response = self.client.get(
            reverse('api:handpiece', kwargs={'pk': handpiece.id}),
            kwargs={'pk': handpiece.id},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, handpiece)

    def test_api_can_get_a_crystalsystem(self):
        """ test the api can get a crystalsystem."""

        crystalsystem = CrystalSystem.objects.get()
        response = self.client.get(
            reverse('api:crystalsystem', kwargs={'pk': crystalsystem.id}),
            kwargs={'pk': crystalsystem.id},
            format="json"

        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, crystalsystem)

    def test_api_can_get_a_photograph(self):
        """ test the api can get a photograph."""

        photograph = Photograph.objects.get()
        response = self.client.get(
            reverse('api:photograph', kwargs={'pk': photograph.id}),
            kwargs={'pk': photograph.id},
            format="json"

        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, photograph)

    def test_api_can_get_a_mineraltype(self):
        """ test the api can get a mineraltype."""

        mineraltype = MineralType.objects.get()
        response = self.client.get(
            reverse('api:mineraltype', kwargs={'pk': mineraltype.id}),
            kwargs={'pk': mineraltype.id},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, mineraltype)

# Create your tests here.
