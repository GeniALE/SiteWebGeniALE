from orchester import ConnectorManager, ConfigHelper, ConnectorType
from orchester_cms_integration.errors import BadParametersError
from orchester_cms_integration.getters import MEMBER_CONNECTOR_FIELD_GETTERS, AVAILABLE_CONNECTORS

config = ConfigHelper.get_config_data()
connector_manager = ConnectorManager(config)


def do_action(action_name, connector_name, member):
  connector_type = connector_name if type(connector_name) is ConnectorType else ConnectorType(connector_name)
  getter = MEMBER_CONNECTOR_FIELD_GETTERS.get(connector_type)
  service_user_id = getter(member)

  if not service_user_id:
    raise BadParametersError("The required field for {} is missing in the member informations".format(connector_type))

  if action_name == 'register':
    return connector_manager.add_to_group(connector_type, service_user_id)
  elif action_name == 'unregister':
    return connector_manager.remove_from_group(connector_type, service_user_id)
  elif action_name == 'check':
    return connector_manager.is_registered_to_group(connector_type, service_user_id)
  else:
    raise BadParametersError("Unsupported operation {}".format(action_name))


def get_user_status_list(member):
  service_info = []

  for connector_type in AVAILABLE_CONNECTORS:
    username_getter = MEMBER_CONNECTOR_FIELD_GETTERS.get(connector_type)

    username = 'N/A'
    try:
      is_active = do_action('check', connector_type, member)
      username = username_getter(member)
    except:
      is_active = False
    service_info.append({
      'username': username,
      'name': connector_type.value,
      'displayName': connector_type.name,
      'status': is_active
    })
  return service_info
