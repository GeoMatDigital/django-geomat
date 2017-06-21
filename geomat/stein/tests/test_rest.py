"""Tests for the REST framework"""
import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from geomat.stein.models import CrystalSystem, Handpiece, MineralType, Photograph


# Helper functions


def convert(input):
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
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

        response = self.client.get(reverse('api:handpiece-list'), kwargs={}, format="json")
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response_data[0]['name'], "testhandpiece")
        self.assertEqual(response_data[0]['current_location'], "nowhere")
        self.assertEqual(response_data[1]['name'], "testhandpiece two")
        self.assertEqual(response_data[1]['current_location'], "nowhere two")

        pass

    def test_api_can_retrieve_crystalsystem_list(self):
        """ Test retrieval of all Crystalsystem objects with the REST framework."""
        response = self.client.get(reverse('api:crystalsystem-list'), kwargs={}, format="json")
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response_data[0]['crystal_system'], "HG")
        self.assertEqual(response_data[0]['temperature'], 90)
        self.assertEqual(response_data[1]['crystal_system'], "HT")
        self.assertEqual(response_data[1]['temperature'], 92)

    def test_api_can_retrieve_photograph_list(self):
        """ Test retrieval of all Photograph objects with the REST framework."""
        response = self.client.get(reverse('api:photograph-list'), kwargs={}, format="json")
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response_data[0]['handpiece']['name'], "testhandpiece")
        self.assertEqual(response_data[0]['handpiece']['current_location'], "nowhere")
        self.assertEqual(response_data[0]['online_status'], True)
        self.assertEqual(response_data[1]['handpiece']['name'], "testhandpiece two")
        self.assertEqual(response_data[1]['handpiece']['current_location'], "nowhere two")
        self.assertEqual(response_data[1]['online_status'], True)

    def test_api_can_retrieve_mineraltype_list(self):
        """ Test retrieval of all Mineraltype objects with the REST framework."""
        response = self.client.get(reverse('api:mineraltype-list'), kwargs={}, format="json")
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response_data[0]['trivial_name'], "testmineraltype")
        self.assertEqual(response_data[0]['minerals'], "many minerals")
        self.assertEqual(response_data[1]['trivial_name'], "testmineraltype two")
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
        response = self.client.post(reverse('api:handpiece', kwargs={'pk': handpiece.id})
                                    , kwargs={'id': 300}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_post_allowed_crystalsystem_detail(self):
        """Test if POST method is NOT allowed on crystalsystem detail view."""
        crystalsystem = CrystalSystem.objects.get(crystal_system="HG")
        response = self.client.post(reverse('api:crystalsystem', kwargs={'pk': crystalsystem.id})
                                    , kwargs={'id': 300}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_post_allowed_photograph_detail(self):
        """Test if POST method is NOT allowed on photograph detail view."""
        handpiece = Handpiece.objects.get(name="testhandpiece")
        photograph = Photograph.objects.get(handpiece=handpiece)
        response = self.client.post(reverse('api:photograph', kwargs={'pk': photograph.id})
                                    , kwargs={'id': 300}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_post_allowed_mineraltype_detail(self):
        """Test if POST method is NOT allowed on mineraltype detail view."""

        mineraltype = MineralType.objects.get(trivial_name="testmineraltype")
        response = self.client.post(reverse('api:mineraltype', kwargs={'pk': mineraltype.id})
                                    , kwargs={'id': 300}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Check wether the Views accept PUT method
    # We expect a 403 - Forbidden, since we want a GET only API

    def test_if_put_allowed_handpiece_detail(self):
        """Test if PUT method is NOT allowed on handpiece detail view."""
        handpiece = Handpiece.objects.get(name="testhandpiece")
        response = self.client.put(reverse('api:handpiece', kwargs={'pk': handpiece.id})
                                   , kwargs={'id': 300}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_put_allowed_crystalsystem_detail(self):
        """Test if PUT method is NOT allowed on crystalsystem detail view."""
        crystalsystem = CrystalSystem.objects.get(crystal_system="HG")
        response = self.client.put(reverse('api:crystalsystem', kwargs={'pk': crystalsystem.id})
                                   , kwargs={'id': 300}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_put_allowed_photograph_detail(self):
        """Test if PUT method is NOT allowed on photograph detail view."""
        handpiece = Handpiece.objects.get(name="testhandpiece")
        photograph = Photograph.objects.get(handpiece=handpiece)
        response = self.client.put(reverse('api:photograph', kwargs={'pk': photograph.id})
                                   , kwargs={'id': 300}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_put_allowed_mineraltype_detail(self):
        """Test if PUT method is NOT allowed on mineraltype detail view."""

        mineraltype = MineralType.objects.get(trivial_name="testmineraltype")
        response = self.client.put(reverse('api:mineraltype', kwargs={'pk': mineraltype.id})
                                   , kwargs={'id': 300}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Check wether the Views accept PATCH method
    # We expect a 403 - Forbidden, since we want a GET only API

    def test_if_patch_allowed_handpiece_detail(self):
        """Test if PATCH method is NOT allowed on handpiece detail view."""
        handpiece = Handpiece.objects.get(name="testhandpiece")
        response = self.client.patch(reverse('api:handpiece', kwargs={'pk': handpiece.id})
                                     , kwargs={'id': 300}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_patch_allowed_crystalsystem_detail(self):
        """Test if PATCH method is NOT allowed on crystalsystem detail view."""
        crystalsystem = CrystalSystem.objects.get(crystal_system="HG")
        response = self.client.patch(reverse('api:crystalsystem', kwargs={'pk': crystalsystem.id})
                                     , kwargs={'id': 300}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_patch_allowed_photograph_detail(self):
        """Test if PATCH method is NOT allowed on photograph detail view."""
        handpiece = Handpiece.objects.get(name="testhandpiece")
        photograph = Photograph.objects.get(handpiece=handpiece)
        response = self.client.patch(reverse('api:photograph', kwargs={'pk': photograph.id})
                                     , kwargs={'id': 300}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_patch_allowed_mineraltype_detail(self):
        """Test if PATCH method is NOT allowed on mineraltype detail view."""

        mineraltype = MineralType.objects.get(trivial_name="testmineraltype")
        response = self.client.patch(reverse('api:mineraltype', kwargs={'pk': mineraltype.id})
                                     , kwargs={'id': 300}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Check wether the Views accept DELETE method
    # We expect a 403 - Forbidden, since we want a GET only API

    def test_if_delete_allowed_handpiece_detail(self):
        """Test if DELETE method is NOT allowed on handpiece detail view."""
        handpiece = Handpiece.objects.get(name="testhandpiece")
        response = self.client.delete(reverse('api:handpiece', kwargs={'pk': handpiece.id})
                                      , kwargs={'id': 300}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_delete_allowed_crystalsystem_detail(self):
        """Test if DELETE method is NOT allowed on crystalsystem detail view."""
        crystalsystem = CrystalSystem.objects.get(crystal_system="HG")
        response = self.client.delete(reverse('api:crystalsystem', kwargs={'pk': crystalsystem.id})
                                      , kwargs={'id': 300}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_delete_allowed_photograph_detail(self):
        """Test if DELETE method is NOT allowed on photograph detail view."""
        handpiece = Handpiece.objects.get(name="testhandpiece")
        photograph = Photograph.objects.get(handpiece=handpiece)
        response = self.client.delete(reverse('api:photograph', kwargs={'pk': photograph.id})
                                      , kwargs={'id': 300}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_delete_allowed_mineraltype_detail(self):
        """Test if DELETE method is NOT allowed on mineraltype detail view."""

        mineraltype = MineralType.objects.get(trivial_name="testmineraltype")
        response = self.client.delete(reverse('api:mineraltype', kwargs={'pk': mineraltype.id})
                                      , kwargs={'id': 300}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class FilterApiViewTestCase(TestCase):
    maxDiff = None

    def setUp(self):
        # we need at least 2 objects of each  model to be sure that it actually filters

        self.client = APIClient()
        self.mineraltype_one = MineralType.objects.create(trivial_name="testmineral one", systematics="HG",
                                                          variety="many one", minerals="minerals one",
                                                          mohs_scale="mohs one", density="hard one",
                                                          streak="streak one", normal_color="color one",
                                                          fracture=["HF"], cleavage=["PE"], lustre=["AM"],
                                                          chemical_formula="CHEMONE", other="other one",
                                                          resource_mindat="mindat one",
                                                          resource_mineralienatlas="atlas one")
        self.mineraltype_one_dict = {'trivial_name': "testmineral one", 'systematics': "HG",
                                     'variety': "many one", 'minerals': "minerals one",
                                     'mohs_scale': "mohs one", 'density': "hard one",
                                     'streak': "streak one", 'normal_color': "color one",
                                     'fracture': ["HF"], 'cleavage': ["PE"], 'lustre': ["AM"],
                                     'chemical_formula': "CHEMONE", 'other': "other one",
                                     'resource_mindat': "mindat one",
                                     'resource_mineralienatlas': "atlas one",
                                     'created_at': self.mineraltype_one.created_at.isoformat().replace('+00:00', 'Z'),
                                     'last_modified': self.mineraltype_one.last_modified.isoformat().replace('+00:00',
                                                                                                             'Z')
                                     }
        self.mineraltype_two = MineralType.objects.create(trivial_name="testmineral two", systematics="HT",
                                                          variety="many two", minerals="minerals two",
                                                          mohs_scale="mohs two", density="hard two",
                                                          streak="streak two", normal_color="color two",
                                                          fracture=["HK"], cleavage=["PL"], lustre=["AS"],
                                                          chemical_formula="CHEMTWO", other="other two",
                                                          resource_mindat="mindat two",
                                                          resource_mineralienatlas="atlas two")
        self.mineraltype_two_dict = {'trivial_name': "testmineral two", 'systematics': "HT",
                                     'variety': "many two", 'minerals': "minerals two",
                                     'mohs_scale': "mohs two", 'density': "hard two",
                                     'streak': "streak two", 'normal_color': "color two",
                                     'fracture': ["HK"], 'cleavage': ["PL"], 'lustre': ["AS"],
                                     'chemical_formula': "CHEMTWO", 'other': "other two",
                                     'resource_mindat': "mindat two",
                                     'resource_mineralienatlas': "atlas two",
                                     'created_at': self.mineraltype_two.created_at.isoformat().replace('+00:00', 'Z'),
                                     'last_modified': self.mineraltype_two.last_modified.isoformat().replace('+00:00',
                                                                                                             'Z')
                                     }

        self.crystalsystem_one = CrystalSystem.objects.create(mineral_type=self.mineraltype_one, crystal_system="TC",
                                                              temperature=90, pressure=80)
        self.crystalsystem_one_dict = {'mineral_type': self.mineraltype_one_dict, 'crystal_system': "TC",
                                       'temperature': 90, 'pressure': 80, }
        self.crystalsystem_two = CrystalSystem.objects.create(mineral_type=self.mineraltype_two, crystal_system="TF",
                                                              temperature=92, pressure=82)
        self.crystalsystem_two_dict = {'mineral_type': self.mineraltype_two_dict, 'crystal_system': "TF",
                                       'temperature': 92, 'pressure': 82, }

        self.handpiece_one = Handpiece.objects.create(name="handpiece one",
                                                      finding_place="nowhere one", current_location="here one",
                                                      old_inventory_number="inven one")
        self.handpiece_one.mineral_type = [self.mineraltype_one, ]
        self.handpiece_one_dict = {'name': "handpiece one", 'mineral_type': self.mineraltype_one_dict,
                                   'finding_place': "nowhere one", 'current_location': "here one",
                                   'old_inventory_number': "inven one",
                                   'created_at': self.handpiece_one.created_at.isoformat().replace('+00:00', 'Z'),
                                   'last_modified': self.handpiece_one.last_modified.isoformat().replace('+00:00', 'Z')
                                   }
        self.handpiece_two = Handpiece.objects.create(name="handpiece two",
                                                      finding_place="nowhere two", current_location="here two",
                                                      old_inventory_number="inven two")
        self.handpiece_two.mineral_type = [self.mineraltype_two, ]
        self.handpiece_two_dict = {'name': "handpiece two", 'mineral_type': self.mineraltype_two_dict,
                                   'finding_place': "nowhere two", 'current_location': "here two",
                                   'old_inventory_number': "inven two",
                                   'created_at': self.handpiece_two.created_at.isoformat().replace('+00:00', 'Z'),
                                   'last_modified': self.handpiece_two.last_modified.isoformat().replace('+00:00', 'Z')
                                   }
        self.photograph_one = Photograph.objects.create(image_file="image_one.jpg", handpiece=self.handpiece_one,
                                                        orientation="T", shot_type="MA")
        self.photograph_one_dict = {'image_file': "image_one.jpg", 'handpiece': self.handpiece_one_dict,
                                    'orientation': "T", 'shot_type': "MA",
                                    'created_at': self.photograph_one.created_at.isoformat().replace('+00:00', 'Z'),
                                    'last_modified': self.photograph_one.last_modified.isoformat().replace('+00:00',
                                                                                                           'Z'),
                                    }
        self.photograph_two = Photograph.objects.create(image_file="image_two.jpg", handpiece=self.handpiece_two,
                                                        orientation="S", shot_type="MI")
        self.photograph_two_dict = {'image_file': "image_two.jpg", 'handpiece': self.handpiece_two_dict,
                                    'orientation': "S", 'shot_type': "MI",
                                    'created_at': self.photograph_two.created_at.isoformat().replace('+00:00', 'Z'),
                                    'last_modified': self.photograph_two.last_modified.isoformat().replace('+00:00',
                                                                                                           'Z'),
                                    }

    # Several tests wether Filter Mineraltype View can filter all needed fields

    def test_can_filter_trivial_name(self):
        response = self.client.get(reverse('api:mineraltype-filter'), {'trivial_name': "testmineral one"},
                                   format="json")
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert (self.mineraltype_one_dict in response_dict) == True

    def test_can_filter_systematics(self):
        response = self.client.get(reverse('api:mineraltype-filter'), kwargs={'systematics': "HG"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert (self.mineraltype_one_dict in response_dict) == True

    def test_can_filter_variety(self):
        response = self.client.get(reverse('api:mineraltype-filter'), kwargs={'variety': "many one"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert (self.mineraltype_one_dict in response_dict) == True

    def test_can_filter_minerals(self):
        response = self.client.get(reverse('api:mineraltype-filter'), kwargs={'minerals': "minerals one"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert (self.mineraltype_one_dict in response_dict) == True

    def test_can_filter_mohs_scale(self):
        response = self.client.get(reverse('api:mineraltype-filter'), kwargs={'mohs_scale': "mohs one"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert (self.mineraltype_one_dict in response_dict) == True

    def test_can_filter_density(self):
        response = self.client.get(reverse('api:mineraltype-filter'), kwargs={'density': "hard one"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert (self.mineraltype_one_dict in response_dict) == True

    def test_can_filter_streak(self):
        response = self.client.get(reverse('api:mineraltype-filter'), kwargs={'streak': "streak one"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert (self.mineraltype_one_dict in response_dict) == True

    def test_can_filter_normal_color(self):
        response = self.client.get(reverse('api:mineraltype-filter'), kwargs={'normal_color': "color one"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert (self.mineraltype_one_dict in response_dict) == True

    def test_can_filter_fracture(self):
        response = self.client.get(reverse('api:mineraltype-filter'), kwargs={'fracture': "HF"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert (self.mineraltype_one_dict in response_dict) == True

    def test_can_filter_cleavage(self):
        response = self.client.get(reverse('api:mineraltype-filter'), kwargs={'cleavage': "PE"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert (self.mineraltype_one_dict in response_dict) == True

    def test_can_filter_lustre(self):
        response = self.client.get(reverse('api:mineraltype-filter'), kwargs={'lustre': "AM"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert (self.mineraltype_one_dict in response_dict) == True

    def test_can_filter_chemical_formula(self):
        response = self.client.get(reverse('api:mineraltype-filter'), kwargs={'chemical_formula': "CHEMONE"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert (self.mineraltype_one_dict in response_dict) == True

    def test_can_filter_other(self):
        response = self.client.get(reverse('api:mineraltype-filter'), kwargs={'other': "other one"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert (self.mineraltype_one_dict in response_dict) == True

    def test_can_filter_resource_mindat(self):
        response = self.client.get(reverse('api:mineraltype-filter'), kwargs={'resource_mindat': "mindat one"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert (self.mineraltype_one_dict in response_dict) == True

    def test_can_filter_resource_mineralienatlas(self):
        response = self.client.get(reverse('api:mineraltype-filter'), kwargs={'resource_mineralienatlas': "atlas one"})
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert (self.mineraltype_one_dict in response_dict) == True
