from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import User

# Create your views here.

def user_list(request):
 request.session['name'] = 'raunak'
 users = User.objects.all()
 return render(request, "users/user_list.html", { "users": users})


 # Retrieve a single user
def user_details(request, pk):
 return HttpResponse(request.session['name'])
 user = get_object_or_404(User, pk=pk)
 return render(request, "users/user_detail.html", { "user": user })

#delete a single user
def user_delete(request, pk):
 return HttpResponse(pk)


