# -*- coding: utf-8 -*-
import otree.views
import otree.views.concrete
import weak_link.forms as forms
from weak_link._builtin import Page, MatchWaitPage, SubsessionWaitPage
from otree.common import Money, money_range

# def variables_for_all_templates(self):
#     return {
#         # example:
#         #'my_field': self.player.my_field,
#     }

class Decision(Page):

#     def participate_condition(self):
#         return True

    template_name = 'weak_link/Decision.html'

    def get_form_class(self):
        return forms.DecisionForm
        

class ResultsWaitPage(SubsessionWaitPage):

    def after_all_players_arrive(self):
        for p in self.subsession.players:
        	p.subsession.minimum()
        	p.subsession.set_payoffs()
    
    def body_text(self):
    	return "Waiting for other players to decide."

class Results(Page):

    template_name = 'weak_link/Results.html'
    
    def variables_for_template(self):
    	return{
    		'decision': self.player.get_decision_display,
    		'payoff': self.player.payoff,
    		'min_value': self.subsession.get_min_value_display
    	}

def pages():
    return [
        Decision,
        ResultsWaitPage,
        Results
    ]