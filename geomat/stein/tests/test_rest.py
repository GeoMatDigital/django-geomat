"""Tests for the REST framework"""
import json

from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from geomat.stein.models import CrystalSystem, Handpiece, MineralType, Photograph


class ViewTestCase(TestCase):
    """Test suite for the REST API views."""

    def setUp(self):
        """Define test client and set up default objects."""

        self.client = APIClient()

        self.handpiece_one = Handpiece.objects.create(
            name="testhandpiece", current_location="nowhere")
        # Second test handpiece since we also test ListViews
        self.handpiece_two = Handpiece.objects.create(
            name="testhandpiece two", current_location="nowhere two")

        self.crystalsystem_one = CrystalSystem.objects.create(
            crystal_system="HG", temperature=90)
        # Second test crystaalsystem since we also test ListViews
        self.crystalsystem_two = CrystalSystem.objects.create(
            crystal_system="HT", temperature=92)

        self.photograph_one = Photograph.objects.create(
            handpiece=self.handpiece_one, online_status=True)
        # Second test photograph since we also test ListViews
        self.photograph_two = Photograph.objects.create(
            handpiece=self.handpiece_two, online_status=True)

        self.mineraltype_one = MineralType.objects.create(
            trivial_name="testmineraltype", minerals="many minerals")
        # Second test mineraltype since we also test ListViews
        self.mineraltype_two = MineralType.objects.create(
            trivial_name="testmineraltype two", minerals="many minerals two")

    def test_api_can_retrieve_handpiece_detail(self):
        """Test retrieval of a Handpiece object with the REST framework."""

        handpiece = Handpiece.objects.get(name="testhandpiece")
        response = self.client.get(
            reverse('api:handpiece', kwargs={'pk': handpiece.id}),
            kwargs={'pk': handpiece.id},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(json.loads(response.content)['name'], "testhandpiece")
        self.assertEqual(
            json.loads(response.content)['current_location'], "nowhere")

    def test_api_return_404_on_missing_handpiece_detail(self):
        """Test that the API returns 404 when requesting a non-existing Handpiece object."""
        response = self.client.get(
            reverse('api:handpiece', kwargs={'pk': 123}),
            kwargs={'pk': 123},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_can_retrieve_crystalsystem_detail(self):
        """Test retrieval of a CrystalSystem object with the REST framework."""

        crystalsystem = CrystalSystem.objects.get(crystal_system="HG")
        response = self.client.get(
            reverse('api:crystalsystem', kwargs={'pk': crystalsystem.id}),
            kwargs={'pk': crystalsystem.id},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(json.loads(response.content)['crystal_system'], "HG")
        self.assertEqual(json.loads(response.content)['temperature'], 90)

    def test_api_return_404_on_missing_crystalsystem_detail(self):
        """Test that the API returns 404 when requesting a non-existing CrystalSystem object."""
        response = self.client.get(
            reverse('api:crystalsystem', kwargs={'pk': 123}),
            kwargs={'pk': 123},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_can_retrieve_photograph_detail(self):
        """Test retrieval of a Photograph object with the REST framework."""

        handpiece = Handpiece.objects.get(name="testhandpiece")
        photograph = Photograph.objects.get(handpiece=handpiece)
        response = self.client.get(
            reverse('api:photograph', kwargs={'pk': photograph.id}),
            kwargs={'pk': photograph.id},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            json.loads(response.content)['handpiece']['name'], "testhandpiece")
        self.assertEqual(
            json.loads(response.content)['handpiece']['current_location'],
            "nowhere")
        self.assertEqual(json.loads(response.content)['online_status'], True)

    def test_api_return_404_on_missing_photograph_detail(self):
        """Test that the API returns 404 when requesting a non-existing Photograph object."""
        response = self.client.get(
            reverse('api:photograph', kwargs={'pk': 123}),
            kwargs={'pk': 123},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_can_retrieve_mineraltype_detail(self):
        """Test retrieval of a MineralType object with the REST framework."""

        mineraltype = MineralType.objects.get(trivial_name="testmineraltype")
        response = self.client.get(
            reverse('api:mineraltype', kwargs={'pk': mineraltype.id}),
            kwargs={'pk': mineraltype.id},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json.loads(response.content)['trivial_name'], "testmineraltype")
        self.assertEqual(
            json.loads(response.content)['minerals'], "many minerals")

    def test_api_return_404_on_missing_mineraltype_detail(self):
        """Test that the API returns 404 when requesting a non-existing mineraltype object."""
        response = self.client.get(
            reverse('api:mineraltype', kwargs={'pk': 123}),
            kwargs={'pk': 123},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_can_retrieve_handpiece_list(self):
        """ Test retrieval of all Handpiece objects with the REST framework."""
        pass

    def test_api_can_retrieve_crystalsystem_list(self):
        """ Test retrieval of all Crystalsystem objects with the REST framework."""
        pass

    def test_api_can_retrieve_photograph_list(self):
        """ Test retrieval of all Photograph objects with the REST framework."""
        pass

    def test_api_can_retrieve_mineraltype_list(self):
        """ Test retrieval of all Mineraltype objects with the REST framework."""
        pass
