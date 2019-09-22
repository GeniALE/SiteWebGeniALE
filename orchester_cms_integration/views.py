# -*- coding: utf-8 -*-
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponseServerError
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
import json

from helpers import to_dict
from orchester_cms_integration.service import get_user_status_list
from teamModule.models import Member, MemberExtraInfoType
from orchester_cms_integration import service


@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
  template_name = 'orchester/list.html'

  def get_queryset(self):
    return Member.objects.all()

  def get_member_layout(self):
    opts = Member._meta
    return [{'field': field.name} for field in opts.concrete_fields]

  def get_extra_info_type_layout(self):
    extra_info_types = set(map(lambda x: x.code,MemberExtraInfoType.objects.all()))
    return [{'field': code} for code in extra_info_types]

  def get_flatten_members_list(self):
    members = Member.objects.prefetch_related(
      'memberextrainfo_set',
      'memberextrainfo_set__info_type'
    ).order_by("first_name")

    result = []
    for member in members:
      member_as_dict = to_dict(member)
      for extra in member.memberextrainfo_set.all():
        member_as_dict[extra.info_type.code] = extra.value
      result.append(member_as_dict)

    return result

  def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
    context = super().get_context_data(**kwargs)
    # Add in a QuerySet of all the books
    member_layout = self.get_member_layout() + self.get_extra_info_type_layout()

    context['memberColumnsDef'] = json.dumps(member_layout, cls=DjangoJSONEncoder)
    context['memberList'] = json.dumps(self.get_flatten_members_list(), cls=DjangoJSONEncoder)
    return context


@method_decorator(login_required, name='dispatch')
class DetailView(generic.DetailView):
  model = Member
  queryset = Member.objects.all()
  template_name = 'orchester/edit.html'
  context_object_name = 'member'

  def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
    context = super().get_context_data(**kwargs)
    # Add in a QuerySet of all the books
    member = context['member']
    context['service_info'] = get_user_status_list(member)
    return context


@login_required
def unregister(request, member_id):
  member = get_object_or_404(Member, pk=member_id)
  service_info = get_user_status_list(member)

  connector_name = request.POST['connector_name']

  try:
    result = service.do_action('unregister', connector_name, member)
    if result:
      return HttpResponseRedirect(reverse('orchester:detail', args=(member.id,)))
    else:
      return render(request, 'orchester/edit.html', {
        'member': member,
        'error_message': "Failed to unregister the user!",
        'service_info': service_info
      })

  except Exception as error:
    return render(request, 'orchester/edit.html', {
      'member': member,
      'error_message': str(error),
      'service_info': service_info
    })


@login_required
def register(request, member_id):
  member = get_object_or_404(Member, pk=member_id)
  service_info = get_user_status_list(member)

  connector_name = request.POST['connector_name']

  try:
    result = service.do_action('register', connector_name, member)
    if result:
      return HttpResponseRedirect(reverse('orchester:detail', args=(member.id,)))
    else:
      return render(request, 'orchester/edit.html', {
        'member': member,
        'error_message': "Failed to register the user",
        'service_info': service_info
      })
  except Exception as error:
    return render(request, 'orchester/edit.html', {
      'member': member,
      'error_message': str(error),
      'service_info': service_info
    })
