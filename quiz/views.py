from django.shortcuts import render

from .forms import UserForm, QuizForm


def user_view(request):
    username = None
    result = None
    if request.POST:
        form = UserForm(request.POST)
        quiz_form = QuizForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
        if quiz_form.is_valid():
            cd = quiz_form.cleaned_data
            if cd['option'] == '3':
                result = 100
            else:
                result = 1
                result -= 1
    else:
        form = UserForm()
    return render(request, 'user_form.html', locals())


