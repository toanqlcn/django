from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from user_auth.form import RegisterForm
 
def register(request):
 
    if request.method == 'POST':
        response = HttpResponse()
        response.write("<h1>Thanks for registering</h1></br>")
        response.write("Your username: " + request.POST['username'] + "</br>")
        response.write("Your email: " + request.POST['email'] + "</br>")
        return response 
  
    registerForm = RegisterForm() 
    return render(request, 'user_auth/register.html', {'form':registerForm})