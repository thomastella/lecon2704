from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Amma Panin'

doc = """
Survey module for the LECON2704 group experiments"
"""


class Constants(BaseConstants):
    name_in_url = 'lecon2704_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    age = models.IntegerField(
        label='What is your age?',
        choices=range(18, 100),
        initial=None)

    education = models.StringField(
        choices=[['A', 'BA'],
                 ['B', 'MA'],
                 ['C', 'PhD'],
                 ['D', 'Other']],
        label='What is your level of education? If you are currently pursuing a degree select that one.')
    
    studyfield = models.StringField(
        blank=True,
        label='What did you study/are you studying?')
    
    ExperEcon = models.BooleanField(
        choices=[[True, 'Yes'],
                 [False, 'No']],
        label='Have you ever taken an Experimental Economics course?')

    nationality = models.StringField(label='What is your nationality?')
    
    child = models.StringField(
        choices=[['Yes', 'Yes'],
                 ['No', 'No']],
        label = 'Do you have children?')

    marital = models.StringField(
        choices=[["Long term partnership", "Long term partnership"],
                 ["Single", "Single"],
                 ["Separated or Divorced", "Separated or Divorced"],
                 ["Widowed", "Widowed"]],
        label='What is your marital status?')
    
    residency = models.StringField(
        label='In what country do you live?')
     
