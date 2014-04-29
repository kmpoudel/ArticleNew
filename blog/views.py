from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView, ListView, DetailView
from blog.models import Post
from blog.forms import PostForm

# Create your views here.


def user_login(request):
	c = {}
	c.update(csrf(request))
	if request.user.is_authenticated():
		return render_to_response('mainblog.html',c)
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
    return HttpResponseRedirect('/')
	#	return render_to_response('mainblog.html', {'user': request.user})
                                                   


def invalid_login(request):
		return render_to_response('invalid_login.html')


def logout(request):
	auth.logout(request)
	return  HttpResponseRedirect('/')

def register(request):
    return render_to_response('registeruser.html')

class AddPost(CreateView):
    template_name='create_post.html'
    model=Post 

    # def get_template_name(self, request):
    #     self.template_name='create_post.html'

    def get(self, request, *args, **kwargs):
        context={'postform': PostForm()}
        return render(request,self.template_name,context)
        

    def post(self, request, *args, **kwargs):
        create_post = PostForm(request.POST)
        if create_post.is_valid():
            print "valid"
            create_post.save()


class ListPost(ListView):
    template_name = 'mainblog.html'
    model = Post
    paginate_by = 3

    def dispatch(self, request, *args, **kwargs):
        return super(ListPost, self).dispatch(request, *args, **kwargs)



class DetailPost(DetailView):
    template_name = 'fullpost.html'
    model = Post

    def dispatch(self, request, *args, **kwargs):
        return super(DetailPost, self).dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        self.pk=pk
        return super(DetailPost,self).get(request,pk)

    def get_context_data(self, **kwargs):
        context = super(DetailPost, self).get_context_data(**kwargs)
        context['detailpost'] = Post.objects.get(id=self.pk)
        print context
        return context

    def get_success_url(self):
        return reverse('detailpost') 





    
    













