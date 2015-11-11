from django.db import models
from django.utils.translation import ugettext_lazy as _


class Handpiece(models.Model):
    """
    A model for the geological handpieces. Each handpiece
    """
    name = models.CharField(
        max_length=100,
        verbose_name=_("Name of Handpiece")
        )
    mineral_type = models.CharField(
        max_length=100,
        verbose_name=_("Mineral type")
        )
    # We will need to maybe change the finding_place to some kind of
    # geolocation.
    finding_place = models.CharField(
        max_length=200,
        verbose_name=_("Place of discovery")
        )
    current_location = models.CharField(
        max_length=200,
        verbose_name=_("Current location")
        )
    old_inventory_number = models.CharField(
        blank=True,
        max_length=100,
        verbose_name=_("Old inventory number")
        )
    resource_mindat = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("MinDat ID")
        )
    resource_mineralienatlas = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("MineralienAtlas ID")
        )
    """
    images = models.OnetoMany(HandpieceImage)
    """
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created at")
        )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Last modified")
        )

    def __unicode__(self):
        return self.name
