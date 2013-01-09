"""Custom admin sites for the models of the ``logger`` app."""
from django.contrib import admin

from logger.models import (
    Action,
    ActionParameter,
    ActionParameterType,
    Log,
)


class ActionAndActionParameterTypeAdmin(admin.ModelAdmin):
    """
    Custom admin for the ``Action`` and the ``ActionParameterType`` model.

    """
    search_fields = ['name', ]
    list_filter = ('name', )


class ActionParameterAdmin(admin.ModelAdmin):
    """Custom admin for the ``ActionParameter`` model."""
    list_display = ('parameter_type', 'parameter_value')
    search_fields = ['parameter_type__name', ]
    list_filter = ('parameter_type__name', )

    def parameter_value(self, obj):
        return obj.get_value()


class LogAdmin(admin.ModelAdmin):
    """Custom admin for the ``Log`` model."""
    list_display = ('creation_time', '__unicode__')
    search_fields = ['action__name', ]
    list_filter = ('action__name', )


admin.site.register(Action, ActionAndActionParameterTypeAdmin)
admin.site.register(ActionParameter, ActionParameterAdmin)
admin.site.register(ActionParameterType, ActionAndActionParameterTypeAdmin)
admin.site.register(Log, LogAdmin)
