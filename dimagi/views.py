from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
import django.forms
import requests
import traceback
from django.forms.utils import ErrorList
from .forms import UserForm
from .models import User
from .CityFinder import CityFinder
from .Tracker import Tracker


# def view1 (request):
#     users = User.objects.all()
#     return render(request,"dimagi/users.html",{'users_list':users})
#     # return HttpResponse("Hello")

class UserListView (generic.ListView):
    model = User
    template_name = "dimagi/users.html"

    # provides the ability to order by year in descending order
    def get_queryset(self):
        return User.objects.order_by('email')

class UserFormView(generic.ListView):
    form_class = UserForm
    template_name = "dimagi/userloc.html"

    def get (self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post (self,request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if request.POST.get('checkin'):
                email = request.POST.get('email')
                city = request.POST.get('city')
                state = request.POST.get('state')
                country = request.POST.get('country')
                t = Tracker()
                try:
                    user = t.get_user(email)
                    city_data = CityFinder().find_city_data(city,state,country)
                    # lookup user and update their record.
                    if city_data:
                        Tracker().update_user_location(user, city, city_data)
                    else:
                        Tracker().update_user_location(user, city, None)
                        print("Couldn't find city data")
                        raise django.forms.ValidationError(f"Couldnt figure out city {city}")
                    # lookup city
                    # store in db
                    return redirect('user-locations')
                except Exception as e:
                    traceback.print_exc()
                    form.errors[django.forms.forms.NON_FIELD_ERRORS] = ErrorList([e.__str__()])
                    return render(request, self.template_name, {'form': form})
