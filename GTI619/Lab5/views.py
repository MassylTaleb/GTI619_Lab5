
from django.shortcuts import render, redirect
from . forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.models import User



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
    if request.method == 'POST':
        form = GridCardForm(request.POST)
        if form.is_valid():
            # TODO : validate grid card here
            return redirect('home')
    else:
        form = GridCardForm()
    return render(request, 'gridcard.html', {'form': form})