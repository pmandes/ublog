# -*- coding: utf-8 -*-
import datetime

from ublog.posts.models import Post, Profile

from django.contrib import auth
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404

# widok główny
def index(request):
    latest_post_list = Post.objects.all().order_by('-pub_date')[:10]

    return render_to_response('posts/index.html', {'latest_post_list': latest_post_list}, context_instance=RequestContext(request))

# pulpit użytkownika
def dashboard(request):
    latest_post_list = Post.objects.all().order_by('-pub_date')[:10]

    return render_to_response('posts/index.html', {'latest_post_list': latest_post_list}, context_instance=RequestContext(request))

# pobranie posta
def get_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404

    return render_to_response('posts/post.html', {'post': post}, context_instance=RequestContext(request))

# wysłanie posta
def add_post(request):
	content = request.POST['content']
	author = Profile.objects.get(id=1)
	post = Post(author=author, content=content, pub_date=datetime.datetime.now())
	post.save()

	return HttpResponseRedirect(reverse('ublog.posts.views.index'))

# podgląd profilu
def profile(request):
    user_id = 0

    return render_to_response('posts/profile.html', {'user_id': user_id}, context_instance=RequestContext(request))

# logowanie
def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('ublog.posts.views.dashboard'))
    else:
        return HttpResponseRedirect(reverse('ublog.posts.views.index'))

# wylogowanie
def logout(request):
    auth.logout(request)

    return HttpResponseRedirect(reverse('ublog.posts.views.index'))

