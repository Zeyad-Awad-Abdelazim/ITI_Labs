from django.shortcuts import render, redirect
from .forms import StudentForm

# Create your views here.
def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return render(request, 'success.html', {'student': student})
    else:
        form = StudentForm()
    return render(request, 'register.html', {'form': form})