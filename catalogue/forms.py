from django import forms
from django.forms import ModelForm
from .models import Syllabus
from .models import Section
from .models import Feedback
from .models import MCERecommendation, recAnswer, recQuestions, recCombined

class SyllabusForm(forms.ModelForm):
    class Meta:
        model = Syllabus
        #field = "__all__"   gets all fields from user
        fields = ('originalLocation',)
    originalLocation = forms.FileField(widget=forms.FileInput())
    
#Create Section Form
class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = "__all__"


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('subject', 'sectionID', 'professorID', 'semester', 'review')

class RecommendationForm(forms.ModelForm):
    class Meta:
        model = recCombined
        fields = "__all__"      