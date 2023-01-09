from rest_framework import serializers

from .models import Loan


class FieldMixin(object):
    def get_field_names(self, *args, **kwargs):
        field_names = self.context.get("fields", None)
        if field_names:
            return field_names

        return super(FieldMixin, self).get_field_names(*args, **kwargs)


class LoanSerializer(FieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"
