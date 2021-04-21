
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, Page, WaitPage
)
cu = c

doc = ''
class Constants(BaseConstants):
    name_in_url = 'groupB'
    players_per_group = None
    num_rounds = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    idealmaternity = models.IntegerField(label="Quelle serait la durée idéale d'un congé maternité ? (en semaine) // What is the ideal duration of maternity leave? (in weeks)")
    idealpaternity = models.IntegerField(label="Quelle serait la durée idéale d'un congé paternité ? (en semaine) // What is the ideal duration of paternity leave? (in weeks)")
    mandatorymaternity = models.IntegerField(label='Combien de semaines de congé maternité devraient être obligatoires ? // How many weeks of maternity leave should be compulsory? ')
    mandatorypaternity = models.IntegerField(label='Combien de semaines de congé paternité devraient être obligatoires ? // How many weeks of paternity leave should be compulsory?')
    peermaternity = models.IntegerField(label='Selon vous, quelle est la réponse moyenne donnée par les autres répondants à la question “Combien de semaines de congé maternité devraient être obligatoires ?” ?  // What is the average response given by others to the question of “How many weeks of maternity leave should be compulsory?”')
    peerpaternity = models.IntegerField(label='Selon vous, quelle est la réponse moyenne donnée par les autres répondants à la question “Combien de semaines de congé paternité devraient être obligatoires ?” ? // What is the average response given by others to the question of “How many weeks should paternity leave be compulsory?”')
    Publicgoodgame = models.FloatField(label='Supposez que vous avez 100 Euros à votre disposition. Quelle part de ce montant seriez-vous prêt à donner à des crèches ou à des écoles maternelles ? // Suppose you have 100 Euros. How much of this amount would you be willing to donate to public preschools or kindergarden? ', max=100, min=0)
    age = models.IntegerField(label='Quel est votre âge ? // How old are you?')
    gender = models.StringField(choices=[['Homme // Men', 'Homme // Men'], ['Femme // Women ', 'Femme // Women '], ['X', 'X']], label='Quel est votre genre ? What is your gender?')
    nationality = models.StringField(label='Quelle est votre nationalité ? //  What is your nationality?')
    child = models.StringField(choices=[['Oui // Yes', 'Oui // Yes'], ['Non // No', 'Non // No']], label='Avez-vous des enfants ? // Do you have children?')
    residency = models.StringField(label='Dans quel pays résider vous ? // In what country do you live?')
