# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponseServerError
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from orchester_cms_integration.service import get_user_status_list
from teamModule.models import Member
from orchester_cms_integration import service


@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
  template_name = 'orchester/list.html'

  def get_queryset(self):
    return Member.objects.all()


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
