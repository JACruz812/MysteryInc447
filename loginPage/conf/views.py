from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

#This view function is used when signup is called
def signup(request):
   #  If the method is requesting to input data than create form, check if valid and save its elements
   if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            #return to home page if account
            return redirect('home')
   else:
       #else create an empty form
        form = UserCreationForm()
    #return the form to signup.html to handle if error
   return render(request, 'signup.html', {'form': form})


