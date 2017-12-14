from django import forms
from django.contrib.postgres.forms import SimpleArrayField
from django.forms import CharField, ModelForm, Textarea
from django.forms.widgets import TextInput

from geomat.stein.models import GlossaryEntry

# This Form was used to enabel full sentences with commas in a ArrayField by defining a | separator
#No longer needed but keep


class GlossaryEntryModelForm(ModelForm):
    examples = SimpleArrayField(
        base_field=CharField(),
        delimiter='|',
        widget=Textarea,
        help_text=
        "When giving more than one example seperate them with a '|' ( Alt Gr + >-Button)."
    )

    class Meta:
        model = GlossaryEntry
        fields = '__all__'


class MineralTypeAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MineralTypeAdminForm, self).__init__(*args, **kwargs)
        self.fields['chemical_formula'].widget = MathJaxField()


class MathJaxField(TextInput):
    class Media:
        js = (
            'https://unpkg.com/lodash@4.16.0/lodash.min.js',
            'https://unpkg.com/vue@latest/dist/vue.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML',
            'common/js/mathjax-vue.js')
        css = {'all': ('common/css/mathjax.css', )}

    template_name = 'widgets/mathjax.html'
