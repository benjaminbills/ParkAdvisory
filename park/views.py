from django.shortcuts import render, redirect
from .forms import ParkForm
from .models import Parks
from .filters import ParkFilter

def home(request):
    parks = Parks.objects.all()
    context = {'parks':parks }
    return render(request, 'home.html', context)

def addPark(request):
    current_user = request.user
    if request.method == 'POST':
        form = ParkForm(request.POST, request.FILES)
        if form.is_valid():
            park = form.save(commit=False)
            park.user = current_user
            park.save()
        return redirect('home')

    else:
        form = ParkForm()
    context = {'form':form}
    return render(request, 'parks/add_park.html', context)

def getParks(request):
    parks = Parks.objects.all()
    myFilter = ParkFilter(request.GET, queryset=parks)
    parks = myFilter.qs
    context = {'parks':parks, 'myFilter':myFilter}
    return render(request, 'parks/parks.html', context)