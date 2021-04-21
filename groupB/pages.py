from .models import *
import time

class Heterogeneity(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'nationality', 'child', 'residency']
class Information(Page):
    form_model = 'group'
class Idealmaternity(Page):
    form_model = 'player'
    form_fields = ['idealmaternity']
class Idealpaternity(Page):
    form_model = 'player'
    form_fields = ['idealpaternity']
class Mandatorymaternity(Page):
    form_model = 'player'
    form_fields = ['mandatorymaternity']
class Mandatorypaternity(Page):
    form_model = 'player'
    form_fields = ['mandatorypaternity']
class Peercomparaison(Page):
    form_model = 'player'
    form_fields = ['peermaternity', 'peerpaternity']
class End(Page):
    form_model = 'player'
    form_fields = ['Publicgoodgame']

page_sequence = [Information,
                 Idealmaternity,
                 Idealpaternity,
                 Mandatorymaternity,
                 Mandatorypaternity,
                 Peercomparaison,
                 End]
