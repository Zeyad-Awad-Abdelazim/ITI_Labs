from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def profile(request):
    context = {
        'name': 'Zeyad Awad',
        'bio': 'Software Engineer',
        'skills': ['python', 'Django', 'APIs', 'SQL', 'Git']
    }
    return render(request, 'profile.html', context)