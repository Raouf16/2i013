import soccersimulator
from soccersimulator import BaseStrategy, Vector2D, SoccerAction, settings
from soccersimulator import SoccerTeam, SoccerMatch
from decisiontree import DTreeStrategy
from soccersimulator import Player, SoccerTournament
from Strat import *


team1 = SoccerTeam ("DZPOWER",[Player("Messi",attaquant_fonceur)])


team2 = SoccerTeam ("DZPOWER",[Player("Raouf",milieu_defensif), Player("Yacine",attaquant_fonceur)])


team4 = SoccerTeam ("DZPOWER",[Player("Raouf",attaquant_pointe), Player("Yacine",milieu_defensif), Player("Raouf JR",milieu), Player("Yacine JR",defenseur_central)])



