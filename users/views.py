""" Users views. """

from users.models import Profile
from users.forms import ProfileForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#Model
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

@login_required
def update_profile(request):
    """ Update a user's profile view. """
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            print(form.cleaned_data)

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            return redirect('update_profile')
    else:
        form = ProfileForm()
    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        })

def login_view(request):
    """ Login view. """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password =password)

        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html',{'error': 'Invalid username and password'})

    return render(request, 'users/login.html')


def signup(request):
    """ Sign up view. """
    #import pdb; pdb.set_trace()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['passwd']
        passwordC = request.POST['passwd_confirmation']

        if password != passwordC :
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})


        # EMAIL VALIDATION
        email = request.POST['email']
        u = User.objects.filter(email=email)
        if u:
            error = f'There is another account using {email}'
            return render(request, 'users/signup.html', {'error': error})

        try:
            user = User.objects.create_user(username=username, password=password)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
        except IntegrityError as ie:
            return render(request, 'users/signup.html', {'error': 'Username is already in use'})

        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')

@login_required
def logout_view(request):
    """ Logout users. """
    logout(request)
    return redirect("login")