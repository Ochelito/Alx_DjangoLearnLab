Endpoints:

GET/POST /register/ — user signup

GET/POST /login/ — login (Django built-in)

GET /logout/ — logout (Django built-in; redirects to login)

GET/POST /profile/ — view & edit user and profile (auth required)

Forms:

CustomUserCreationForm for signup (+email)

UserUpdateForm & ProfileForm for profile edit

Redirects:

LOGIN_REDIRECT_URL = "profile"

LOGOUT_REDIRECT_URL = "login"