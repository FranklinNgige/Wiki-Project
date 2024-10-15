# user_portal/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def user_portal(request):
    return render(request, 'user_portal/user_portal.html')  

