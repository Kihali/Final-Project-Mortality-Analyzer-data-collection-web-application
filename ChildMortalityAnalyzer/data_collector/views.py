from django.shortcuts import render, redirect
from .forms import ChildMortalityForm
from .models import ChildMortality
import csv
from django.http import HttpResponse
from django.http import JsonResponse
from data_collector.models import ChildMortality

def home(request):
    return render(request, 'data_collector/home.html')

def add_data(request):
    if request.method == 'POST':
        form = ChildMortalityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_data')
    else:
        form = ChildMortalityForm()
    return render(request, 'data_collector/add_data.html', {'form': form})

def export_data(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="child_mortality_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Year', 'Mortality Rate'])

    for data in ChildMortality.objects.all():
        writer.writerow([data.year, data.mortality_rate])

    return response

def clear_data(request):
    if request.method == 'POST':
        # Clear data from the database
        ChildMortality.objects.all().delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)