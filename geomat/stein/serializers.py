"""Serializers for REST framework"""
from rest_framework import serializers

from geomat.stein.models import CrystalSystem, Handpiece, MineralType, Photograph, Classification


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
                        return_object[key] = super(
                            StdImageField, self).to_representation(field_obj)

        # Also include the original (if possible)
        if hasattr(obj, 'url'):
            return_object['original'] = super(StdImageField,
                                              self).to_representation(obj)

        return return_object


class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = ('classification_name', 'mineral_type')


class NameClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = ('classification_name',)


class MineralTypeSerializer(serializers.ModelSerializer):
    classification = NameClassificationSerializer()
    systematics = serializers.SerializerMethodField()
    fracture = serializers.SerializerMethodField()
    cleavage = serializers.SerializerMethodField()
    lustre = serializers.SerializerMethodField()
    class Meta:
        model = MineralType
        fields = '__all__'
        depth = 1
    def get_systematics(self, obj):
	return obj.get_systematics_display()
    def get_fracture(self, obj):
	lst =[]
	choice_dict = dict(obj.FRACTURE_CHOICES)
	for choice in obj.fracture:
	    lst.append(choice_dict.get(choice))
	return lst
    def get_cleavage(self, obj):
	lst =[]
	choice_dict = dict(obj.CLEAVAGE_CHOICES)
	for choice in obj.cleavage:
	    lst.append(choice_dict.get(choice))
	return lst
    def get_lustre(self, obj):
	lst =[]
	choice_dict = dict(obj.LUSTRE_CHOICES)
	for choice in obj.lustre:
	    lst.append(choice_dict.get(choice))
	return lst


class CrystalSystemSerializer(serializers.ModelSerializer):
    mineral_type = MineralTypeSerializer()

    class Meta:
        model = CrystalSystem
        fields = ('id', 'mineral_type', 'crystal_system', 'temperature',
                  'pressure')


class HandpieceSerializer(serializers.ModelSerializer):
    mineral_type = MineralTypeSerializer(many=True)

    class Meta:
        model = Handpiece
        fields = ('id', 'name', 'mineral_type', 'finding_place',
                  'current_location', 'old_inventory_number', 'created_at',
                  'last_modified')


class PhotographSerializer(serializers.ModelSerializer):
    image_file = StdImageField()
    handpiece = HandpieceSerializer()
    online_status = serializers.BooleanField()

    class Meta:
        model = Photograph
        fields = ('id', 'image_file', 'handpiece', 'orientation', 'shot_type',
                  'online_status', 'created_at', 'last_modified')
