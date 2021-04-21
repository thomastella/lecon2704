from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class SurveyPage(Page):
    form_model = 'player'
    form_fields = ['age',
                   'education',
                   'studyfield',
                   'ExperEcon',
                   'nationality',
                   'child',
                   'marital',
                   'residency']

class EndPage(Page):
    pass

page_sequence = [SurveyPage,
                 EndPage]
