from django.shortcuts import render

@login_required
def view_foo(request):
    user_profile = request.user.get_profile()
    url = user_profile.url