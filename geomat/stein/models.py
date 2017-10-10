from django.db import models
from django.utils.translation import ugettext_lazy as _
from stdimage.models import StdImageField

from geomat.stein.fields import ChoiceArrayField


# Mostly all fields are defined as CharFields, so the input is easier.
# The max_length is a total arbitrary value that I defined in the beginning.
class Classification(models.Model):
    """
    Defines a classification field which can be added as a ForeignKey to the MineralType class.
    """
    # mineral_type = models.ForeignKey(
    #     MineralType, null=True, verbose_name=_('mineral type'), related_name="classification")
    classification_name = models.CharField(
        max_length=100, null=True, verbose_name=_("classification"))

    class Meta:
        verbose_name = _("classification")
        verbose_name_plural = _("classifications")

    def __unicode__(self):
        return self.classification_name

    def __str__(self):
        return self.classification_name


class MineralType(models.Model):
    """
    Defines the mineral type model. This model is used as a
    ManyToMany-field inside the Handpiece model.
    """

    MINERAL_CATEGORIES = (
        ('EL', _("Elements")),
        ('SF', _("Sulfides & Sulfosalts")),
        ('HG', _("Halogenides")),
        ('OH', _("Oxides and Hydroxides")),
        ('CN', _("Carbonates and Nitrates")),
        ('BR', _("Borates")),
        ('SL', _("Sulfates")),
        ('PV', _("Phosphates, Arsenates & Vanadates")),
        ('SG', _("Silicates & Germanates")),
        ('OC', _("Organic Compounds")), )

    FRACTURE_CHOICES = (
        ('CF', _("Conchoidal")),
        ('EF', _("Earthy")),
        ('HF', _("Hackly")),
        ('SF', _("Splintery")),
        ('UF', _("Uneven")), )
    CLEAVAGE_CHOICES = (
        ('PE', _("Perfect")),
        ('LP', _("Less perfect")),
        ('GO', _("Good")),
        ('DI', _("Distinct")),
        ('ID', _("Indistinct")),
        ('NO', _("None")), )
    LUSTRE_CHOICES = (
        ('AM', _("Adamantine")),
        ('DL', _("Dull")),
        ('GR', _("Greasy")),
        ('MT', _("Metallic")),
        ('PY', _("Pearly")),
        ('SL', _("Silky")),
        ('SM', _("Submetallic")),
        ('VT', _("Vitreous")),
        ('WY', _("Waxy")), )

    trivial_name = models.CharField(
        max_length=100, blank=True, verbose_name=_("trivial name"))
    systematics = models.CharField(
        max_length=2,
        choices=MINERAL_CATEGORIES,
        default="EL",
        verbose_name=_("systematics"))
    variety = models.CharField(
        max_length=100, blank=True, verbose_name=_("variety"))
    minerals = models.CharField(
        max_length=100, blank=True, verbose_name=_("minerals"))
    mohs_scale = models.CharField(max_length=20, verbose_name=_("mohs scale"))
    density = models.CharField(
        max_length=20, default=0, verbose_name=_("density"))
    streak = models.CharField(max_length=100, verbose_name=_("streak"))
    normal_color = models.CharField(
        max_length=100, verbose_name=_("normal color"))
    fracture = ChoiceArrayField(
        models.CharField(
            max_length=2,
            choices=FRACTURE_CHOICES, ),
        verbose_name=_("fracture"),
        null=True)
    cleavage = ChoiceArrayField(
        models.CharField(
            max_length=2,
            choices=CLEAVAGE_CHOICES, ),
        null=True,
        verbose_name=_("cleavage"))
    lustre = ChoiceArrayField(
        models.CharField(
            max_length=2,
            choices=LUSTRE_CHOICES, ),
        null=True,
        verbose_name=_("lustre"))
    chemical_formula = models.CharField(
        max_length=100, verbose_name=_("chemical formula"))
    other = models.TextField(
        max_length=100, blank=True, verbose_name=_("comment"))
    resource_mindat = models.CharField(
        max_length=100, blank=True, verbose_name=_("MinDat ID"))
    resource_mineralienatlas = models.CharField(
        max_length=100, blank=True, verbose_name=_("MineralienAtlas ID"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("created at"))
    last_modified = models.DateTimeField(
        auto_now=True, verbose_name=_("last modified"))
    classification = models.ForeignKey(
        Classification,
        null=True,
        verbose_name=_('classification'),
        related_name="mineral_type")
    images = StdImageField(
        variations={
        'large': (1200, 800),
        'medium': (900, 600),
        'small': (600, 400),
        'thumbnail': (100, 100, True),
                    },
        blank=True,
        null=True)

    class Meta:
        verbose_name = _("mineral type")
        verbose_name_plural = _("mineral types")

    def __unicode__(self):
        return self.trivial_name

    def __str__(self):
        return self.trivial_name


# class Classification(models.Model):
#     """
#     Defines a classification field which can be added as a ForeignKey to the MineralType class.
#     """
#     # mineral_type = models.ForeignKey(
#     #     MineralType, null=True, verbose_name=_('mineral type'), related_name="classification")
#     classification_name = models.CharField(
#         max_length=100, blank=True, verbose_name=_("classification"))
#
#
#     class Meta:
#         verbose_name = _("Classification")
#         verbose_name_plural = _("Classifications")


class CrystalSystem(models.Model):
    """
    Defines a crystal system, which then should be used as a ForeignKey
    inside the MineralType class.
    """
    CRYSTAL_SYSTEM_CHOICES = (
        ('TC', _("Triclinic")),
        ('MC', _("Monoclinic")),
        ('OR', _("Orthorhombic")),
        ('TT', _("Tetragonal")),
        ('TR', _("Trigonal")),
        ('HG', _("Hexagonal")),
        ('CB', _("Cubic")),
        ('AM', _("Amorph")),)

    mineral_type = models.ForeignKey(
        MineralType,
        null=True,
        verbose_name=_('mineral type'),
        related_name="crystallsystem")
    crystal_system = models.CharField(
        max_length=2,
        blank=True,
        choices=CRYSTAL_SYSTEM_CHOICES,
        verbose_name=_("crystal system"))
    temperature = models.IntegerField(
        blank=True, null=True, verbose_name=_('temperature'))
    pressure = models.IntegerField(
        blank=True, null=True, verbose_name=_('pressure'))

    class Meta:
        verbose_name = _("Crystal System")
        verbose_name_plural = _("Crystal Systems")

    def __str__(self):
        return '{} ({})'.format(self.mineral_type, self.crystal_system)


class Handpiece(models.Model):
    """
    A model for the geological handpieces.
    """

    name = models.CharField(
        max_length=100, verbose_name=_("name of handpiece"))
    mineral_type = models.ManyToManyField(
        MineralType, verbose_name=_("mineral type"))
    # We will need to maybe change the finding_place to some kind of
    # geolocation.
    finding_place = models.CharField(
        max_length=200, blank=True, verbose_name=_("place of discovery"))
    current_location = models.CharField(
        max_length=200, blank=True, verbose_name=_("current location"))
    old_inventory_number = models.CharField(
        blank=True, max_length=100, verbose_name=_("old inventory number"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("created at"))
    last_modified = models.DateTimeField(
        auto_now=True, verbose_name=_("last modified"))

    class Meta:
        verbose_name = _("Handpiece")
        verbose_name_plural = _("Handpieces")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def list_mineral_types(self):
        # Snippet found here: http://stackoverflow.com/a/18108586/4791226
        return ", ".join([p.trivial_name for p in self.mineral_type.all()])

    list_mineral_types.short_description = _("mineral type(s)")


class Photograph(models.Model):
    """
    Defines the model used for the upload of taken photographs of
    the handpieces.
    """

    ORIENTATION_CHOICES = (
        ('T', _("Top")),
        ('B', _("Bottom")),
        ('S', _("Side")), )
    SHOT_TYPE_CHOICES = (
        ('MI', _("Micro")),
        ('MA', _("Macro")),
        ('FE', _("Fisheye")),
        ('TL', _("Tele")), )

    image_file = StdImageField(variations={
        'large': (1200, 800),
        'medium': (900, 600),
        'small': (600, 400),
        'thumbnail': (100, 100, True),
    })
    handpiece = models.ForeignKey(Handpiece, related_name="photograph")
    orientation = models.CharField(
        max_length=1,
        choices=ORIENTATION_CHOICES,
        verbose_name=_("orientation"))
    shot_type = models.CharField(
        max_length=2, choices=SHOT_TYPE_CHOICES, verbose_name=_("shot type"))
    online_status = models.BooleanField(
        default=False, verbose_name=_("active photograph?"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("created at"))
    last_modified = models.DateTimeField(
        auto_now=True, verbose_name=_("last modified"))

    class Meta:
        verbose_name = _("Photograph")
        verbose_name_plural = _("Photographs")
