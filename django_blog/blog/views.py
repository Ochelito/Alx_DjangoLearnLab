from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, ProfileForm, UserEditForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['welcome_message'] = "Welcome to the Blog!"
        return context

class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """if the form is valid, save the user and log them in."""
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)
  

class ProfileView(LoginRequiredMixin, View):
    template_name = 'profile.html'

    def get(self, request):
        user_form = UserEditForm(instance=request.user)
        # Create a ProfileForm instance with the user's profile 
        profile_form = ProfileForm(instance=request.user.profile)
        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form
        })

    def post(self, request):
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, 
            request.FILES, 
            instance=request.user.profile
        )
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile') # Redirect to the profile page after saving  
        
        # If the forms are not valid, render the profile page with the forms
        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form
        })