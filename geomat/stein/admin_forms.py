
from django import forms
from django.contrib import admin


from geomat.stein.models import QuizQuestion, QuizAnswer


class QuizQuestionAdminForm(forms.ModelForm):
    """
    Also the Questiontext is a CharField we want the Widget of a Textfield
    in the Admin interface.
    """

    class Meta:
        model = QuizQuestion
        widgets = {
            "qtext": forms.Textarea()
        }
        fields = "__all__"


class QuizAnswerAdminForm(forms.ModelForm):
    """
    Also the Answertext, the Feedback for answering correct and incorrect
    are CharFields we want the Widget of a Textfield in the Admin interface.
    """

    class Meta:
        model = QuizAnswer
        widgets = {
            "atext": forms.Textarea(),
            "feedback_correct": forms.Textarea(),
            "feedback_incorrect": forms.Textarea()
        }
        fields = "__all__"
