from rest_framework import serializers
from .models import CrystalSystem, Handpiece, Photograph, MineralType


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
    handpiece = HandpieceSerializer()
    image_file = serializers.ImageField()

    class Meta:

        model = Photograph
        fields = ('image_file', 'handpiece', 'orientation', 'shot_type', ' online_status', 'created_at', 'last_modified')


