"""Models for the ``logging`` app."""
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
        # TODO
        return 'foo'


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
