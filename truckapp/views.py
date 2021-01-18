from django.shortcuts import render,redirect
from truckapp.models import Truck
from truckapp.forms import TruckForm
import time


def _time24_to12hr(time_str:str):
    try:
        t = time.strptime(time_str,"%H:%M:%S")
    except ValueError:
        t = time.strptime(time_str,"%H:%M")
    return time.strftime("%I:%M %p",t)

def truck_view(request):
    truck_list=Truck.objects.all()
    for truck in truck_list:
        truck.truck_closing_time = _time24_to12hr(truck.truck_closing_time)
        truck.truck_opening_time = _time24_to12hr(truck.truck_opening_time)
    return render(request,'truckapp/index.html',{'truck_list':truck_list})
    
def truck_add_view(request):
    form=TruckForm()
    if request.method=='POST':
        form=TruckForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(truck_view)
    return render(request,'truckapp/add.html',{'form':form})

def truck_update_view(request,pk):
    truck=Truck.objects.get(id=pk)
    if request.method=='POST':
        form=TruckForm(request.POST,instance=truck)
        if form.is_valid():
            print(form) 
            form.save()
            return redirect(truck_view)
        else:
            print(form.errors)
            return render(request,'truckapp/home.html')

    return render(request,'truckapp/update.html',{'truck':truck})

def truck_delete_view(request,pk):
    truck=Truck.objects.get(id=pk)
    truck.delete()
    return redirect(truck_view)

def _urlify(in_string, in_string_length):
    return in_string[:in_string_length].replace(' ','%20')

def home_view(request):
    truck_list = Truck.objects.all()
    for truck in truck_list:
        truck.truck_closing_time = _time24_to12hr(truck.truck_closing_time)
        truck.truck_opening_time = _time24_to12hr(truck.truck_opening_time)
    return render(request,'truckapp/home.html',{'truck_list':truck_list})

def truck_search_view(request):
        if request.method == 'GET':
            query = request.GET.get('search',None)
            if query:
                truck_list = Truck.objects.filter(food_type__icontains=query)
                if truck_list:
                    for truck in truck_list:
                        truck.truck_closing_time = _time24_to12hr(truck.truck_closing_time)
                        truck.truck_opening_time = _time24_to12hr(truck.truck_opening_time)
                    return render(request,'truckapp/home.html',{'truck_list':truck_list})
                else:
                    return render(request,'truckapp/home.html',{'error':"No trucks for this food type"})

            else:
                return render(request,'truckapp/home.html',{'error':"Enter input in the search"})
        else:
            print(request.method)
        return redirect(home_view)