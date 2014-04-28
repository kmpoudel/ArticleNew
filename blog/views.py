from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

# Create your views here.


def user_login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html',c)

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/blog/loggedin')
	else:
		return HttpResponseRedirect('/blog/invalid')

def loggedin(request):
		return render_to_response('loggedin.html', {'full_name': request.user.username})

def invalid_login(request):
		return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('loggedout.html')





















































'''def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)
    #print context

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                #return HttpResponseRedirect('/latest/')
                
                return render_to_response("mainpage.html", Context(request, {'user': user}))
                #return render_to_response('mainpage.html',{'user':user})
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        
        return render_to_response('login.html', {}, context)

def mainpage(request):
	#user = User.objects.get(username= request.user.username)
	return render_to_response('mainpage.html')

	#return render_to_response('mainpage.html',{'user':User})'''