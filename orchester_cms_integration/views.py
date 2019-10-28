# -*- coding: utf-8 -*-
from datetime import datetime

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponseServerError
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
import json

from orchester_cms_integration.getters import EXTRA_VALUE_PREFIX
from teamModule.helpers import to_dict
from orchester_cms_integration.service import get_user_status_list
from teamModule.models import Member, MemberExtraInfoType
from orchester_cms_integration import service


def remove_duplicates(array, field):
  grouped_values = {getattr(val, field): val for val in array}
  return grouped_values.values()


@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
  template_name = 'orchester/list.html'

  def get_queryset(self):
    return Member.objects.all()

  def get_member_columns(self):
    opts = Member._meta
    return [{'data': field.name} for field in opts.concrete_fields]

  def get_member_column_names(self):
    opts = Member._meta
    return list(map(lambda x: x.name.capitalize().replace('_', ' '), opts.concrete_fields))

  def get_member_column_names(self):
    opts = Member._meta
    return list(map(lambda x: x.name.capitalize().replace('_', ' '), opts.concrete_fields))

  def get_extra_info_columns(self):
    return remove_duplicates(MemberExtraInfoType.objects.all(), 'code')

  def get_extra_info_type_columns(self, columns):
    return [{'data': EXTRA_VALUE_PREFIX + column.code} for column in columns]

  def get_extra_info_type_column_names(self, columns):
    return [column.code.capitalize() for column in columns]

  def get_flatten_members_list(self):
    members = Member.objects.prefetch_related(
      'memberextrainfo_set',
      'memberextrainfo_set__info_type'
    ).order_by("first_name")

    result = []
    for member in members:
      member_as_dict = to_dict(member)

      member_as_dict['formation'] = str(member.formation)

      # Convert datetime to dates
      member_as_dict['date_joined'] = member_as_dict['date_joined'].date()
      if 'date_left' in member_as_dict and isinstance(member_as_dict['date_left'], datetime):
        member_as_dict['date_left'] = member_as_dict['date_left'].date()

      for extra in member.memberextrainfo_set.all():
        member_as_dict[EXTRA_VALUE_PREFIX + extra.info_type.code] = extra.value
      result.append(member_as_dict)

    return result

  def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
    context = super().get_context_data(**kwargs)

    # Add in a QuerySet of all the books
    extra_columns = self.get_extra_info_columns()

    member_columns = self.get_extra_info_type_columns(extra_columns)
    member_column_names = self.get_extra_info_type_column_names(extra_columns)

    context['memberColumns'] = json.dumps(member_columns, cls=DjangoJSONEncoder)
    context['memberColumnNames'] = json.dumps(member_column_names, cls=DjangoJSONEncoder)
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
    context['service_info'] = json.dumps(get_user_status_list(member))
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
        'service_info': json.dumps(service_info)
      })

  except Exception as error:
    return render(request, 'orchester/edit.html', {
      'member': member,
      'error_message': str(error),
      'service_info': json.dumps(service_info)
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
        'service_info': json.dumps(service_info)
      })
  except Exception as error:
    return render(request, 'orchester/edit.html', {
      'member': member,
      'error_message': str(error),
      'service_info': json.dumps(service_info)
    })
