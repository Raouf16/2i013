import soccersimulator
from soccersimulator import AbstractStrategy, Vector2D, SoccerAction, settings
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Player, SoccerTournament

class MaStrategy(AbstractStrategy):
    def __init__(self):
        AbstractStrategy.__init__(self, "Aleatoire")
        
    
    def compute_strategy(self, state, id_team, id_p1ayer):
        p = state.player_state(id_team, id_p1ayer)
        vballe = state.ball.position
        vjoueur = p.position
        if(id_team == 1):
            if((vballe.distance(vjoueur)) < (settings.PLAYER_RADIUS + settings.BALL_RADIUS)):
                return SoccerAction(state.ball.position - p.position, Vector2D(settings.GAME_WIDTH, settings.GAME_HEIGHT / 2) - p.position)
            else:
                return SoccerAction(state.ball.position - p.position, Vector2D(0,0))
        else:
            if((vballe.distance(vjoueur)) < (settings.PLAYER_RADIUS + settings.BALL_RADIUS)):
                return SoccerAction(state.ball.position - p.position, Vector2D(0, settings.GAME_HEIGHT / 2) - p.position)
            else:
                return SoccerAction(state.ball.position - p.position, Vector2D(0,0))

               
               
team1 = SoccerTeam ("Real Madrid",[Player("Raouf",MaStrategy())])
team2 = SoccerTeam ("Barcelone",[Player("Yacine",MaStrategy())])

tournoi = SoccerTournament(1)
tournoi.add_team(team1)
tournoi.add_team(team2)

soccersimulator.show(tournoi)

 
