from django.shortcuts import render
from things.forms import ThingForm

def home(request):
    if request.method == 'POST':
        form = ThingForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a new URL or show a success message
    else:
        form = ThingForm()
    return render(request, 'home.html', {'form': form})
