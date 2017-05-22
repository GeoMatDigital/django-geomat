<<<<<<< HEAD
<<<<<<< HEAD
from django.test import TestCase, Client
=======
from django.test import TestCase
>>>>>>> e485a85... I cleared the stein.models.py and established basic tests for the api. This contains tests for the "GET"-method only for now.
=======
from django.test import TestCase, Client
>>>>>>> a05fe75... Created basic GET views, tests not working jet
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import CrystalSystem, Handpiece, MineralType, Photograph


<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> e485a85... I cleared the stein.models.py and established basic tests for the api. This contains tests for the "GET"-method only for now.
=======

>>>>>>> a05fe75... Created basic GET views, tests not working jet
class ViewTestCase(TestCase):
    """ Test suite for the api views"""

    def setUp(self):
        """ Define test client and other stuff"""
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a05fe75... Created basic GET views, tests not working jet

        # self.factory = RequestFactory()
        self.client = Client()
        self.handpiece = Handpiece.objects.create(name="testhandpiece", current_location="nowhere")
        self.crystalsystem = CrystalSystem.objects.create(crystal_system="HG", temperature="90")
        self.photograph = Photograph.objects.create(handpiece=self.handpiece, online_status=True)
        self.mineraltype = MineralType.objects.create(trivial_name="testmineraltype", minerals="many minerals")
<<<<<<< HEAD
=======
        self.client = APIClient()
        self.handpiece = Handpiece(name="testhandpiece",current_location="nowhere")
        self.crystalsystem = CrystalSystem(crystal_system="testsystem",temperature="9000")
        self.photograph = Photograph(handpiece=self.handpiece, online_status=True)
        self.mineraltype = MineralType(trivial_name="testmineraltype", minerals="many minerals")
>>>>>>> e485a85... I cleared the stein.models.py and established basic tests for the api. This contains tests for the "GET"-method only for now.
=======
>>>>>>> a05fe75... Created basic GET views, tests not working jet

    def test_api_can_get_a_handpiece(self):
        """ test the api can get a Handpiece."""

        handpiece = Handpiece.objects.get()
        response = self.client.get(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            reverse('api:handpiece'),
            kwargs={'pk': handpiece.id},
            format="json"

=======
            reverse('get_handpiece'),
=======
            reverse('handpiece'),
>>>>>>> 90d581e... Created apiurls in the right directory and edited the right urls,
            kwargs={'pk': handpiece.id},
            format="json"
>>>>>>> e485a85... I cleared the stein.models.py and established basic tests for the api. This contains tests for the "GET"-method only for now.
=======
            reverse('api:handpiece'),
            kwargs={'pk': handpiece.id},
            format="json"

>>>>>>> a05fe75... Created basic GET views, tests not working jet
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, handpiece)

    def test_api_can_get_a_crystalsystem(self):
        """ test the api can get a crystalsystem."""

<<<<<<< HEAD
<<<<<<< HEAD
        crystalsystem = CrystalSystem.objects.get()
        response = self.client.get(
            reverse('api:crystalsystem'),
            kwargs={'pk': crystalsystem.id},
            format="json"

        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, crystalsystem)
=======
        crstalsystem = CrystalSystem.objects.get()
=======
        crystalsystem = CrystalSystem.objects.get()
>>>>>>> a05fe75... Created basic GET views, tests not working jet
        response = self.client.get(
            reverse('api:crystalsystem'),
            kwargs={'pk': crystalsystem.id},
            format="json"

        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
<<<<<<< HEAD
        self.assertContains(response, crstalsystem)
>>>>>>> e485a85... I cleared the stein.models.py and established basic tests for the api. This contains tests for the "GET"-method only for now.
=======
        self.assertContains(response, crystalsystem)
>>>>>>> a05fe75... Created basic GET views, tests not working jet

    def test_api_can_get_a_Photograph(self):
        """ test the api can get a photograph."""

<<<<<<< HEAD
<<<<<<< HEAD
        photograph = Photograph.objects.get()
        response = self.client.get(
            reverse('api:photograph'),
            kwargs={'pk': photograph.id},
            format="json"

        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
=======
        photograph = Photograph.onjects.get()
=======
        photograph = Photograph.objects.get()
>>>>>>> a05fe75... Created basic GET views, tests not working jet
        response = self.client.get(
            reverse('api:photograph'),
            kwargs={'pk': photograph.id},
            format="json"

        )
<<<<<<< HEAD
        self.assertEqual(response.status_code,status.HTTP_200_OK)
>>>>>>> e485a85... I cleared the stein.models.py and established basic tests for the api. This contains tests for the "GET"-method only for now.
=======
        self.assertEqual(response.status_code, status.HTTP_200_OK)
>>>>>>> a05fe75... Created basic GET views, tests not working jet
        self.assertContains(response, photograph)

    def test_api_can_get_a_mineraltype(self):
        """ test the api can get a mineraltype."""

<<<<<<< HEAD
<<<<<<< HEAD
        mineraltype = MineralType.objects.get()
        response = self.client.get(
            reverse('api:mineraltype'),
            kwargs={'pk': mineraltype.id},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, mineraltype)
=======
        mieraltype = MineralType.objects.get()
=======
        mineraltype = MineralType.objects.get()
>>>>>>> a05fe75... Created basic GET views, tests not working jet
        response = self.client.get(
            reverse('api:mineraltype'),
            kwargs={'pk': mineraltype.id},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
<<<<<<< HEAD
        self.assertContains(response, mieraltype)
>>>>>>> e485a85... I cleared the stein.models.py and established basic tests for the api. This contains tests for the "GET"-method only for now.
=======
        self.assertContains(response, mineraltype)
>>>>>>> a05fe75... Created basic GET views, tests not working jet

# Create your tests here.
