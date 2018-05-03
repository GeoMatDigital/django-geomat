from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields.ranges import FloatRangeField
from geomat.stein.fields import ChoiceArrayField
from stdimage.models import StdImageField


# Mostly all fields are defined as CharFields, so the input is easier.
# The max_length is a total arbitrary value that I defined in the beginning.

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
    SPLIT_CHOICES = (
        ('SU', _('Sulfides')),
        ('SS', _('Sulfosalts')),
        ('CA', _('Carbonates')),
        ('NI', _('Nitrates')),
        ('PH', _('Phosphates')),
        ('AR', _('Arsenates')),
        ('VA', _('Vanadates')),
        ('SI', _('Silicates')),
        ('GE', _('Germanates')),
        ("OX", _("Oxides")),
        ("HY", _("Hydroxides")), )
    SUB_CHOICES=(
        ("IS", _("Island Silicates")),
        ("GS", _("Group Silicates")),
        ("CS", _("Chain Silicates")),
        ("DS", _("Double Chain Silicates")),
        ("CC", _("Cyclo Silicates")),
        ("PS", _("Phyllo Silicates")),
        ("FS", _("Framework Silicates")), )
    CLEAVAGE_CHOICES = (
        ('PE', _("perfect")),
        ('LP', _("less perfect")),
        ('GO', _("good")),
        ('DI', _("distinct")),
        ('ID', _("indistinct")),
        ('NO', _("none")), )
    LUSTRE_CHOICES = (
        ('AM', _("adamantine lustre")),
        ('DL', _("dull lustre")),
        ('GR', _("greasy lustre")),
        ('MT', _("metallic lustre")),
        ('PY', _("pearly lustre")),
        ('SL', _("silky lustre")),
        ('SM', _("submetallic lustre")),
        ('VT', _("vitreous lustre")),
        ('WY', _("waxy lustre")), )
    FRACTURE_CHOICES = (
        ('CF', _("conchoidal")),
        ('EF', _("earthy")),
        ('HF', _("hackly")),
        ('SF', _("splintery")),
        ('UF', _("uneven")), )

    trivial_name = models.CharField(
        max_length=100, blank=True, verbose_name=_("trivial name"))
    systematics = models.CharField(
        max_length=2,
        choices=MINERAL_CATEGORIES,
        default="EL",
        verbose_name=_("systematics"))
    split_systematics = models.CharField(
        max_length=2,
        choices=SPLIT_CHOICES,
        blank=True,
        verbose_name=_("splitted systematics"))
    sub_systematics = models.CharField(
        max_length=2,
        choices=SUB_CHOICES,
        blank=True,
        verbose_name=_("subsystematics")
    )
    variety = models.CharField(
        max_length=100, blank=True, verbose_name=_("variety"))
    minerals = models.CharField(
        max_length=100, blank=True, verbose_name=_("minerals"))
    new_mohs_scale = density = FloatRangeField(null=True, blank=True)
    mohs_scale = models.CharField(max_length=20, verbose_name=_("mohs scale"))
    density = FloatRangeField(null=True, blank=True)
    streak = models.CharField(max_length=100, verbose_name=_("streak"))
    normal_color = models.CharField(
        max_length=100, verbose_name=_("normal color"))
    fracture = ChoiceArrayField(
        models.CharField(
            max_length=2,
            choices=FRACTURE_CHOICES, ),
        null=True,
        verbose_name=_("fracture"))
    lustre = ChoiceArrayField(
        models.CharField(
            max_length=2,
            choices=LUSTRE_CHOICES, ),
        null=True,
        verbose_name=_("lustre"))
    chemical_formula = models.CharField(
        max_length=100, verbose_name=_("chemical formula"))
    other = models.TextField(
        max_length=500, blank=True, verbose_name=_("comment"))
    resource_mindat = models.CharField(
        max_length=100, blank=True, verbose_name=_("MinDat ID"))
    resource_mineralienatlas = models.CharField(
        max_length=100, blank=True, verbose_name=_("MineralienAtlas ID"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("created at"))
    last_modified = models.DateTimeField(
        auto_now=True, verbose_name=_("last modified"))

    class Meta:
        verbose_name = _("mineral type")
        verbose_name_plural = _("mineral types")

    def __str__(self):
        return self.trivial_name


class Cleavage(models.Model):
    """
    Defines a Cleavage which should be used as a ForeignKey
    inside the Mineraltype Class.
    """

    CLEAVAGE_CHOICES = (
        ('PE', _("perfect")),
        ('LP', _("less perfect")),
        ('GO', _("good")),
        ('DI', _("distinct")),
        ('ID', _("indistinct")),
        ('NO', _("none")), )

    cleavage = models.CharField(
        max_length=2, choices=CLEAVAGE_CHOICES, verbose_name=_("cleavage"))

    coordinates = models.CharField(
        max_length=100, default="", blank=True, verbose_name=_("coordinates"))

    mineral_type = models.ForeignKey(
        MineralType,
        blank=True,
        null=True,
        verbose_name=_("mineral type"),
        related_name="cleavage",
        on_delete=models.CASCADE)


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
        ('AM', _("Amorph")), )

    mineral_type = models.ForeignKey(
        MineralType,
        null=True,
        verbose_name=_('mineral type'),
        on_delete=models.CASCADE,
        related_name="crystal_system")
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
        return "{} ({})".format(self.mineral_type.minerals,
                                self.crystal_system)


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

    image_file = StdImageField(
        variations={
            'large': (1200, 800),
            'medium': (900, 600),
            'small': (600, 400),
            'thumbnail': (100, 100, True),
        },
        db_index=True)
    handpiece = models.ForeignKey(
        Handpiece, related_name="photograph", on_delete=models.CASCADE)
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


