# -*- coding: utf-8 -*-
import pub_goods.models as models
from django import forms
from pub_goods._builtin import Form
from crispy_forms.layout import HTML
from otree.common import Money, money_range

class ContributionForm(Form):

    class Meta:
        model = models.Player
        fields = ['contribution']

#    def my_field_error_message(self, value):
#        if not 0 <= value <= 10:
#            return 'Value is not in allowed range'

    def labels(self):
        return {'contribution': ''}

    def choices(self):
        return {'contribution': self.treatment.contribution_choices()}
