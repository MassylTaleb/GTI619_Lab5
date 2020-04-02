
from django.shortcuts import render, redirect
from . forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.models import User
import string
import random
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .token import account_activation_token
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail


gridCardCol = 5
gridCardRow = 5

class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.profile.email_confirmed = True
            user.save()
            login(request, user)
            messages.success(request, ('Your account have been confirmed.'))
            return redirect('home')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('home')


@login_required
def home(request):
    return render(request, 'home.html')

def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print("authenticated user : ", user)
        if user is not None:
            user.is_active = False
            card, created = GridCard.objects.get_or_create(user=user)
            user.gridcard = card
            user.save()
            current_site = get_current_site(request)
            print(current_site)
            subject = 'Activate Your MySite Account'
            card = generateGridCard(gridCardRow, gridCardCol)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            activateToken = account_activation_token.make_token(user)
            htmlmessage = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': uid,
                'token': activateToken,
                'gridcard': card,
                'gridRowRangeMinusOne': range(1, gridCardRow),
                'gridColRange': range(gridCardCol)
            })
            message = strip_tags(htmlmessage)
            user_email = user.email
            recipients = [user_email]

            combi = 3
            cols = random.sample(range(1, gridCardCol+1), combi)
            rows = random.sample(range(1, gridCardRow+1), combi)
            responses = {card[0][cols[0]] + card[rows[0]][0] : card[rows[0]][cols[0]]}
            for i in range(1, combi):
                responses[card[0][cols[i]] + card[rows[i]][0]] = card[rows[i]][cols[i]]

            print("responses", responses)
            iterResponseKeys = iter(responses)
            key1 = next(iterResponseKeys)
            key2 = next(iterResponseKeys)
            key3 = next(iterResponseKeys)
            iterResponseValues = iter(responses.values())
            val1 = next(iterResponseValues)
            val2 = next(iterResponseValues)
            val3 = next(iterResponseValues)

            # save responses in db
            new_gc = GridCard.objects.get(
                user_id = user.id
            )
            new_gc.key1 = key1
            new_gc.key2 = key2
            new_gc.key3 = key3
            new_gc.value1 = val1
            new_gc.value2 = val2
            new_gc.value3 = val3
            new_gc.active = True
            gcSaved = new_gc.save()
            print("gridcard saved in db? : ", gcSaved)
            user.gridcard = new_gc
            user.gridcard.save()

            print("In case you messed up and user cannot log in : ")
            print("http://"+current_site.domain+"/Lab5/activate/"+ uid + "/" + activateToken)
            result = send_mail(
                subject,message,
                'Do Not Reply <do_not_reply@domain.com>',
                recipients,
                html_message=htmlmessage)
            print(result)
            
            return render(request, 'gridcard.html', {'userId': uid, 'key1': key1, 'key2': key2, 'key3': key3})
            # return redirect('gridcard')
            # return render(request, 'confirmation_email.html')
        else:
            user = User.objects.get(username=username)
            print("try again", user)
            if user is not None:
                user.is_active = True
                card, created = GridCard.objects.get_or_create(user=user)
                user.gridcard = card
                user.save()
            messages.info(request, f'account done not exit plz sign in')
            return redirect('logout')

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form, 'title': 'log in'})



def signup(request):
    users = User.objects.all()
    for user in users:
        print(user.username)
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
    if request.user.username == 'admin':
        if request.method == 'POST':
            form = ParamsForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'parameters_changed.html')
        else:
            form = ParamsForm()
        return render(request, 'params.html', {'form': form})
    else:
        return render(request, 'notAllowed.html')

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

# 5x5 is suggested
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

def gridcard(request):
    if request.method == 'POST':
        form = GridCardForm(request.POST)
        if form.is_valid():
            uuid = request.POST.get('userId', None)
            try:
                uid = force_text(urlsafe_base64_decode(uuid))
                user = User.objects.get(pk=uid)
                response = GridCard.objects.get(user_id=user.id)
                value1 = request.POST.get('value1', None)
                value2 = request.POST.get('value2', None)
                value3 = request.POST.get('value3', None)
                user.is_active = True
                user.save()
                if value1 == response.value1 and value2 == response.value2 and value3 == response.value3:
                    print("gridcard validation success, logging user")
                    login(request, user)
                    return redirect('home')
                print("gridcard validation failed, try again")
            except(TypeError, ValueError, OverflowError, User.DoesNotExist):
                user = None
                return redirect('login')

            return redirect('logout')
    else:
        return redirect('login')
        
    return render(request, 'gridcard.html', {'form': form})