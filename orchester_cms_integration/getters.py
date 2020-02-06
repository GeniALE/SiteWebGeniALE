from django.db.models import Q
from orchester import ConnectorType

from teamModule.models import Member, MemberExtraInfo

EXTRA_VALUE_PREFIX = "extra_"


def get_slack_user(member: Member):
    return member.email


def get_g_drive_user(member: Member):
    return member.email


def get_trello_user(member: Member):
    q_filter = Q(member_id__exact=member.id) & Q(info_type__code=ConnectorType.TRELLO.value)
    extra_infos = MemberExtraInfo.objects.filter(q_filter).first()

    if extra_infos:
        return extra_infos.value
    else:
        return None


def get_github_user(member: Member):
    q_filter = Q(member_id__exact=member.id) & Q(info_type__code=ConnectorType.GITHUB.value)
    extra_infos = MemberExtraInfo.objects.filter(q_filter).first()

    if extra_infos:
        return extra_infos.value
    else:
        return None


MEMBER_CONNECTOR_FIELD_GETTERS = {
    ConnectorType.SLACK: get_slack_user,
    ConnectorType.GITHUB: get_github_user,
    ConnectorType.TRELLO: get_trello_user,
    ConnectorType.G_DRIVE: get_g_drive_user,
}

AVAILABLE_CONNECTORS = MEMBER_CONNECTOR_FIELD_GETTERS.keys()
