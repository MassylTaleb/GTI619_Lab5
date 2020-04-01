
from django.shortcuts import render, redirect
from . forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.models import User
import string
import random



@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def activate_token(request, uuid, token):
    try:
        uid = force_text(urlsafe_base64_decode(uuid))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and activate_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'activation_invalid.html')

@login_required
def params(request):
    if request.method == 'POST':
        form = ParamsForm(request.POST)

    else:
        form = ParamsForm()
    return render(request, 'params.html', {'form': form})

@login_required
def getAllCR(request):
    currentUser = request.user.id
    currentProfile = Profile.objects.get(user_id = currentUser)
    print(currentProfile.role)
    if currentProfile.role != 'CA':
        cr_list = User.objects.filter(profile__role='CR')
        return render(request, 'allCR.html', {'cr_user_list': cr_list})
    else:
        return render(request, 'notAllowed.html')



@login_required
def getAllCA(request):
    currentUser = request.user.id
    currentProfile = Profile.objects.get(user_id=currentUser)
    if currentProfile.role != 'CR':
        ca_list = User.objects.filter(profile__role='CA')
        return render(request, 'allCA.html', {'ca_user_list': ca_list})
    else:
        return render(request, 'notAllowed.html')


@login_required
def gridcard(request):
    currentUserId = request.user.id
    if request.method == 'POST':
        form = GridCardForm(request.POST)
        if form.is_valid():
            # TODO : validate grid card here
            print(form)
            return redirect('home')
    else:

        def generateGridCard(row, col):
            # add 1 for row header and column header
            row += 1 
            col += 1
            columnHeader = random.sample(range(1, col+1), col)
            columnHeader = list(map(str, columnHeader)) # convert int array to str array
            columnHeader[0] = ' ' #first top left cell is empty
            rowHeader = random.sample(string.ascii_uppercase[:row], col)
            possibilities = (row -1) * (col -1)
            arrRandomAlpha = random.sample(string.ascii_uppercase[:26], 26) if possibilities <= 26 else random.choices(string.ascii_uppercase[:26], k=possibilities)

            card = [[' ' for x in range(col)] for y in range(row)]
            card[0] = columnHeader
            randomAlphaIndex = 0
            for rowIndex in range(1, row):
                card[rowIndex][0] = rowHeader[rowIndex]
                for colIndex in range(1, col):
                    card[rowIndex][colIndex] = arrRandomAlpha[randomAlphaIndex]
                    randomAlphaIndex += 1
            
            # print gridcard
            for x in range(row):
                print(card[x])

            return card

        col = 5
        row = 5
        # TODO : check if user already has its gridcard
        card = generateGridCard(row, col) # 5x5 is suggested
        # TODO : send gridcard via email

        combi = 3
        cols = random.sample(range(1, col+1), combi)
        rows = random.sample(range(1, row+1), combi)
        response = {card[0][cols[0]] + card[rows[0]][0] : card[rows[0]][cols[0]]}
        for i in range(1, combi):
            response[card[0][cols[i]] + card[rows[i]][0]] = card[rows[i]][cols[i]]

        print("response", response)

        form = GridCardForm()
        print(form)
        
    return render(request, 'gridcard.html', {'form': form})