from ast import Dict
import json
from typing import Any
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View, TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.core import serializers
from requests import request

from core.utils import generate_text
from .models import GroupMessage, Message, Group



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

    friend = User.objects.get(id=friend_id)

    Message.objects.create(message=message, _from=request.user, to=friend)

    return JsonResponse({'data': { 'message': message }})


# --------------------------------- [ Group ] -----------------------------------
class GroupView(ListView):
    template_name = "chat/groups.html"
    context_object_name = 'groups'

    def get_queryset(self):
        return Group.objects.filter(member=self.request.user)

class GroupCreation(View):
    def post(self, *args, **kwargs):

        title = self.request.POST.get('title', None)

        random_text = generate_text(5)

        slug = f'{title}-{random_text}'

        group = Group.objects.create(
            title=title,
            owner=self.request.user,
            slug=slug,
        )

        group.member.add(self.request.user)

        return redirect('chat:groups')

def get_group_messages(request, group_id):

    queryset = GroupMessage.objects.filter(group_id=group_id).values()

    messages = [query for query in queryset]

    return JsonResponse({'data': messages })


def send_group_message(request, message, group_id):

    group = Group.objects.get(id=group_id)

    GroupMessage.objects.create(group=group, message=message, _from=request.user)

    return JsonResponse({'data': { 'message': message }})


def join_group(request, group_slug):

    group = get_object_or_404(Group, slug=group_slug)

    group.member.add(request.user)

    return JsonResponse({'data': 'added successfully'})


