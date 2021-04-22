from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import HttpResponseNotFound
from django.shortcuts import render

from .forms import UserForm, UserForm2
from .models import Person





#Получение данных из БД
def index(request):
	people = Person.objects.all()
	return render(request, "firstapp/index.html",{"people": people})

def create(request):
	if request.method == "POST":
		tom = Person()
		tom.name = request.POST.get("name")
		tom.age = request.POST.get("age")
		tom.save()
	return HttpResponseRedirect("/")









def m404(request):
	return HttpResponseNotFound("<h2>Not Found</h2>")

def about(request):
	return HttpResponse("About")

def contact(request):
	return HttpResponseRedirect("/about")

def details(request):
	return HttpResponsePermanentRedirect("/")


def products(request, productid=21):
	category = request.GET.get("cat","hamburger")
	output = "<h2>Product № {0} Category: {1}</h2>".format(productid, category)
	return HttpResponse(output)


def users(request):
	id = request.GET.get("id",1)
	name = request.GET.get("name","Uvuvwevwevwe Onyetenyevwe Ugwemuhwem Osas")
	output = "<h2>User</h2><h3>id: {0} name: {1} </h3>".format(id,name)
	return HttpResponse(output)

def condit(request):
	data = {"n":-5}
	return render(request,"firstapp/condit.html", context = data)

def langs(request):
	langs = ["English", "German", "French", "Spanish", "Chineese"]
	return render(request, "firstapp/langs.html", context = {"langs": langs})

