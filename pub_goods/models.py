# -*- coding: utf-8 -*-
"""Documentation at https://github.com/wickens/django-otree-docs/wiki"""

from otree.db import models
import otree.models
from otree.common import Money, money_range

author = 'Donja Darai'

doc = """
Public goods game with groups of about 18 and an marginal per capita return of 0.1
"""

class Subsession(otree.models.BaseSubsession):

    name_in_url = 'pub_goods'


class Treatment(otree.models.BaseTreatment):
    # <built-in>
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    p = models.FloatField(
        default=2.00,
        doc="payoff = p(endowment-contribution)+a/N*sum(contribution)"
    )

    endowment = models.MoneyField(
        default=20.00,
        doc="payoff = p(endowment-contribution)+a/N*sum(contribution)"
    )

    a = models.FloatField(
        default=3.8,
        doc="payoff = p(endowment-contribution)+a/N*sum(contribution)"
    )

    def contribution_choices(self):
        return money_range(0,self.endowment,1.00)


class Match(otree.models.BaseMatch):
    # <built-in>
    treatment = models.ForeignKey(Treatment)
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    players_per_match = 4
    
    sum_contribution = models.MoneyField(
        default=None,
        doc="sum of contributions in a matching group"
    )
    
    avg_contribution = models.MoneyField(
        default=None,
        doc="average contribution of the other players"
    )
    
    def sum_avg(self):
    	self.sum_contribution = sum(p.contribution for p in self.players)
    	self.avg_contribution = self.sum_contribution / self.players_per_match
    
    def set_payoffs(self):
	for p in self.players:
	    p.payoff = p.treatment.p * (p.treatment.endowment - p.contribution) + p.treatment.a * p.match.avg_contribution        

class Player(otree.models.BasePlayer):
    # <built-in>
    match = models.ForeignKey(Match, null = True)
    treatment = models.ForeignKey(Treatment, null = True)
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    contribution = models.MoneyField(
        default=None,
        doc="player's own contribution"
    )

#* (p.treatment.endowment - p.contribution) + p.treatment.a / float(self.players_per_match) * sum_contribution
#(p.match.sum_contribution - p.contribution)
            #/(float(self.players_per_match)-1)

def treatments():
    return [Treatment.create()]