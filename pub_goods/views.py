# -*- coding: utf-8 -*-
import otree.views
import otree.views.concrete
import pub_goods.forms as forms
from pub_goods._builtin import Page, MatchWaitPage, SubsessionWaitPage
from otree.common import Money, money_range

def variables_for_all_templates(self):
    return {
        'endowment': self.treatment.endowment
    }

class Contribution(Page):

    template_name = 'pub_goods/Contribution.html'

    def get_form_class(self):
        return forms.ContributionForm


class ResultsWaitPage(MatchWaitPage):

    def after_all_players_arrive(self):
        self.match.sum_avg()
        self.match.set_payoffs()

    def body_text(self):
        return "Waiting for other players to decide."


class Results(Page):

    template_name = 'pub_goods/Results.html'

    def variables_for_template(self):
    	return {
	    'sum_contribution': self.match.sum_contribution,
	    'avg_contribution': self.match.avg_contribution,
	    'contribution': self.player.contribution,
	    'payoff': self.player.payoff
	}


def pages():
    return [
        Contribution,
        ResultsWaitPage,
        Results
    ]