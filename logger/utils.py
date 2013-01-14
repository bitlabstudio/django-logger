"""Utilities for the ``logger`` app."""
from logger.models import (
    Action,
    ActionParameter,
    ActionParameterType,
    Log,
)


class Logger(object):
    """The class that holds all the methods needed for logging."""
    def create_log(self, action_name, param_dict):
        """
        Creates a ``Log`` object based on the above values.

        :action_name: String representing the action type. E.g. "payment"
        :param_dict: A dictionary in the format of
            {'parameter_type1': 'value1', ... } defining the values of the
            action to log.

        """
        # retrieve the action type
        action = self.get_action(action_name)

        # create a new log
        log = Log(action=action)
        log.save()

        # assign the paremeters to the log
        for (param, value) in param_dict.iteritems():
            log.action_parameter.add(self.get_action_parameter(param, value))

        return log

    def get_action(self, action_name):
        """Returns the ``Action`` object matching the action_name argument."""
        try:
            action = Action.objects.get(name=action_name)
        except Action.DoesNotExist:
            action = Action(name=action_name)
            action.save()
        return action

    def get_action_parameter(self, param, value):
        """Returns an ``ActionParameter`` object."""
        # create  action parameter
        action_parameter = ActionParameter(
            parameter_type=self.get_parameter_type(param))
        action_parameter.set_value(value)
        action_parameter.save()
        return action_parameter

    def get_parameter_type(self, param):
        """Retrieves an ``ActionParameterType`` object."""
        # retrieve ActionParameterType. If it doesn't exist, create it
        try:
            parameter_type = ActionParameterType.objects.get(name=param)
        except ActionParameterType.DoesNotExist:
            parameter_type = ActionParameterType(name=param)
            parameter_type.save()
        return parameter_type
