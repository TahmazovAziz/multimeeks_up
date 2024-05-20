from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib.auth import logout
from .forms import UserCreationForm
class LogoutView(View):
    template_name = 'registration/logout.html'

    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        if request.method == 'POST':
            logout(request)
            return redirect('/')

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):         
        return render(request, self.template_name, {'form':UserCreationForm})
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('/')
        return render(request, self.template_name, {"form":form})            
