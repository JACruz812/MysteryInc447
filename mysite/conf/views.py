from django.contrib.auth import login, authenticate, logout
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
#This view function is used when signout is called
def signout(request):
    logout(request)
    #redirect to the login page after the user is logged out
    return redirect('login')
def index(request):
    return render(request, 'index.html', context={})
def new_story(request):
    return render(request, 'Storyboard.html', context={})
def load_story(request):
    return render(request, 'Storyboard.html', context={})

def storyboard(request):
    # First checks to see if the username exists in the database
    # try:
    #     user = user.username
    # except User.DoesNotExist:
    #     raise Http404("User does not exist")
    # # Checks to see if the username corresponds to the logged in user
    # # if it does then progress to the storyboard else alert user to
    # # the error
    # if user.username == selected.username:
    #     author_name = user.username
    #     context = {
    #         'author_name': author_name,
    #     }
    #     # may need to alter path once files are being merged in github
        return render(request, 'Storyboard.html', context={})
    # else:
    #     raise Http404("Username does not match logged in user")


