from django.forms import ModelForm, Textarea, CharField
from django.contrib.postgres.forms import SimpleArrayField
from geomat.stein.models import GlossaryEntry

# This Form was used to enabel full sentences with commas in a ArrayField by defining a | separator
#No longer needed but keep


class GlossaryEntryModelForm(ModelForm):
    examples = SimpleArrayField(base_field=CharField(),
                                delimiter='|',
                                widget=Textarea,
                                help_text=
                                "When giving more than one example seperate them with a '|' ( Alt Gr + >-Button)."
                                )

    class Meta:
        model = GlossaryEntry
        fields = '__all__'
