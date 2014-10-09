# -*- coding: utf-8 -*-
import otree.views
import otree.views.concrete
import norms.forms as forms
from norms._builtin import Page, MatchWaitPage, SubsessionWaitPage
from otree.common import Money, money_range

def variables_for_all_templates(self):
	return {
		 'round_number': self.subsession.round_number
	}

class Question(Page):

	template_name = 'norms/Question.html'
	
	def get_form_class(self):
		return forms.QuestionForm

#     def participate_condition(self):
#         return True

#     def variables_for_template(self):
#         return {
#             'my_variable_here': 1,
#         }

class ResultsWaitPage(SubsessionWaitPage):
 
# 	def after_all_players_arrive(self):
#     	#self.match.set_payoffs()
# 		self.player.random()


# THIS SOLUTION WORKS	 
	def after_all_players_arrive(self):
		for p in self.subsession.players:
			#p.random()
			p.subsession.most_common()
			p.subsession.set_payoffs()

	def body_text(self):
		return "Waiting for other players to decide."


class Results(Page):

#     def participate_condition(self):
#         return True

	template_name = 'norms/Results.html'

	def variables_for_template(self):
		return {
			'rating': self.player.get_rating_display,
			'payoff': self.player.payoff,
			#'random_player' : self.player.random_player,
			#'random_rating' : self.player.random_rating,
			'most_common_rating' : self.player.get_most_common_rating_display
		}

def pages():
	return [
		Question,
		ResultsWaitPage,
		Results
	]