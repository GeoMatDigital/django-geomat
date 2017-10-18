import pytest
from django.test import TestCase
from django.db import models
from django.contrib.postgres.fields import ArrayField


class QuizQuestionModelExistsTestCase(TestCase):

    def test_model_existence(self):
        """Thsi test just lokks wether or not we can import the model right away"""

        import_result = None

        try:
            from geomat.stein.models import QuizQuestion
        except ImportError:
            pass
        else:
            import_result = True

        assert import_result


class QuizAnswerModelExistsTestCase(TestCase):

    def test_model_existence(self):
        """Thsi test just lokks wether or not we can import the model right away"""

        import_result = None

        try:
            from geomat.stein.models import QuizAnswer
        except ImportError:
            pass
        else:
            import_result = True

        assert import_result


from geomat.stein.models import QuizQuestion, QuizAnswer


class QuizQuestionModelFieldsTestCase(TestCase):
    """
    This Testcase is designed to ensure that the new
    modle has all required Fileds and the Fieldtypes are correct.
    """

    def setUp(self):
        self.model = QuizQuestion()

    def test_model_has_qtype(self):
        assert hasattr(self.model, 'qtext')

    def test_model_has_qtext(self):
        assert hasattr(self.model, 'qtext')

    def test_model_has_tags(self):
        assert hasattr(self.model, 'tags')

    def test_model_has_difficulty(self):
        assert hasattr(self.model, 'difficulty')

    def test_model_has_answers(self):
        assert hasattr(self.model, 'answers')

    def test_field_type_qtype(self):
        assert issubclass(self.model._meta.get_field('qtype').__class__, models.CharField().__class__)

    def test_field_type_qtext(self):
        assert issubclass(self.model._meta.get_field('qtext').__class__, models.CharField().__class__)

    def test_field_type_tags(self):
        assert issubclass(self.model._meta.get_field('tags').__class__, ArrayField)

    def test_field_type_difficulty(self):
        assert issubclass(self.model._meta.get_field('difficulty').__class__, models.IntegerField().__class__)

    def test_field_type_answers(self):
        assert issubclass(self.model._meta.get_field('answers').__class__, models.ManyToOneRel)


class QuizAnswerModleFieldsTestCase(TestCase):

    def setUp(self):
        self.model = QuizAnswer()

    def test_model_has_atext(self):
        assert hasattr(self.model, 'atext')

    def test_model_has_correct(self):
        assert hasattr(self.model, 'correct')

    def tes_model_has_feedback_correct(self):
        assert hasattr(self.model, 'feedback_correct')

    def test_model_has_feedback_incorrect(self):
        assert hasattr(self.model, 'feedback_incorrect')

    def test_model_has_question(self):
        assert hasattr(self.model, 'question')

    def test_field_type_atext(self):
        assert issubclass(self.model._meta.get_field('atext').__class__, models.CharField().__class__)

    def test_field_type_correct(self):
        assert issubclass(self.model._meta.get_field('correct').__class__, models.BooleanField().__class__)

    def test_field_type_feedback_correct(self):
        assert issubclass(self.model._meta.get_field('feedback_correct').__class__, models.CharField().__class__)

    def test_field_type_feedback_incorrect(self):
        assert issubclass(self.model._meta.get_field('feedback_incorrect').__class__, models.CharField().__class__)

    def test_field_type_question(self):
        assert issubclass(self.model._meta.get_field('question').__class__, models.ForeignKey)

