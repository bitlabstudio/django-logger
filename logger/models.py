"""Models for the ``logger`` app."""
import datetime
import decimal

from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Action(models.Model):
    """Defines the type of action performed. E.g. payment, url call etc."""
    name = models.CharField(
        max_length=64,
        verbose_name=_('Action name'),
    )

    def __unicode__(self):
        return self.name


class ActionParameterType(models.Model):
    """
    Defines the type of parameter the ``ActionParameter`` model stores.

    e.g. "amount" for an ``Action`` called "payment sent".

    """
    name = models.CharField(
        max_length=64,
        verbose_name=_('Action parameter type'),
    )

    def __unicode__(self):
        return self.name


class ActionParameter(models.Model):
    """
    A value belonging to the action.

    E.g. 34.10 for an ``ActionParameter`` called "amount".

    :parameter_type: The type of parameter this amount belongs to.
    :value_char: Character value for this parameter.
    :value_int: Integer value for this parameter.
    :value_time: Datetime value for this parameter.
    :value_decimal: Decimal value for this parameter.
    :value_bool: Boolean value for this parameter.
    :value_object: Object value for this parameter.
    :content_type: FK to ContentType of the related object.
    :object_id: Integer representing the id of the related object.

    """
    parameter_type = models.ForeignKey(
        'ActionParameterType',
        verbose_name=_('Action parameter type'),
        related_name='action_parameters',
    )

    value_char = models.CharField(
        max_length=128,
        verbose_name=_('Char value'),
        blank=True, null=True,
    )

    value_int = models.CharField(
        max_length=64,
        verbose_name=_('Integer value'),
        blank=True, null=True,
    )

    value_time = models.DateTimeField(
        max_length=64,
        verbose_name=_('Time and date value'),
        blank=True, null=True,
    )

    value_decimal = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_('Decimal value'),
        blank=True, null=True,
    )

    value_bool = models.NullBooleanField(
        verbose_name=_('Boolean value'),
        blank=True, null=True,
    )

    content_type = models.ForeignKey(
        ContentType,
        verbose_name=_('Content type'),
        blank=True, null=True,
    )

    object_id = models.PositiveIntegerField(
        verbose_name=_('Object id'),
        blank=True, null=True,
    )

    value_object = generic.GenericForeignKey(
        'content_type',
        'object_id',
    )

    def __unicode__(self):
        return '{0} - {1}'.format(self.parameter_type, self.get_value())

    def get_value(self):
        """Iterates over value fields and returns the one not being None."""
        for field in self._meta.get_all_field_names():
            if field.startswith('value_'):
                value = getattr(self, field)
                if value is not None:
                    return value
        # this is not recognized as fields so it is added manually
        if self.value_object is not None:
            return self.value_object
        return None

    def set_value(self, value):
        """
        Goes through all possible types and stores the value to the correct
        field.

        """
        value_type = type(value)
        if value_type == int:
            self.value_int = str(value)
        elif value_type == str:
            self.value_char = value
        elif value_type == bool:
            self.value_bool = value
        elif value_type == datetime.datetime:
            self.value_time = value
        elif value_type == decimal.Decimal:
            self.value_decimal = value
        elif hasattr(value, 'pk'):
            self.value_object = value
        return self


class Log(models.Model):
    """
    This contains the information from the specific log entry.

    :creation_time: The date and time of the entry.
    :action: Foreign key to the action taken place.
    :action_parameter: ManyToMany to the information values of the action.

    """
    creation_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Creation time'),
    )

    action = models.ForeignKey(
        'Action',
        verbose_name=_('Action'),
    )

    action_parameter = models.ManyToManyField(
        'ActionParameter',
        verbose_name=_('action parameter'),
    )

    def __unicode__(self):
        parameters = []
        for parameter in self.action_parameter.all():
            parameters.append(parameter.__unicode__())
        return '{0} - {1}'.format(
            self.action,
            parameters,
        )
