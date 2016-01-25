import soccersimulator
from soccersimulator import BaseStrategy, Vector2D, SoccerAction, settings
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Player, SoccerTournament

class MaStrategy(BaseStrategy):
    def __init__(self):
        BaseStrategy.__init__(self, "Aleatoire")
        
    
    def compute_strategy(self, state, id_team, id_p1ayer):
        p = state.player_state(id_team, id_p1ayer)
        vballe = state.ball.position
        vjoueur = p.position
        if(id_team == 1):
            if((vballe.distance(vjoueur)) < (settings.PLAYER_RADIUS + settings.BALL_RADIUS)):
		if(p.position.x > settings.GAME_WIDTH - 5):
			return SoccerAction(state.ball.position - p.position, (Vector2D(settings.GAME_WIDTH, settings.GAME_HEIGHT / 2) - p.position)* 0.1)
		else:
                	return SoccerAction(state.ball.position - p.position, Vector2D(settings.GAME_WIDTH, settings.GAME_HEIGHT / 2) - p.position)
            else:
                return SoccerAction(state.ball.position - p.position, Vector2D(0,0))
        else:
            if((vballe.distance(vjoueur)) < (settings.PLAYER_RADIUS + settings.BALL_RADIUS)):
		if(p.position.x < 5):
			return SoccerAction(state.ball.position - p.position, (Vector2D(0, settings.GAME_HEIGHT / 2) - p.position)* 0.1)
		else:
                	return SoccerAction(state.ball.position - p.position, Vector2D(0, settings.GAME_HEIGHT / 2) - p.position)
            else:
                return SoccerAction(state.ball.position - p.position, Vector2D(0,0))

class MaStrategy2(BaseStrategy):
    def __init__(self):
        BaseStrategy.__init__(self, "Aleatoire")
        
    
    def compute_strategy(self, state, id_team, id_p1ayer):
        p = state.player_state(id_team, id_p1ayer)
        vballe = state.ball.position
        vjoueur = p.position
        if(id_team == 1):
		if(state.ball.position.x < 30):
            		if((vballe.distance(vjoueur)) < (settings.PLAYER_RADIUS + settings.BALL_RADIUS)):
				return SoccerAction(state.ball.position - p.position, Vector2D(settings.GAME_WIDTH, settings.GAME_HEIGHT / 2) - p.position)
           		else:
                		return SoccerAction(state.ball.position - p.position, Vector2D(0,0))
		return SoccerAction(Vector2D(10, settings.GAME_HEIGHT / 2) - p.position, Vector2D(0,0))
        else:
		if(state.ball.position.x > 120):	
            		if((vballe.distance(vjoueur)) < (settings.PLAYER_RADIUS + settings.BALL_RADIUS)):
                		return SoccerAction(state.ball.position - p.position, Vector2D(0, settings.GAME_HEIGHT / 2) - p.position)
            		else:
                		return SoccerAction(state.ball.position - p.position, Vector2D(0,0))
		return SoccerAction(Vector2D(settings.GAME_WIDTH - 10, settings.GAME_HEIGHT / 2) - p.position, Vector2D(0,0))

               
team1 = SoccerTeam ("Real Madrid",[Player("Raouf",MaStrategy()), Player("Raouf2",MaStrategy2())])
team2 = SoccerTeam ("Barcelone",[Player("Yacine",MaStrategy()), Player("Yacine2",MaStrategy2())])
match = SoccerMatch(team1,team2, 4000)
soccersimulator.show(match)


