from typing import AnyStr


class BadParametersError(Exception):
  def __init__(self, error_description: AnyStr = "Bad parameters supplied"):
    # Call the base class constructor with the parameters it needs
    super(BadParametersError, self).__init__(error_description)


class NotFoundError(Exception):
  def __init__(self, error_description: AnyStr = "Not found"):
    # Call the base class constructor with the parameters it needs
    super(NotFoundError, self).__init__(error_description)
