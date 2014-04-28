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
	if request.user.is_authenticated():
		return render_to_response('loggedin.html',c)
	else:
		return render_to_response('login.html',c)	

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/blog/loggedin')
	else:
		return HttpResponseRedirect('/blog/logout')

def loggedin(request):
		return render_to_response('loggedin.html', {'full_name': request.user.username})

def invalid_login(request):
		return render_to_response('invalid_login.html')

@login_required
def logout(request):
	auth.logout(request)
	return render_to_response('loggedout.html')

def register(request):
    return render_to_response('registeruser.html')













