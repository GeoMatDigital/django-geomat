"""Tests for our ArrayField implementation."""
from django.forms.fields import ChoiceField, MultipleChoiceField
from django.forms.widgets import SelectMultiple
from django.test import TestCase

from geomat.stein.fields import ArrayField

FRACTURE_CHOICES = (('CF', "Conchoidal"), ('EF', "Earthy"), ('HF', "Hackly"),
                    ('SF', "Splintery"), ('UF', "Uneven"), )


class ArrayFieldTestCase(TestCase):
    """Class to test the ArrayField."""

    def test_arrayfield_base_field(self):
        """Test that the Field object and its arguments supplied to ArrayField are
        returned correctly.
        """
        form = ChoiceArrayField(ChoiceField(choices=FRACTURE_CHOICES))
        formfield = form.formfield()

        self.assertEqual(formfield.choices, list(FRACTURE_CHOICES))
        self.assertTrue(isinstance(formfield.widget, SelectMultiple))
        self.assertTrue(isinstance(formfield, MultipleChoiceField))
