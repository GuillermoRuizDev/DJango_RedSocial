""" Codegram middleware catalog. """

#django
#from django.http import response
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """ Profile completion middleware

        Ensure every user that is interacting with the platform
        have their profile picture and biography.
    """
    def __init__(self, get_response):
        """ Middleware initialization. """
        self.get_response = get_response

    def __call__(self, request):
        """ Code to be executed for each request before the view is called """
        if not request.user.is_anonymous:
            profile = request.user.profile
            if not profile.picture or not profile.biography:
                if request.path not in [reverse('update_profile'),reverse('logout')]:
                    return redirect('update_profile')

        response = self.get_response(request)
        return response


"""     def __delattr__(self, request):
        if not request.user.is_anonymous:
        try:
            profile = request.user.profile
            if not profile.picture or not profile.biography:
                if request.path != reverse('update_profile'):
                    return redirect('update_profile')
        except:
            print('no profile')
            logout(request)
            return render(request, 'users/login.html', {'error': 'User has no profile'})

        response = self.get_response(request)
        return response """