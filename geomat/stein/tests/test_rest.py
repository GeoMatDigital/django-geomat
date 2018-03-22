"""Tests for the REST framework"""
import json
import tempfile
from pprint import pprint

import pytest
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from geomat.stein.models import CrystalSystem, Handpiece, MineralType, Photograph, Cleavage
from geomat.stein.serializers import *


# Helper functions


def convert(input):
    if isinstance(input, dict):
        return {
            convert(key): convert(value)
            for key, value in list(input.items())
        }
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, str):
        return input.encode('utf-8')
    else:
        return input


class ApiViewTestCase(TestCase):
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

        image = tempfile.NamedTemporaryFile(suffix='.jpg').name
        self.photograph_one = Photograph.objects.create(
            handpiece=self.handpiece_one, image_file=image, online_status=True)
        # Second test photograph since we also test ListViews
        self.photograph_two = Photograph.objects.create(
            handpiece=self.handpiece_two, image_file=image, online_status=True)

        self.mineraltype_one = MineralType.objects.create(
            trivial_name="testmineraltype", minerals="many minerals")
        # Second test mineraltype since we also test ListViews
        self.mineraltype_two = MineralType.objects.create(
            trivial_name="testmineraltype two", minerals="many minerals two")

    def test_api_can_retrieve_handpiece_detail(self):
        """Test retrieval of a Handpiece object with the REST framework."""

        handpiece = Handpiece.objects.get(name="testhandpiece")
        response = self.client.get(
            reverse('api:handpiece-detail', kwargs={'pk': handpiece.id}),
            kwargs={'pk': handpiece.id},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(json.loads(response.content)['name'], "testhandpiece")
        self.assertEqual(
            json.loads(response.content)['current_location'], "nowhere")

    def test_api_return_404_on_missing_handpiece_detail(self):
        """Test that the API returns 404 when requesting a non-existing Handpiece object."""
        response = self.client.get(
            reverse('api:handpiece-detail', kwargs={'pk': 123}),
            kwargs={'pk': 123},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_can_retrieve_crystalsystem_detail(self):
        """Test retrieval of a CrystalSystem object with the REST framework."""

        crystalsystem = CrystalSystem.objects.get(crystal_system="HG")
        response = self.client.get(
            reverse('api:crystalsystem-detail', kwargs={'pk': crystalsystem.id}),
            kwargs={'pk': crystalsystem.id},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(json.loads(response.content)['crystal_system'], "HG")
        self.assertEqual(json.loads(response.content)['temperature'], 90)

    def test_api_return_404_on_missing_crystalsystem_detail(self):
        """Test that the API returns 404 when requesting a non-existing CrystalSystem object."""
        response = self.client.get(
            reverse('api:crystalsystem-detail', kwargs={'pk': 123}),
            kwargs={'pk': 123},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_can_retrieve_photograph_detail(self):
        """Test retrieval of a Photograph object with the REST framework."""

        handpiece = Handpiece.objects.get(name="testhandpiece")
        photograph = Photograph.objects.get(handpiece=handpiece)
        response = self.client.get(
            reverse('api:photograph-detail', kwargs={'pk': photograph.id}),
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
            reverse('api:photograph-detail', kwargs={'pk': 123}),
            kwargs={'pk': 123},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_can_retrieve_mineraltype_detail(self):
        """Test retrieval of a MineralType object with the REST framework."""

        mineraltype = MineralType.objects.get(trivial_name="testmineraltype")
        response = self.client.get(
            reverse('api:mineraltype-detail', kwargs={'pk': mineraltype.id}),
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
            reverse('api:mineraltype-detail', kwargs={'pk': 123}),
            kwargs={'pk': 123},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_can_retrieve_handpiece_list(self):
        """ Test retrieval of all Handpiece objects with the REST framework."""

        response = self.client.get(
            reverse('api:handpiece-list'), kwargs={}, format="json")
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response_data[0]['name'], "testhandpiece")
        self.assertEqual(response_data[0]['current_location'], "nowhere")
        self.assertEqual(response_data[1]['name'], "testhandpiece two")
        self.assertEqual(response_data[1]['current_location'], "nowhere two")

        pass

    def test_api_can_retrieve_crystalsystem_list(self):
        """ Test retrieval of all Crystalsystem objects with the REST framework."""
        response = self.client.get(
            reverse('api:crystalsystem-list'), kwargs={}, format="json")
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response_data[0]['crystal_system'], "HG")
        self.assertEqual(response_data[0]['temperature'], 90)
        self.assertEqual(response_data[1]['crystal_system'], "HT")
        self.assertEqual(response_data[1]['temperature'], 92)

    def test_api_can_retrieve_photograph_list(self):
        """ Test retrieval of all Photograph objects with the REST framework."""
        response = self.client.get(
            reverse('api:photograph-list'), kwargs={}, format="json")
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response_data[0]['handpiece']['name'],
                         "testhandpiece")
        self.assertEqual(response_data[0]['handpiece']['current_location'],
                         "nowhere")
        self.assertEqual(response_data[0]['online_status'], True)
        self.assertEqual(response_data[1]['handpiece']['name'],
                         "testhandpiece two")
        self.assertEqual(response_data[1]['handpiece']['current_location'],
                         "nowhere two")
        self.assertEqual(response_data[1]['online_status'], True)

    def test_api_can_retrieve_mineraltype_list(self):
        """ Test retrieval of all Mineraltype objects with the REST framework."""
        response = self.client.get(
            reverse('api:mineraltype-list'), kwargs={}, format="json")
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response_data[0]['trivial_name'], "testmineraltype")
        self.assertEqual(response_data[0]['minerals'], "many minerals")
        self.assertEqual(response_data[1]['trivial_name'],
                         "testmineraltype two")
        self.assertEqual(response_data[1]['minerals'], "many minerals two")


# Test Case wether the Views are GET only Views


class ApiForbiddenMethodTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.handpiece_one = Handpiece.objects.create(
            name="testhandpiece", current_location="nowhere")

        self.crystalsystem_one = CrystalSystem.objects.create(
            crystal_system="HG", temperature=90)

        self.photograph_one = Photograph.objects.create(
            handpiece=self.handpiece_one, online_status=True)

        self.mineraltype_one = MineralType.objects.create(
            trivial_name="testmineraltype", minerals="many minerals")

    # Check wether the Views accept POST method
    # We expect a 403 - Forbidden, since we want a GET only API

    def test_if_post_allowed_handpiece_detail(self):
        """Test if POST method is NOT allowed on handpiece detail view."""
        handpiece = Handpiece.objects.get(name="testhandpiece")
        response = self.client.post(
            reverse('api:handpiece-detail', kwargs={'pk': handpiece.id}),
            kwargs={'id': 300},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_post_allowed_crystalsystem_detail(self):
        """Test if POST method is NOT allowed on crystalsystem detail view."""
        crystalsystem = CrystalSystem.objects.get(crystal_system="HG")
        response = self.client.post(
            reverse('api:crystalsystem-detail', kwargs={'pk': crystalsystem.id}),
            kwargs={'id': 300},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_post_allowed_photograph_detail(self):
        """Test if POST method is NOT allowed on photograph detail view."""
        handpiece = Handpiece.objects.get(name="testhandpiece")
        photograph = Photograph.objects.get(handpiece=handpiece)
        response = self.client.post(
            reverse('api:photograph-detail', kwargs={'pk': photograph.id}),
            kwargs={'id': 300},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_post_allowed_mineraltype_detail(self):
        """Test if POST method is NOT allowed on mineraltype detail view."""

        mineraltype = MineralType.objects.get(trivial_name="testmineraltype")
        response = self.client.post(
            reverse('api:mineraltype-detail', kwargs={'pk': mineraltype.id}),
            kwargs={'id': 300},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Check wether the Views accept PUT method
    # We expect a 403 - Forbidden, since we want a GET only API

    def test_if_put_allowed_handpiece_detail(self):
        """Test if PUT method is NOT allowed on handpiece detail view."""
        handpiece = Handpiece.objects.get(name="testhandpiece")
        response = self.client.put(
            reverse('api:handpiece-detail', kwargs={'pk': handpiece.id}),
            kwargs={'id': 300},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_put_allowed_crystalsystem_detail(self):
        """Test if PUT method is NOT allowed on crystalsystem detail view."""
        crystalsystem = CrystalSystem.objects.get(crystal_system="HG")
        response = self.client.put(
            reverse('api:crystalsystem-detail', kwargs={'pk': crystalsystem.id}),
            kwargs={'id': 300},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_put_allowed_photograph_detail(self):
        """Test if PUT method is NOT allowed on photograph detail view."""
        handpiece = Handpiece.objects.get(name="testhandpiece")
        photograph = Photograph.objects.get(handpiece=handpiece)
        response = self.client.put(
            reverse('api:photograph-detail', kwargs={'pk': photograph.id}),
            kwargs={'id': 300},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_put_allowed_mineraltype_detail(self):
        """Test if PUT method is NOT allowed on mineraltype detail view."""

        mineraltype = MineralType.objects.get(trivial_name="testmineraltype")
        response = self.client.put(
            reverse('api:mineraltype-detail', kwargs={'pk': mineraltype.id}),
            kwargs={'id': 300},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Check wether the Views accept PATCH method
    # We expect a 403 - Forbidden, since we want a GET only API

    def test_if_patch_allowed_handpiece_detail(self):
        """Test if PATCH method is NOT allowed on handpiece detail view."""
        handpiece = Handpiece.objects.get(name="testhandpiece")
        response = self.client.patch(
            reverse('api:handpiece-detail', kwargs={'pk': handpiece.id}),
            kwargs={'id': 300},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_patch_allowed_crystalsystem_detail(self):
        """Test if PATCH method is NOT allowed on crystalsystem detail view."""
        crystalsystem = CrystalSystem.objects.get(crystal_system="HG")
        response = self.client.patch(
            reverse('api:crystalsystem-detail', kwargs={'pk': crystalsystem.id}),
            kwargs={'id': 300},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_patch_allowed_photograph_detail(self):
        """Test if PATCH method is NOT allowed on photograph detail view."""
        handpiece = Handpiece.objects.get(name="testhandpiece")
        photograph = Photograph.objects.get(handpiece=handpiece)
        response = self.client.patch(
            reverse('api:photograph-detail', kwargs={'pk': photograph.id}),
            kwargs={'id': 300},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_patch_allowed_mineraltype_detail(self):
        """Test if PATCH method is NOT allowed on mineraltype detail view."""

        mineraltype = MineralType.objects.get(trivial_name="testmineraltype")
        response = self.client.patch(
            reverse('api:mineraltype-detail', kwargs={'pk': mineraltype.id}),
            kwargs={'id': 300},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Check wether the Views accept DELETE method
    # We expect a 403 - Forbidden, since we want a GET only API

    def test_if_delete_allowed_handpiece_detail(self):
        """Test if DELETE method is NOT allowed on handpiece detail view."""
        handpiece = Handpiece.objects.get(name="testhandpiece")
        response = self.client.delete(
            reverse('api:handpiece-detail', kwargs={'pk': handpiece.id}),
            kwargs={'id': 300},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_delete_allowed_crystalsystem_detail(self):
        """Test if DELETE method is NOT allowed on crystalsystem detail view."""
        crystalsystem = CrystalSystem.objects.get(crystal_system="HG")
        response = self.client.delete(
            reverse('api:crystalsystem-detail', kwargs={'pk': crystalsystem.id}),
            kwargs={'id': 300},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_delete_allowed_photograph_detail(self):
        """Test if DELETE method is NOT allowed on photograph detail view."""
        handpiece = Handpiece.objects.get(name="testhandpiece")
        photograph = Photograph.objects.get(handpiece=handpiece)
        response = self.client.delete(
            reverse('api:photograph-detail', kwargs={'pk': photograph.id}),
            kwargs={'id': 300},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_delete_allowed_mineraltype_detail(self):
        """Test if DELETE method is NOT allowed on mineraltype detail view."""

        mineraltype = MineralType.objects.get(trivial_name="testmineraltype")
        response = self.client.delete(
            reverse('api:mineraltype-detail', kwargs={'pk': mineraltype.id}),
            kwargs={'id': 300},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)



class FilterApiViewTestCase(TestCase):
    maxDiff = None

    def setUp(self):
        # we need at least 2 objects of each  model to be sure that it actually filters

        self.client = APIClient()
        self.cleavage_one = Cleavage.objects.create(
            cleavage='PE'
        )
        self.mineraltype_one = MineralType.objects.create(
            trivial_name="testmineral one",
            systematics="HG",
            variety="many one",
            minerals="minerals one",
            mohs_scale="mohs one",
            density="hard one",
            streak="streak one",
            normal_color="color one",
            fracture=["HF"],
            lustre=["AM"],
            chemical_formula="CHEMONE",
            other="other one",
            resource_mindat="mindat one",
            resource_mineralienatlas="atlas one", )
        self.mineraltype_one.cleavage.set([self.cleavage_one])

        self.cleavage_two = Cleavage.objects.create(
            cleavage='DI'
        )
        self.mineraltype_two = MineralType.objects.create(
            trivial_name="testmineral two",
            systematics="HT",
            variety="many two",
            minerals="minerals two",
            mohs_scale="mohs two",
            density="hard two",
            streak="streak two",
            normal_color="color two",
            fracture=["CF"],
            lustre=["DL"],
            chemical_formula="CHEMTWO",
            other="other two",
            resource_mindat="mindat two",
            resource_mineralienatlas="atlas two")
        self.mineraltype_two.cleavage.set([self.cleavage_two])

        self.crystalsystem_one = CrystalSystem.objects.create(
            mineral_type=self.mineraltype_one,
            crystal_system="TC",
            temperature=90,
            pressure=80)
        self.crystalsystem_two = CrystalSystem.objects.create(
            mineral_type=self.mineraltype_two,
            crystal_system="OR",
            temperature=92,
            pressure=82)

        self.handpiece_one = Handpiece.objects.create(
            name="handpiece one",
            finding_place="nowhere one",
            current_location="here one",
            old_inventory_number="inven one")
        self.handpiece_one.mineral_type.set([self.mineraltype_one])
        self.handpiece_two = Handpiece.objects.create(
            name="handpiece two",
            finding_place="nowhere two",
            current_location="here two",
            old_inventory_number="inven two")
        self.handpiece_two.mineral_type.set([self.mineraltype_two])
        self.photograph_one = Photograph.objects.create(
            handpiece=self.handpiece_one,
            image_file="image_one.jpg",
            orientation="T",
            shot_type="MA")
        self.photograph_two = Photograph.objects.create(
            handpiece=self.handpiece_two,
            image_file="image_two.jpg",
            orientation="S",
            shot_type="MI")

        self.photograph_one_dict = PhotographSerializer(self.photograph_one).data

        self.photograph_two_dict = PhotographSerializer(self.photograph_two).data

        self.mineraltype_one_dict = MineralTypeSerializer(self.mineraltype_one).data

        self.mineraltype_two_dict = MineralTypeSerializer(self.mineraltype_two).data

        self.crystalsystem_one_dict = CrystalSystemFullSerializer(self.crystalsystem_one).data

        self.crystalsystem_two_dict = CrystalSystemFullSerializer(self.crystalsystem_two).data

        self.handpiece_one_dict = HandpieceSerializer(self.handpiece_one).data

        self.handpiece_two_dict = HandpieceSerializer(self.handpiece_two).data

    def test_can_filter_trivial_name(self):
        response = self.client.get(
            reverse('api:mineraltype-filter'),
            {'trivial_name': "testmineral one"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.mineraltype_one_dict in response_dict
        assert len(response_dict) == 1

    def test_can_filter_systematics(self):
        response = self.client.get(
            reverse('api:mineraltype-filter'), {'systematics': "HG"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.mineraltype_one_dict in response_dict
        assert len(response_dict) == 1

    def test_can_filter_variety(self):
        response = self.client.get(
            reverse('api:mineraltype-filter'), {'variety': "many one"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.mineraltype_one_dict in response_dict
        assert len(response_dict) == 1

    def test_can_filter_minerals(self):
        response = self.client.get(
            reverse('api:mineraltype-filter'), {'minerals': "minerals one"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.mineraltype_one_dict in response_dict
        assert len(response_dict) == 1

    def test_can_filter_mohs_scale(self):
        response = self.client.get(
            reverse('api:mineraltype-filter'), {'mohs_scale': "mohs one"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.mineraltype_one_dict in response_dict
        assert len(response_dict) == 1

    def test_can_filter_density(self):
        response = self.client.get(
            reverse('api:mineraltype-filter'), {'density': "hard one"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.mineraltype_one_dict in response_dict
        assert len(response_dict) == 1

    def test_can_filter_streak(self):
        response = self.client.get(
            reverse('api:mineraltype-filter'), {'streak': "streak one"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.mineraltype_one_dict in response_dict
        assert len(response_dict) == 1

    def test_can_filter_normal_color(self):
        response = self.client.get(
            reverse('api:mineraltype-filter'), {'normal_color': "color one"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.mineraltype_one_dict in response_dict
        assert len(response_dict) == 1

    def test_can_filter_fracture(self):
        response = self.client.get(
            reverse('api:mineraltype-filter'), {'fracture': str(["HF"])})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.mineraltype_one_dict in response_dict
        assert len(response_dict) == 1

    def test_can_filter_cleavage(self):
        response = self.client.get(
            reverse('api:mineraltype-filter'), {'cleavage': self.cleavage_one.pk})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.mineraltype_one_dict in response_dict
        assert len(response_dict) == 1

    def test_can_filter_lustre(self):
        response = self.client.get(
            reverse('api:mineraltype-filter'), {'lustre': str(["AM"])})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.mineraltype_one_dict in response_dict
        assert len(response_dict) == 1

    def test_can_filter_chemical_formula(self):
        response = self.client.get(
            reverse('api:mineraltype-filter'), {'chemical_formula': "CHEMONE"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response_dict)
        print((self.mineraltype_one_dict))
        assert self.mineraltype_one_dict in response_dict
        assert len(response_dict) == 1

    def test_can_filter_other(self):
        response = self.client.get(
            reverse('api:mineraltype-filter'), {'other': "other one"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.mineraltype_one_dict in response_dict
        assert len(response_dict) == 1

    def test_can_filter_resource_mindat(self):
        response = self.client.get(
            reverse('api:mineraltype-filter'),
            {'resource_mindat': "mindat one"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.mineraltype_one_dict in response_dict
        assert len(response_dict) == 1

    def test_can_filter_resource_mineralienatlas(self):
        response = self.client.get(
            reverse('api:mineraltype-filter'),
            {'resource_mineralienatlas': "atlas one"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.mineraltype_one_dict in response_dict
        assert len(response_dict) == 1

    # Several tests wether Filter Crystalsystem View can filter all needed fields

    def test_can_filter_mineraltype(self):
        response = self.client.get(
            reverse('api:crystalsystem-filter'),
            {'mineral_type': self.mineraltype_one.pk})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.crystalsystem_one_dict in response_dict
        assert len(response_dict) == 1

    def test_can_filter_crystal_system(self):
        response = self.client.get(
            reverse('api:crystalsystem-filter'), {'crystal_system': "TC"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.crystalsystem_one_dict in response_dict
        assert len(response_dict) == 1

    def test_can_filter_temperature(self):
        response = self.client.get(
            reverse('api:crystalsystem-filter'), {'temperature': 90})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.crystalsystem_one_dict in response_dict
        assert len(response_dict) == 1

    def test_can_filter_pressure(self):
        response = self.client.get(
            reverse('api:crystalsystem-filter'), {'pressure': 80})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.crystalsystem_one_dict in response_dict
        assert len(response_dict) == 1

    # Several tests wether Filter Handpiece View can filter all needed fields

    def test_can_filter_name(self):
        response = self.client.get(
            reverse('api:handpiece-filter'), {'name': "handpiece one"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.handpiece_one_dict in response_dict
        assert len(response_dict) == 1

    def test_can_filter_mineral_type(self):
        response = self.client.get(
            reverse('api:handpiece-filter'),
            {'mineral_type': self.mineraltype_one.pk})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.handpiece_one_dict in response_dict
        assert len(response_dict) == 1

    def test_can_filter_finding_place(self):
        response = self.client.get(
            reverse('api:handpiece-filter'), {'finding_place': "nowhere one"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.handpiece_one_dict in response_dict
        assert len(response_dict) == 1

    def test_can_filter_current_location(self):
        response = self.client.get(
            reverse('api:handpiece-filter'), {'current_location': "here one"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.handpiece_one_dict in response_dict
        assert len(response_dict) == 1

    def test_can_filter_old_inventory_number(self):
        response = self.client.get(
            reverse('api:handpiece-filter'),
            {'old_inventory_number': "inven one"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.handpiece_one_dict in response_dict
        assert len(response_dict) == 1

    # Several tests wether Filter Photograph View can filter all needed fields
    @pytest.mark.skip(
        reason=
        "The given output of the StdImageField, contains full server url of the image files. The dict does NOT contain them, to besolved in future process"
    )
    def test_can_filter_image_file(self):
        response = self.client.get(
            reverse('api:photograph-filter'), {'image_file': "image_one.jpg"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.photograph_one_dict in response_dict
        assert len(response_dict) == 1

    @pytest.mark.skip(
        reason=
        "The given output of the StdImageField, contains full server url of the image files. The dict does NOT contain them, to besolved in future process"
    )
    def test_can_filter_old_handpiece(self):
        response = self.client.get(
            reverse('api:photograph-filter'),
            {'handpiece': self.handpiece_one.id})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.photograph_one_dict in response_dict
        assert len(response_dict) == 1

    @pytest.mark.skip(
        reason=
        "The given output of the StdImageField, contains full server url of the image files.The dict does NOT contain them, to besolved in future process"
    )
    def test_can_filter_orientation(self):
        response = self.client.get(
            reverse('api:photograph-filter'), {'orientation': "T"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.photograph_one_dict in response_dict
        assert len(response_dict) == 1

    @pytest.mark.skip(
        reason=
        "The given output of the StdImageField, contains full server url of the image files. The dict does NOT contain them, to besolved in future process"
    )
    def test_can_filter_shot_type(self):
        response = self.client.get(
            reverse('api:photograph-filter'), {'shot_type': "MA"})
        response_dict = json.loads(response.content)
        pprint(response_dict)
        pprint(self.photograph_one_dict)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert self.photograph_one_dict in response_dict
        assert len(response_dict) == 1
