from django.contrib.auth.models import User
from django.views.generic import DetailView, View, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseBadRequest
from followers.models import Follower
from feed.models import Post
from .models import Profile
from .forms import UpdateProfileForm

class ProfileDetailView(DetailView):
    http_method_names = ['get']
    template_name = 'profiles/detail.html'
    model = User
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        user = self.get_object()
        userid = user.id
        context = super().get_context_data(**kwargs)
        context['total_posts'] = Post.objects.filter(author=user).count()
        context['total_followers'] = Follower.objects.filter(following=userid).count()
        if self.request.user.is_authenticated:
            context['you_follow'] = Follower.objects.filter(following=user, followed_by=self.request.user).exists()
        return context

class FollowView(LoginRequiredMixin, View):
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        data = request.POST.dict()

        if "action" not in data or "username" not in data:
            return HttpResponseBadRequest("Missing data")

        try:
            other_user = User.objects.get(username=data["username"])
        except User.DoesNotExist:
            return HttpResponseBadRequest("Missing User")

        if data['action'] == "follow":
            follower, created = Follower.objects.get_or_create(
                followed_by=request.user,
                following=other_user,
            )
        else:
            try:
                follower = Follower.objects.get(
                    followed_by=request.user,
                    following=other_user,
                )
            except Follower.DoesNotExist:
                follower = None

            if follower:
                follower.delete()
        
        return JsonResponse({
            "success": True,
            "wording": "Unfollow" if data['action'] == "follow" else "Follow"
        })

class UpdateProfileView(LoginRequiredMixin, FormView):
    http_method_names =['get', 'post']
    template_name = 'profiles/update.html'
    form_class = UpdateProfileForm
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["user"] = self.request.user
        return context

    def form_valid(self, form):
        new_object = Profile.objects.update_or_create(
            FirstName = form.cleaned_data['First_Name'],
            LastName = form.cleaned_data['Last_Name'],
            Username = form.cleaned_data['Username'],
            Image = form.cleaned_data['image'],
            Password = form.cleaned_data['Password'],
        )
        if form.is_valid():
            new_object.save()
        return super().form_valid(form)





