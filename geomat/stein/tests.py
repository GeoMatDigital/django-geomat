from django.test import TestCase
from .models import MineralType,Classification, CrystalSystem, Handpiece, Photograph

class MineralTypeTestCase(TestCase):
    """ This class defines the test suite for the mieraltype model."""

    def setUp(self):
        self.mineral_type_name = "New MineralType"
        self.mineral_type = MineralType(trivial_name=self.mineral_type_name)

    def test_mineral_catigories_not_empty(self):
        """
        1) Test wether mineral Categories choices is empty.
        """
        categories = self.mineral_type.MINERAL_CATEGORIES

        self.assertEqual(True, all(categories))


# Create your tests here.
