from django import forms


# question 'wtf a u doing here? mother father!'
OPTIONS = [
    ('1', 'i\'m doing shit'),
    ('2', 'i\'m wasting time'),
    ('3', 'i\'m coding'),
    ('4', 'i\'m watching youtube')
]


class UserForm(forms.Form):
    username = forms.CharField(max_length=20)


class QuizForm(forms.Form):
    option = forms.ChoiceField(choices=OPTIONS)
