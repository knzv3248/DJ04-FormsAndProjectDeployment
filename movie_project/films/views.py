from django.shortcuts import render
from .models import Films
from .forms import FilmsForm

# Create your views here.
def index(request):
    films = Films.objects.all()
    return render(request, 'films/index.html', {'films': films})

def add_review(request):
    error = ""
    if request.method == 'POST':
        form = FilmsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'films/add_review.html', {'form': form})
        else:
            error = "Форма заполнена неверно"
    form = FilmsForm()
    return render(request, 'films/add_review.html', {'form': form})