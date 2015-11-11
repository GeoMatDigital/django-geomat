from django.db import models
from django.utils.translation import ugettext_lazy as _

# Mostly all fields are defined as CharFields, so the input is easier.
#The max_length is a total arbitrary value that I defined in the beginning.


class MineralType(models.Model):
    """
    Defines the mineral type model. This model is used as a
    ManyToMany-field inside the Handpiece model.
    """

    CRYSTAL_SYSTEM_CHOICES = (
        ('TC', _("Triclinic")),
        ('MC', _("Monoclinic")),
        ('OR', _("Orthorhombic")),
        ('TT', _("Tetragonal")),
        ('TR', _("Trigonal")),
        ('HG', _("Hexagonal")),
        ('CB', _("Cubic")),
    )
    FRACTURE_CHOICES = (
        ('CF', _("Conchoidal")),
        ('EF', _("Earthy")),
        ('HF', _("Hackly")),
        ('SF', _("Splintery")),
        ('UF', _("Uneven")),
    )
    CLEAVAGE_CHOICES = (
        ('BP', _("Basal/Pinacoidal")),
        ('CC', _("Cubic")),
        ('OC', _("Octahedral")),
        ('RC', _("Rhombohedral")),
        ('PM', _("Prismatic")),
        ('DH', _("Dodecahedral")),
    )
    LUSTRE_CHOICES = (
        ('AM', _("Adamantine")),
        ('DL', _("Dull")),
        ('GR', _("Greasy")),
        ('MT', _("Metallic")),
        ('PY', _("Pearly")),
        ('RS', _("Resinous")),
        ('SL', _("Silky")),
        ('SM', _("Submetallic")),
        ('VT', _("Vitreous")),
        ('WY', _("Waxy")),
    )

    trivial_name = models.CharField(
        max_length=100,
        verbose_name=_("trivial name")
    )
    # Do we need some more data here? My notes say "Aufdroeselung der
    # Familien/Gattung des Stuecks"
    variety = models.CharField(max_length=100, verbose_name=_("variety"))
    minerals = models.CharField(max_length=100, verbose_name=_("minerals"))
    classification = models.CharField(
        max_length=100,
        verbose_name=_("classification")
    )
    crystal_system = models.CharField(
        max_length=2,
        choices=CRYSTAL_SYSTEM_CHOICES,
        default="TC",
        verbose_name=_("crystal system")
        )
    mohs_scale = models.CharField(max_length=20, verbose_name=_("mohs scale"))
    streak = models.CharField(max_length=100, verbose_name=_("streak"))
    normal_color = models.CharField(
        max_length=100,
        verbose_name=_("normal color")
    )
    # https://de.wikipedia.org/wiki/Bruch_(Mineral)
    fracture = models.CharField(
        max_length=2,
        choices=FRACTURE_CHOICES,
        default="CF",
        verbose_name=_("fracture")
    )
    # https://de.wikipedia.org/wiki/Spaltbarkeit
    cleavage = models.CharField(
        max_length=2,
        choices=CLEAVAGE_CHOICES,
        default="BP",
        verbose_name=_("cleavage")
    )
    lustre = models.CharField(
        max_length=2,
        choices=LUSTRE_CHOICES,
        default="AM",
        verbose_name=_("lustre")
    )
    chemical_formula = models.CharField(
        max_length=100,
        verbose_name=_("chemical formula")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created at")
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_("last modified")
    )

    def __unicode__(self):
        return self.trivial_name


class Handpiece(models.Model):
    """
    A model for the geological handpieces. Each handpiece
    """

    name = models.CharField(
        max_length=100,
        verbose_name=_("name of Handpiece")
        )
    mineral_type = models.ManyToManyField(
        MineralType,
        verbose_name=_("mineral type")
        )
    # We will need to maybe change the finding_place to some kind of
    # geolocation.
    finding_place = models.CharField(
        max_length=200,
        verbose_name=_("place of discovery")
        )
    current_location = models.CharField(
        max_length=200,
        verbose_name=_("current location")
        )
    old_inventory_number = models.CharField(
        blank=True,
        max_length=100,
        verbose_name=_("old inventory number")
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
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created at")
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_("last modified")
    )

    def __unicode__(self):
        return self.name

    def list_mineral_types(self):
        return self.mineral_type


class Photograph(models.Model):
    """
    Defines the model used for the upload of taken photographs of
    the handpieces.
    """

    ORIENTATION_CHOICES = (
        ('T', _("Top")),
        ('B', _("Bottom")),
        ('S', _("Side")),
    )
    SHOT_TYPE_CHOICES = (
        ('MI', _("Micro")),
        ('MA', _("Macro")),
        ('FE', _("Fisheye")),
        ('TL', _("Tele")),
    )

    image_file = models.ImageField(verbose_name=_("image file"))
    handpiece = models.ForeignKey(Handpiece)
    orientation = models.CharField(
        max_length=1,
        choices=ORIENTATION_CHOICES,
        verbose_name=_("orientation")
    )
    shot_type = models.CharField(
        max_length=2,
        choices=SHOT_TYPE_CHOICES,
        verbose_name=_("shot type")
    )
    online_status = models.BooleanField(
        default=False,
        verbose_name=_("active photograph?")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created at")
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_("last modified")
    )
