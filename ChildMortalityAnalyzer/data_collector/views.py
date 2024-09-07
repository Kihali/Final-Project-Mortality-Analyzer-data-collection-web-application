from django.shortcuts import render, redirect
from .forms import ChildMortalityForm
from .models import ChildMortality
import csv
from django.http import HttpResponse, JsonResponse

def home(request):
    return render(request, 'data_collector/home.html')

def add_data(request):
    if request.method == 'POST':
        form = ChildMortalityForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form saved successfully!")  # Debugging statement
            return redirect('add_data')
        else:
            print("Form errors:", form.errors)  # Debugging statement
    else:
        form = ChildMortalityForm()
    return render(request, 'data_collector/add_data.html', {'form': form})

def export_data(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="child_mortality_data.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'Facility Name', 'Facility Location', 'Facility Capacity',
        'Child Age', 'Child Gender', 'Cause of Death', 
        'Region Name', 'Population', 'GDP'
    ])

    for data in ChildMortality.objects.all():
        writer.writerow([
            data.facility_name, data.facility_location, data.facility_capacity, 
            data.child_age, data.child_gender, data.cause_of_death, 
            data.region_name, data.population, data.gdp
        ])

    return response

def clear_data(request):
    if request.method == 'POST':
        ChildMortality.objects.all().delete()
        return JsonResponse({'message': 'Data cleared successfully!'})
    return JsonResponse({'status': 'fail'}, status=400)
