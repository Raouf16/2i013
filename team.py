import soccersimulator
from soccersimulator import BaseStrategy, Vector2D, SoccerAction, settings
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Player, SoccerTournament
from strategies import attaquantcentral, defenseurcentral, defenseurgauche, defenseurdroit, Milieu


team1 = SoccerTeam ("Real Madrid",[Player("Messi",attaquantcentral())])

team2 = SoccerTeam ("Real Madrid",[Player("Raouf",attaquantcentral()), Player("Yacine",defenseurgauche())])

team4 = SoccerTeam ("Barca",[Player("Raouf",attaquantcentral()), Player("Yacine",Milieu()), Player("Raouf JR",defenseurgauche()), Player("Yacine JR",defenseurdroit())])
