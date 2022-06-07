import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.core import serializers
from .models import Message



def list_users(request):
    template_name = 'chat/messenger.html'
    context = {
        'friends': User.objects.all()
    }
    return render(request, template_name, context)

def get_messages(request, friend_id):
    friend = get_object_or_404(User, id = friend_id)

    query =  Message.objects.filter(Q(_from=friend) | Q(to=friend)).values().reverse()

    queryset = [subquery for subquery in query]

    return JsonResponse({'data': queryset})


def send_message(request, message, friend_id):

    print(message, '<= message')

    friend = User.objects.get(id=friend_id)

    Message.objects.create(message=message, _from=request.user, to=friend)

    return JsonResponse({'data': { 'message': message }})
