# -*- coding: utf-8 -*-
import weak_link.models as models
from django import forms
from weak_link._builtin import Form
from crispy_forms.layout import HTML
from otree.common import Money, money_range

class DecisionForm(Form):

    class Meta:
        model = models.Player
        fields = ['decision']
        widgets = {'decision': forms.RadioSelect()}

#     def my_field_error_message(self, value):
#         if not 0 <= value <= 10:
#             return 'Value is not in allowed range'

    def labels(self):
        return {'decision':'Allocation as percentage of upper boundary:'}

#     def order(self):
#         pass
