from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from projectapp.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets
from rest_framework import permissions
from projectapp.serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from projectapp.forms import *


class HomeView(ListView):
    model = Video
    template_name = "projectapp/index.html"
    ordering = ['-id']

class VideoDetailView(DetailView):
    model = Video
    template_name = "projectapp/video_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(VideoDetailView, self).get_context_data(**kwargs)
        stuff = get_object_or_404(Video, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes
        return context

class AddVideoView(CreateView):
    model = Video
    template_name = "projectapp/add_video.html"
    fields = ["title", "preview", "video", "user", "description"]


def LikeView(request, pk):
    video = get_object_or_404(Video, id=request.POST.get('video_id'))
    video.likes.add(request.user)
    return HttpResponseRedirect(reverse('video-detail', args=[str(pk)]))

class AddCommentView(CreateView):
    model = Comment
    template_name = "projectapp/add_comment.html"
    fields = "__all__"

def search_videos(request):
    if request.method == "POST":
        searched = request.POST['searched']
        videos = Video.objects.filter(title__contains=searched)
        return render(request, 'projectapp/search_videos.html', {"searched": searched, "videos": videos})
    else:
        return render(request, 'projectapp/search_videos.html', {})


class BanUserView(UpdateView):
    model = Profile
    template_name = "projectapp/ban_user.html"
    fields = ["user", "is_ban"]


class UserListView(ListView):
    model = Profile
    template_name = "projectapp/user_list.html"


class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class VideoViewset(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def destroy(self, request, pk, format=None):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentViewset(viewsets.ModelViewSet):
   queryset = Comment.objects.all()
   serializer_class = CommentSerializer


def form(request):
    form = EmailForm()
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = 'Your account was succesfully done!'
            message = 'Now you can Became a Famous Person'
            recipient = form.cleaned_data.get('email')
            send_mail(subject, 
              message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Success!')
            return redirect('email')
    return render(request, 'projectapp/email.html', {'form': form})