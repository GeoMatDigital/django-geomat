from rest_framework import serializers
from .models import CrystalSystem, Handpiece, Photograph, MineralType


class StdImageField(serializers.ImageField):
    """
    Get all the variations of the StdImageField
    """

    def to_native(self, obj):
        return self.get_variations_urls(obj)

    def to_representation(self, obj):
        return self.get_variations_urls(obj)

    def get_variations_urls(self, obj):
        """
        Get all the logo urls.
        """

        # Initiate return object
        return_object = {}

        # Get the field of the object
        field = obj.field

        # A lot of ifs going araound, first check if it has the field variations
        if hasattr(field, 'variations'):
            # Get the variations
            variations = field.variations
            # Go through the variations dict
            for key in variations.keys():
                # Just to be sure if the stdimage object has it stored in the obj
                if hasattr(obj, key):
                    # get the by stdimage properties
                    field_obj = getattr(obj, key, None)
                    if field_obj and hasattr(field_obj, 'url'):
                        # store it, with the name of the variation type into our return object
                        return_object[key] = super(StdImageField, self).to_representation(field_obj)

        # Also include the original (if possible)
        if hasattr(obj, 'url'):
            return_object['original'] = super(StdImageField, self).to_representation(obj)

        return return_object


class MineralTypeSerializer(serializers.ModelSerializer):

    class Meta:

        model = MineralType
        fields = ('trivial_name', 'systematics', 'variety', 'minerals', 'mohs_scale', 'density', 'streak',
                  'normal_color', 'fracture', 'cleavage', 'lustre', 'chemical_formula', 'other', 'resource_mindat',
                  'resource_mineralienatlas', 'created_at', 'last_modified')


class CrystalSystemSerializer(serializers.ModelSerializer):
    mineral_type = MineralTypeSerializer()

    class Meta:

        model = CrystalSystem
        fields = ('mineral_type', 'crystal_system', 'temperature', 'pressure')


class HandpieceSerializer(serializers.ModelSerializer):
    mineral_type = MineralTypeSerializer(many=True)

    class Meta:

        model = Handpiece
        fields = ('name', 'mineral_type', 'finding_place', 'current_location', 'old_inventory_number',
                  'created_at', 'last_modified')


class PhotographSerializer(serializers.ModelSerializer):
    image_file = StdImageField()
    handpiece = HandpieceSerializer()
    online_status = serializers.BooleanField()

    class Meta:

        model = Photograph
        fields = ('image_file', 'handpiece', 'orientation', 'shot_type', 'online_status', 'created_at', 'last_modified')


