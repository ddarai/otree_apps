# -*- coding: utf-8 -*-
from otree.db import models
import otree.models
from otree.common import Money, money_range
import random

author = 'Donja Darai'

doc = """
This app is used to conduct an experiment for norm elicitation (see Krupka & Weber).
"""

class Subsession(otree.models.BaseSubsession):

	name_in_url = 'norms' 
	
	def set_payoffs(self):
		for p in self.players:
			if p.rating == p.random_rating:
				p.payoff = p.treatment.match_payoff
			else:
				p.payoff = 0

class Treatment(otree.models.BaseTreatment):
    
    # <built-in>
    subsession = models.ForeignKey(Subsession)
    # </built-in>
    
    match_payoff = models.MoneyField(
    	default=10,
    	doc="payoff if answer matches most common answer"
    )

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
	
	rating = models.CharField(
		choices = ['very inappropriate','somewhat inappropriate','somewhat appropriate','very appropriate'],
		default = None,
		doc="Players enter norm rating"
	)
	
	random_player = models.IntegerField(
		default = None,
		doc="number of random player"
	)
	
	random_rating = models.CharField(
    	default = None,
    	doc="rating of random player"
    )

	def random(self):
 		self.random_player = random.choice(self.other_players_in_subsession())
 		self.random_rating = self.random_player.rating
 		
 			
def treatments():
    return [Treatment.create()]