import soccersimulator
from soccersimulator import BaseStrategy, Vector2D, SoccerAction, settings
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Player, SoccerTournament


def peutShooter(vjoueur,vballe):
	return (vballe.distance(vjoueur)) < (settings.PLAYER_RADIUS + settings.BALL_RADIUS) # Si le joueur est dans le rayon de la balle, il tire

def passeOuShoot(vjoueur, vballe, id_team):
	if(id_team == 1): 
		if(vballe.x > settings.GAME_WIDTH - 5): #Si on est loin des buts, on fait des petites passes
			return SoccerAction(vballe - vjoueur, (Vector2D(settings.GAME_WIDTH, settings.GAME_HEIGHT / 2) - vjoueur) * 0.03)
		else: #Sinon, on tire
                	return SoccerAction(vballe - vjoueur, Vector2D(settings.GAME_WIDTH, settings.GAME_HEIGHT / 2) - vjoueur)
	else:
		if(vballe.x < 5): #Si on est loin des buts, on fait des petites passes
			return SoccerAction(vballe - vjoueur, (Vector2D(0, settings.GAME_HEIGHT / 2) - vjoueur) * 0.03)
		else: #Sinon, on tire
                	return SoccerAction(vballe - vjoueur, Vector2D(0, settings.GAME_HEIGHT / 2) - vjoueur)


def courirVersBalle(vjoueur,vballe):
	return SoccerAction(vballe - vjoueur, Vector2D(0,0)) #Si on peut ni tirer ni passer, on court vers la balle


def peutShooterDefense(vballe,vjoueur,id_team):
	if(id_team == 1):
		return vballe.x < 30
	else:
		return vballe.x > 120

def shootDefense(vjoueur,vballe,id_team):
	if(id_team == 1):
            	if (peutShooter(vjoueur,vballe)):
			return SoccerAction(Vector2D(10, settings.GAME_HEIGHT / 2) - vjoueur, Vector2D(0,0))
		else: 
			return SoccerAction(vballe - vjoueur, Vector2D(0,0))
	else:
	
		if(peutShooter(vjoueur,vballe)):
                	return SoccerAction(vballe - vjoueur, Vector2D(0, settings.GAME_HEIGHT / 2) - vjoueur)
            	else:
                	return SoccerAction(vballe - vjoueur, Vector2D(0,0))

def replacementDefense(vjoueur,vballe,id_team):
	if (id_team == 1):
		return SoccerAction(Vector2D(10, settings.GAME_HEIGHT / 2) - vjoueur, Vector2D(0,0))
	else:
		return SoccerAction(Vector2D(settings.GAME_WIDTH - 10, settings.GAME_HEIGHT / 2) - vjoueur, Vector2D(0,0))
		


class MaStrategy(BaseStrategy):
	def __init__(self):
        	BaseStrategy.__init__(self, "Aleatoire")
        
    
	def compute_strategy(self, state, id_team, id_p1ayer):
        	p = state.player_state(id_team, id_p1ayer)
        	vballe = state.ball.position
        	vjoueur = p.position
            
		if(peutShooter(vjoueur, vballe)):
			return passeOuShoot(vjoueur, vballe, id_team)	
 		else:
             		return courirVersBalle(vjoueur, vballe)



class MaStrategy2(BaseStrategy):
	def __init__(self):
        	BaseStrategy.__init__(self, "Aleatoire")
	    
    	def compute_strategy(self, state, id_team, id_p1ayer):
        	p = state.player_state(id_team, id_p1ayer)
        	vballe = state.ball.position
        	vjoueur = p.position
        
		if(peutShooterDefense(vballe,vjoueur,id_team)):
			return shootDefense(vjoueur,vballe,id_team)
		return replacementDefense(vjoueur,vballe,id_team)
       

               
team1 = SoccerTeam ("Real Madrid",[Player("Raouf",MaStrategy()), Player("Raouf2",MaStrategy2())])
team2 = SoccerTeam ("Barcelone",[Player("Yacine",MaStrategy()), Player("Yacine2",MaStrategy2())])
match = SoccerMatch(team1,team2, 4000)
soccersimulator.show(match)


