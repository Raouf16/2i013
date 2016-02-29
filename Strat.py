from  soccersimulator import settings
from soccersimulator import BaseStrategy, SoccerAction, KeyboardStrategy
from decisiontree import *
from Tools import *
from Strat import *
import cPickle 

class Strat(BaseStrategy):
    def __init__(self,comportement,name):
        BaseStrategy.__init__(self,name)
        self.comportement = comportement
    def compute_strategy(self, state, id_team, id_player):
        s_miroir = state
        if id_team==1 :
            Mystate = PlayerStateDecorator(s_miroir,id_team , id_player)
            return self.comportement(Mystate)
        else :
            s_miroir = miroir_st(state)
            Mystate = PlayerStateDecorator(s_miroir,id_team , id_player)
            return miroir_sa(self.comportement(Mystate))


attaquant = Strat(attaquant_fonceur, "A")
attaquant_pointe = Strat(attaquant_pointe, "AP")
defenseur_central = Strat(defenseur_central, "DC")
defenseur_gauche = Strat(defenseur_gauche, "DG")
defenseur_droit = Strat(defenseur_droit, "DD")
milieu = Strat(milieu, "M")
milieu_defensif = Strat(milieu_defensif, "MD")

#### Arbres de decisions

tree = cPickle.load(file("./arbre.pkl"))
dic = {"A":Strat(attaquant_fonceur, "1"),"AP":Strat(attaquant_pointe, "2"),"DC":Strat(defenseur_central, "3"), "DG":Strat(defenseur_gauche, "4"), "DD":Strat(defenseur_droit, "5"), "M":Strat(milieu, "6"), "MD":Strat(milieu_defensif, "7")}
treeStrat = DTreeStrategy(tree,dic,gen_features)

#### Controle avec commandes 

keytest = KeyboardStrategy(fn = "arbre")

keytest.add("a", attaquant)
keytest.add("z", attaquant_pointe)           
keytest.add("d", defenseur_central)  
keytest.add("e", milieu)  
keytest.add("r", milieu_defensif)

