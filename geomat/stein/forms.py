from django.forms import ModelForm, Textarea, CharField
from django.contrib.postgres.forms import SimpleArrayField
from geomat.stein.models import GlossaryEntry


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
