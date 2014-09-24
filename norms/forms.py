# -*- coding: utf-8 -*-
import norms.models as models
from django import forms
from norms._builtin import Form
from crispy_forms.layout import HTML
from otree.common import Money, money_range

class QuestionForm(Form):

    class Meta:
        model = models.Player
        fields = ['rating']
        widgets = {'rating': forms.RadioSelect()}

#     def my_field_error_message(self, value):
#         if not 0 <= value <= 10:
#             return 'Value is not in allowed range'

    def labels(self):
        return {'rating':''}

#     def order(self):
#         pass

