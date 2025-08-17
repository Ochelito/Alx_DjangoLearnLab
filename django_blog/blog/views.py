from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from .forms import CustomUserCreationForm, UserUpdateForm, ProfileForm, UserEditForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import TemplateView, UpdateView
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView

User = get_user_model()
# Create your views here.
class HomeView(TemplateView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['welcome_message'] = "Welcome to the Blog!"
        return context

class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """if the form is valid, save the user and log them in."""
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Account created successfully. Welcome")
        return redirect(self.success_url)
  
class CustomLoginView(LoginView):
    template_name = "blog/login.html"

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/profile.html'

    def get(self, request, *args, **kwargs):
        user_form = UserEditForm(instance=request.user)
        # Create a ProfileForm instance with the user's profile 
        profile_form = ProfileForm(instance=request.user.profile)
        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form
        })

    def post(self, request, *args, **kwargs):
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, 
            request.FILES, 
            instance=request.user.profile
        )
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile Updated successfully!")
            return redirect('profile') # Redirect to the profile page after saving  
        
        # If the forms are not valid, render the profile page with the forms
        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form
        })