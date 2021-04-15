
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

# These objects will need to be transformed into models later on
# but as of right now they work since no information is being saved
# to the database in regards to the story
class Clue:
    clue_num = 0 # actual clue number seen by user
    clue_text = ''
    clue_img_url = ''
    parent_clues = [] # list of the actual clues
    parent_clue_ids = [] # list of parent id numbers
    num_parents = 0
    clue_id = 0 # clue id, never changes after initial creation (not updated ever for easy identification)


class Story:
    title = ''
    synopsis = ''
    clue_amount = 0
    clue_id_tracker = 0 # will keep track of overall number of clues that have existed, regardless of how many remain
    Clues = []
    removed_ids = []


global temp_story
temp_story = Story()
######################################################################

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
   
    global temp_story

    # Clears the contents of the clue list in the story to clear memory
    temp_story.Clues.clear()
    ######################################################################

    # Sets the temp story to a blank story
    temp_story.title = ''
    temp_story.synopsis = ''
    temp_story.clue_amount = 0
    temp_story.clue_id_tracker = 0
    ######################################################################
   
    return HttpResponseRedirect(reverse('storyboard'))
   
def load_story(request):
    return HttpResponseRedirect(reverse('storyboard'))

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
        temp_story.clue_id_tracker += 1
        temp_clue = Clue()
        temp_clue.clue_num = temp_story.clue_amount
        temp_clue.clue_id = temp_story.clue_id_tracker
        ######################################################################

        # Reads in the contents of existing clues in the storyboard and stores the content to the stories clues list
        for x in temp_story.Clues:
            x.clue_text = request.POST['clue' + str(x.clue_num) + '_text']
            x.clue_img_url = request.POST['clue' + str(x.clue_num) + '_img_url']
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
        marked_id = []

        # Loop through the Clues in the story setting all available data
        for x in temp_story.Clues:
            x.clue_text = request.POST['clue' + str(x.clue_num) + '_text']
            x.clue_img_url = request.POST['clue' + str(x.clue_num) + '_img_url']

            # If the clue has been marked for removal add the clue number to the marked list
            # also add clue id
            if request.POST['clue' + str(x.clue_num) + '_remove'] == "Remove":
                marked.append(int(x.clue_num) - 1)
                marked.append(int(x.clue_id)) # idk if I will need this to be -1 or if this is at all helpful
                temp_story.removed_ids.append(x.clue_id)

        # Loop through the marked list and remove the corresponding clue from Clue list in
        # temp_story
        for x in reversed(marked):
            temp_clue = temp_story.Clues[x]

            # remove the list of parent clues if needed, not sure it is

            # for i in temp_clue.num_parents:
            # figure out if this is a deep or shallow copy
            # temp_clue.parent_clues.remove()

            # remove the clue from the list
            temp_story.Clues.remove(temp_clue)

            # determine which clues have the clue being removed as a parent and delete them
            for curr_clue in temp_story.Clues:

                # if clue being removed is a parent, remove it from list of parents
                if temp_clue.clue_id in curr_clue.parent_clue_ids:

                    curr_clue.parent_clues.remove(temp_clue) # remove from list of clues, may need to be updated
                    curr_clue.parent_clue_ids.remove(temp_clue.clue_id)
                    curr_clue.num_parents -= 1

            # finally actually delete the clues
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


# allows user to connect two clues together
def connect_clue(request):

    if request.method == 'POST':

        # im assuming this is how I get the parent and child
        x.clue_text = request.POST['clue' + str(x.clue_num) + '_text']

        # Accesses the temp story that contains all of the clues that need to be connected
        global temp_story
        temp_story.title = request.POST['title']
        temp_story.synopsis = request.POST['synopsis']
        ######################################################################

        # check through all clues, find numbers that need to be connected
        for x in temp_story.Clues:

            # empty out list of parent clues
            x.parent_clues = []
            x.parent_clue_ids = []
            x.num_parents = 0

            # add back in any clues if needed
            # may need to replace this with function Connor made
            if request.POST['clue' + str(x.clue_num) + '_parent'] != NULL:

                # connect each parent clue
                # NOT parent_nums, should be size of the array on the webpage
                for i in size(parent_nums):
                    
                    # get parent clue, will need to do verification that this is the correct clue later on when I figure out how we are getting the information
                    # verify using id numbers
                    parent_clue = temp_story.Clues[parent_nums[i - 1]]

                    # add parent clue to child clue's list
                    x.parent_clues.append(parent_clue)
                    x.parent_clue_ids.append(parent_clue.clue_id)
                    x.num_parents += 1

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
        ######################################################################

    return HttpResponseRedirect(reverse('storyboard'))

# allows user to go back to the Storyboard editor from the visually displayed clues page
def return_to_editor(request):
   return render(request, 'Storyboard.html', context={})

# allows user to access visual clues page
def display_clues(request):
    return render(request, 'display_clues.html', context={})


