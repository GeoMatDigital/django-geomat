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
        self.handpiece = Handpiece(name="testhandpiece",current_location="nowhere")
        self.crystalsystem = CrystalSystem(crystal_system="testsystem",temperature="9000")
        self.photograph = Photograph(handpiece=self.handpiece, online_status=True)
        self.mineraltype = MineralType(trivial_name="testmineraltype", minerals="many minerals")

    def test_api_can_get_a_handpiece(self):
        """ test the api can get a Handpiece."""

        handpiece = Handpiece.objects.get()
        response = self.client.get(
            reverse('handpiece'),
            kwargs={'pk': handpiece.id},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, handpiece)

    def test_api_can_get_a_crystalsystem(self):
        """ test the api can get a crystalsystem."""

        crstalsystem = CrystalSystem.objects.get()
        response = self.client.get(
            reverse('crystalsystem'),
            kwargs={'pk': crstalsystem.id},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, crstalsystem)

    def test_api_can_get_a_Photograph(self):
        """ test the api can get a photograph."""

        photograph = Photograph.onjects.get()
        response = self.client.get(
            reverse('photograph'),
            kwargs={'pk': photograph.id},
            format="json"
        )
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertContains(response, photograph)

    def test_api_can_get_a_mineraltype(self):
        """ test the api can get a mineraltype."""

        mieraltype = MineralType.objects.get()
        response = self.client.get(
            reverse('mineraltype'),
            kwargs={'pk': mieraltype.id},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, mieraltype)

# Create your tests here.
