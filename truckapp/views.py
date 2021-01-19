from django.shortcuts import render,redirect
from truckapp.models import Truck
from truckapp.forms import TruckForm
import time
from datetime import datetime

# this view for convert time in 12 hr stamp
def _time24_to12hr(time_str:str):
    try:
        t = time.strptime(time_str,"%H:%M:%S")
    except ValueError:
        t = time.strptime(time_str,"%H:%M")
    return time.strftime("%I:%M %p",t)


# truck admin page for Create,update and delete operation
def truck_view(request):
    truck_list=Truck.objects.all()
    for truck in truck_list:
        truck.truck_closing_time = _time24_to12hr(truck.truck_closing_time)
        truck.truck_opening_time = _time24_to12hr(truck.truck_opening_time)
    return render(request,'truckapp/index.html',{'truck_list':truck_list})

# to add new truck
def truck_add_view(request):
    form=TruckForm()
    if request.method=='POST':
        form=TruckForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(truck_view)
    return render(request,'truckapp/add.html',{'form':form})
# to update truck details
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
# to delate truck record
def truck_delete_view(request,pk):
    truck=Truck.objects.get(id=pk)
    truck.delete()
    return redirect(truck_view)

# this is for home page for user.
def home_view(request):
    truck_list = Truck.objects.all()
    status=None
    for truck in truck_list:

              truck.truck_closing_time = _time24_to12hr(truck.truck_closing_time)
              truck.truck_opening_time = _time24_to12hr(truck.truck_opening_time)
              current_time = datetime.now().strftime("%H:%M")
              current_time=_time24_to12hr(current_time)


              if truck.truck_opening_time <= current_time <= truck.truck_closing_time:

                  status='open'
                  # return render(request, 'truckapp/home.html', {'truck_list': truck_list, 'status':status})
              else:
                  status='closed'
                  # return render(request, 'truckapp/home.html', {'truck_list': truck_list, 'status': status})
    return render(request, 'truckapp/home.html', {'truck_list': truck_list, 'status': status})

# this is for serach operation by user
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
        return redirect(home_view)

