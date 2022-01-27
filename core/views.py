from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProfileForm
from .models import Video, Profile, Video, Channel


class Home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/profile/')
        return render(request, 'empty.html')


@method_decorator(login_required)
class Channel(View):

    def get(self, request, *args, **kwargs):

        channels = request.user.profiles.all()

        print(channels)

        return render(request, 'empty.html', {
            'channels': channels
        })


@method_decorator(login_required)
class Subscriptions(View):

    def get(self, request, profile_id, *args, **kwargs):

        profile = Profile.objects.get(uuid=profile_id)

        subscription = Profile.objects.get(profile.subscriptions)

        print(subscription)

        return render(request, 'empty.html', {
            'subscription': subscription
        })


@method_decorator(login_required)
class ProfileCreate(View):
    def get(self, request, *args, **kwargs):
        form = ProfileForm()

        return render(request, 'empty.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None)

        if form.is_valid():
            print(form.cleaned_data)
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                return redirect(f'/watch/{profile.uuid}')

        return render(request, 'empty.html', {
            'form': form
        })


@method_decorator(login_required)
class Watch(View):
    def get(self, request, video_id, *args, **kwargs):
        try:
            profile = Profile.objects.get(uuid=video_id)

            videos = Video.objects.filter(age_limit=profile.age_limit)

            try:
                showcase = videos[0]
            except:
                showcase = None

            if profile not in request.user.profiles.all():
                return redirect(to='core:Channel')
            return render(request, 'empty.html', {
                'vides': videos,
                'showcase': showcase
            })
        except Profile.DoesNotExist:
            return redirect(to='core:Channel')


@method_decorator(login_required)
class VideoDescription(View):
    def get(self, request, video_id, *args, **kwargs):
        try:

            video = Video.objects.get(uuid=video_id)

            return render(request, 'empty.html', {
                'video': video
            })
        except Video.DoesNotExist:
            return redirect('core:channel')


@method_decorator(login_required)
class ShowVideo(View):
    def get(self, request, video_id, *args, **kwargs):
        try:

            video = Video.objects.get(uuid=video_id)

            video = video.videos.values()

            return render(request, 'empty.html', {
                'video': list(video)
            })
        except Video.DoesNotExist:
            return redirect('core:channel')
