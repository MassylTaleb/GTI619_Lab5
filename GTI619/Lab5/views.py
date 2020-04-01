
from django.shortcuts import render, redirect
from . forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from .token import account_activation_token
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail


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
        if user is not None:
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            print(current_site)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            user_email = user.email
            recipients = [user_email]
            print(user_email)
            result = send_mail(
                subject,message,
                'massyltaleb@gmail.com',
              recipients)
            print(result)
            return render(request, 'confirmation_email.html')
        else:
            messages.info(request, f'account done not exit plz sign in')

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form, 'title': 'log in'})



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
    if request.user.username == 'admin':
        if request.method == 'POST':
            form = ParamsForm(request.POST)
            if form.is_valid():
                form.save()

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
