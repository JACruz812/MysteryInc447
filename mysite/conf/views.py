from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LoadForm
from .models import Clue as DBClue
from .models import Story as DBStory
import json


# These objects will need to be transformed into models later on
# but as of right now they work since no information is being saved
# to the database in regards to the story
class Clue:
    clue_id = 0
    clue_num = 0
    clue_text = ''
    clue_img_url = ''
    clue_parents = []


class Story:
    title = ''
    synopsis = ''
    clue_amount = 0
    Clues = []


# Turns the input into an array allowing for ease of access and manipulation
# of clues within the temp_story
def load_parent_list(parent_list):
    jsonDec = json.decoder.JSONDecoder()
    return jsonDec.decode(parent_list)


# Turns the input array into a string allowing for easy saves into the database
def save_parent_list(parent_list):
    return json.dumps(parent_list)


# Takes in the string version of the list created by the user and converts it into
# a list that is to be saved in the temp clue object
def create_list(my_string, in_exist):
    finished_list = []
    if my_string != '':
        my_list = my_string.split(',')
        length = len(my_list)
        for i in range(length):
            try:
                temp_int = int(my_list[i])
                if temp_int > 0:
                    if temp_int in in_exist:
                        if temp_int not in finished_list:
                            finished_list.append(temp_int)

            except:
                pass

    return finished_list


global temp_story
temp_story = Story()


######################################################################

# This view function is used when signup is called
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
            # return to home page if account
            return redirect('home')
    else:
        # else create an empty form
        form = UserCreationForm()
    # return the form to signup.html to handle if error
    return render(request, 'signup.html', {'form': form})


# This view function is used when signout is called
def signout(request):
    logout(request)
    # redirect to the login page after the user is logged out
    return redirect('login')


def index(request):
    return render(request, 'index.html', context={})


def new_story(request):
    global temp_story

    # Clears the contents of the clue list in the story to clear memory
    temp_story.Clues.clear()
    ######################################################################

    # Sets the temp story to a blank story
    temp_story.title = ''
    temp_story.synopsis = ''
    temp_story.clue_amount = 0
    ######################################################################

    return HttpResponseRedirect(reverse('storyboard'))

def loadworkaround(request):
    Choices=[]#Will be a list of tupples
    username = request.user.username
    s=DBStory.objects.filter(user=username)#find stories written by the user
    #Append all of the user's stories to Choices as tupples because the ChoiceField attribute in forms expects it
    for stor in s:
        Choices.append((stor.title,stor.title))
    #Create a form with choices that match the stories the user wrote
    form =LoadForm(choices=Choices)
    #render the form on story_select.html
    return render(request, 'story_select.html', {'form': form})
def load_story(request):
    username = request.user.username
    if request.method =="POST":
        #Get the selected stories title from the form
        s_title=request.POST['story_title']
        #Load the story from the database
        s=DBStory.objects.get(title=s_title,user=username)
        #Fill in the values fot temp_story from s
        temp_story.title=s.title
        temp_story.synopsis=s.synopsis
        temp_story.clue_amount=s.num_clues
        #Clear the temp_story clues
        temp_story.Clues.clear()
        #add the clues from s to temp_story
        for i in range(0,s.num_clues):
            temp_story.Clues.append(DBClue.objects.get(story=s,clue_num=i+1))
    return HttpResponseRedirect(reverse('storyboard'))


def save_story(request):
    if request.method == 'POST':

        # Accesses the temp story add inserts a blank clue to the end of the clue list that is not connected to any clue
        # while increasing the clue counter in the story
        global temp_story

        temp_story.title = request.POST['title']
        temp_story.synopsis = request.POST['synopsis']
        ######################################################################

        # Reads in the contents of existing clues in the storyboard and stores the content to the stories clues list
        for x in temp_story.Clues:
            x.clue_text = request.POST['clue' + str(x.clue_num) + '_text']
            x.clue_img_url = request.POST['clue' + str(x.clue_num) + '_img_url']
        ######################################################################

        # create a story object with the title,synopsis, and clue amounts from the temp_story
        username = request.user.username

        if DBStory.objects.filter(title=temp_story.title, user=username).exists():
            s = DBStory.objects.get(title=temp_story.title, user=username)
            s.synopsis = temp_story.synopsis
            s.num_clues = temp_story.clue_amount
            s.clue_set.all().delete()
        else:
            s = DBStory(title=temp_story.title, synopsis=temp_story.synopsis, num_clues=temp_story.clue_amount,
                        user=username)

        s.save()

        for clue in temp_story.Clues:
            s.clue_set.create(clue_id=clue.clue_id, clue_num=clue.clue_num, clue_text=clue.clue_text,
                              clue_img_url=clue.clue_img_url, parent_list=save_parent_list(clue.clue_parents))
        s.save()

    return HttpResponseRedirect(reverse('refresh_story'))
    
