"""Utilities for the ``logger`` app."""
from logger.models import (
    Action,
    ActionParameter,
    ActionParameterType,
    Log,
)


class Logger(object):
    """The class that holds all the methods needed for logging."""
    def create_log(self, action_name, parameter_type_names, values):
        """
        Creates a ``Log`` object based on the above values.

        :action_name: String representing the action type. E.g. "payment"
        :parameter_type_name: A list of strings or single string
            representing the types of stored values.
            E.g. ["amount",  "user"] or just "has used this"
        :value: A list of values or a single value that is stored.
            Each item in the list or the value itself can be either of the
            following types: string, integer, date or datetime, decimal,
            boolean or django model instance.

        """
        # retrieve the action type
        action = self.get_action(action_name)
        # retrieve the parameter list
        action_parameters = self.get_action_parameters(
            parameter_type_names, values)

        # create a new log
        log = Log(action=action)
        log.save()
        # assign the paremeters to the log
        for parameter in action_parameters:
            log.action_parameter.add(parameter)

        return log

    def get_action(self, action_name):
        """Returns the ``Action`` object matching the action_name argument."""
        try:
            action = Action.objects.get(name=action_name)
        except Action.DoesNotExist:
            action = Action(name=action_name)
            action.save()
        return action

    def get_action_parameters(self, parameter_type_names, values):
        """Returns a list of ``ActionParameter`` objects."""
        # if no lists were given, turn them into a list to make them iterable
        if not isinstance(parameter_type_names, list):
            parameter_type_name_list = [parameter_type_names]
        else:
            parameter_type_name_list = parameter_type_names
        if not isinstance(values,  list):
            value_list = [values]
        else:
            value_list = values

        # if the list lengths differ, raise an IndexError
        if len(parameter_type_name_list) != len(value_list):
            raise IndexError('The length of the given lists does not match.')

        # iterate over parameter_type_names and create action parameters
        parameter_type_list = self.get_parameter_types(
            parameter_type_name_list, value_list)

        # create list of action parameters
        action_parameter_list = []
        for (counter, parameter_type) in enumerate(parameter_type_list):
            action_parameter = ActionParameter(parameter_type=parameter_type)
            action_parameter.set_value(value_list[counter])
            action_parameter.save()
            action_parameter_list.append(action_parameter)
        return action_parameter_list

    def get_parameter_types(self, parameter_type_name_list, value_list):
        """Retrieves a list of ``ActionParameterType`` objects."""
        parameter_type_list = []
        for parameter_type_name in parameter_type_name_list:
            # retrieve ActionParameterType. If it doesn't exist, create it
            # and append it to the list
            try:
                parameter_type = ActionParameterType.objects.get(
                    name=parameter_type_name)
            except ActionParameterType.DoesNotExist:
                parameter_type = ActionParameterType(
                    name=parameter_type_name)
                parameter_type.save()
            parameter_type_list.append(parameter_type)
        return parameter_type_list