class GlossaryEntry(models.Model):
    """
    Defines a Model for the Glossary which is displayed in the GeoMat App.
    """
    id = models.CharField(
        max_length=100, verbose_name=_("id"), primary_key=True)
    header = models.CharField(
        max_length=200, verbose_name=_("header"), null=True)
    description = models.TextField(verbose_name=_("description"), null=True)

    class Meta:
        verbose_name = _("Glossary Entry")
        verbose_name_plural = _("Glossary Entries")
        ordering = ('header',)


class QuizQuestion(models.Model):
    """
    This Model Defines Questions for the Self-learn Quiz in the GeoMat App.
    """

    QTYPE_CHOICES = (
        ("SC", _("Single Choice")),
        ("MC", _("Multiple Choice")),
        ("DD", _("Drag and Drop")),
        ("RG", _("Ranking")),
        ("HS", _("Hotspot")), )
    DIFFICULTY_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))

    qtext = models.CharField(
        max_length=500, null=True, verbose_name=_("question text"))
    qtype = models.CharField(
        max_length=2,
        choices=QTYPE_CHOICES,
        null=True,
        verbose_name=_("question type"))
    tags = ArrayField(
        base_field=models.CharField(max_length=200),
        null=True,
        help_text=
        "If you want to add more than one tag, seperate them with commas.")
    difficulty = models.IntegerField(
        choices=DIFFICULTY_CHOICES, null=True, verbose_name=_("difficulty"))


class QuizAnswer(models.Model):
    """
    This Model Defines the Answers for a Question of the Self.learn Quiz in the GeoMat App.
    """

    atext = models.CharField(
        max_length=500, null=True, verbose_name=_("answer text"))
    correct = models.BooleanField(
        verbose_name=_("correct"), help_text="Nothing yet.")
    feedback_correct = models.CharField(
        max_length=500,
        default="",
        blank=True,
        verbose_name=_("feedback if answered correctly"))
    feedback_incorrect = models.CharField(
        max_length=500,
        default="",
        blank=True,
        verbose_name=_("feedback if answered incorrectly"))
    question = models.ForeignKey(
        QuizQuestion,
        null=True,
        verbose_name=_("question"),
        related_name="answers",
        on_delete=models.CASCADE)