def storyboard(request):
    return render(request, 'Storyboard.html', context={'title': temp_story.title, 'synopsis': temp_story.synopsis,
                                                       'clues': temp_story.Clues})


def add_clue(request):
    if request.method == 'POST':

        # Accesses the temp story add inserts a blank clue to the end of the clue list that is not connected to any clue
        # while increasing the clue counter in the story
        global temp_story
        temp_story.title = request.POST['title']
        temp_story.synopsis = request.POST['synopsis']
        temp_story.clue_amount += 1
        temp_clue = Clue()
        temp_clue.clue_num = temp_story.clue_amount
        ######################################################################

        # Reads in the contents of existing clues in the storyboard and stores the content to the stories clues list
        for x in temp_story.Clues:
            x.clue_text = request.POST['clue' + str(x.clue_num) + '_text']
            x.clue_img_url = request.POST['clue' + str(x.clue_num) + '_img_url']
            # x.clue_parents = request.POST['clue' + str(x.clue_num) + '_clue_parents']
        ######################################################################

        # Adds an empty clue to the end of the stories clue list
        temp_story.Clues.append(temp_clue)
        ######################################################################

    return HttpResponseRedirect(reverse('storyboard'))


def remove_clue(request):
    if request.method == 'POST':

        global temp_story
        # Accesses the temp_story and set the title and synopsis variables
        temp_story.title = request.POST['title']
        temp_story.synopsis = request.POST['synopsis']

        marked = []

        # Loop through the Clues in the story setting all available data
        for x in temp_story.Clues:
            x.clue_text = request.POST['clue' + str(x.clue_num) + '_text']
            x.clue_img_url = request.POST['clue' + str(x.clue_num) + '_img_url']
            # x.clue_parents = request.POST['clue' + str(x.clue_num) + 'clue_parents']

            # If the clue has been marked for removal add the clue number to the marked list
            if request.POST['clue' + str(x.clue_num) + '_remove'] == "Remove":
                marked.append(int(x.clue_num) - 1)

        # Loop through the marked list and remove the corresponding clue from Clue list in
        # temp_story
        for x in reversed(marked):
            temp_clue = temp_story.Clues[x]
            temp_story.Clues.remove(temp_clue)
            del temp_clue

            # Once the clue is removed lower the clue nums of all clues that came after
            # the removed clue
            for clue in reversed(temp_story.Clues):

                if clue.clue_num > x:
                    clue.clue_num -= 1
                else:
                    break

            # Decrease the clue amount in the temp_story
            temp_story.clue_amount -= 1

    return HttpResponseRedirect(reverse('storyboard'))


def refresh_story(request):
    if request.method == 'POST':

        # Accesses the temp story add inserts a blank clue to the end of the clue list that is not connected to any clue
        # while increasing the clue counter in the story
        global temp_story

        temp_story.title = request.POST['title']
        temp_story.synopsis = request.POST['synopsis']
        ######################################################################

        # Reads in the contents of existing clues in the storyboard and stores the content to the stories clues list
        for x in temp_story.Clues:
            x.clue_text = request.POST['clue' + str(x.clue_num) + '_text']
            x.clue_img_url = request.POST['clue' + str(x.clue_num) + '_img_url']
            # x.clue_parents = request.POST['clue' + str(x.clue_num) + '_clue_parents']
        ######################################################################

    return HttpResponseRedirect(reverse('storyboard'))


# allows user to go back to the Storyboard editor from the visually displayed clues page
def return_to_editor(request):
    return render(request, 'Storyboard.html', context={})


# allows user to access visual clues page
def display_clues(request):
    return render(request, 'display_clues.html', context={})
