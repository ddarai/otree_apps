# -*- coding: utf-8 -*-
"""Documentation at https://github.com/wickens/django-otree-docs/wiki"""

from otree.db import models
import otree.models
from otree.common import Money, money_range

author = 'Donja Darai'

doc = """
This app is a weak link coordination game played among all participants
of the session, there are no subgroups.
"""

class Subsession(otree.models.BaseSubsession):

	name_in_url = 'weak_link'
	
	min_value = models.FloatField(
		default=None,
		choices=[(1, '100 %'),(0.8, '80 %'),(0.6, '60 %'), (0.4, '40 %'), (0.2, '20 %'), (0, '0 %')],
		doc="minimum of all decisions")
	
	def minimum(self):
		self.min_value = min(p.decision for p in self.players)
	
 	def set_payoffs(self):
 		for p in self.players:
  			p.payoff = p.treatment.a + p.treatment.b * p.subsession.min_value - p.treatment.c * p.decision
 	 	

class Treatment(otree.models.BaseTreatment):
    # <built-in>
    subsession = models.ForeignKey(Subsession)
    # </built-in>
    
    a = models.FloatField(default=200.0,doc="a+b*(minimum of all)-c*(own choice)")    
    
    b = models.FloatField(default=400.0,doc="a+b*(minimum of all)-c*(own choice)")    
    
    c = models.FloatField(default=200.0,doc="a+b*(minimum of all)-c*(own choice)")    
 

class Match(otree.models.BaseMatch):
    # <built-in>
    treatment = models.ForeignKey(Treatment)
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    players_per_match = 1


class Player(otree.models.BasePlayer):
	# <built-in>
	match = models.ForeignKey(Match, null = True)
	treatment = models.ForeignKey(Treatment, null = True)
	subsession = models.ForeignKey(Subsession)
	# </built-in>
    
	decision = models.FloatField(
		default=None,
		choices=[(1, '100 %'),(0.8, '80 %'),(0.6, '60 %'), (0.4, '40 %'), (0.2, '20 %'), (0, '0 %')],
		doc="degree to which capital requirement is accomodated"
	)
				

def treatments():
    return [Treatment.create()]