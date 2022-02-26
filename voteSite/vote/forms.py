from django import forms
from vote.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '투표 주제',
            'content': '투표 내용',
        }