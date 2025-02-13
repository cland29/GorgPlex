from gorg_utils.gorg import Gorg
from random import random

def get_win_ratio(gorg_1:Gorg, gorg_2, Gorg)->float:
    '''Returns a percentage chance that gore_1 would beat gore_2 in a fight'''
    return gorg_1.modifier.skill / (gorg_1.modifier.skill + gorg_2.modifier.skill)

def fight_gorgs(gorg_1: Gorg, gorg_2: Gorg)->Gorg:
    '''Pits two gorgs against each other, and then returns the winner'''
    gorg_1_winrate = get_win_ratio(gorg_1, gorg_2)

    if gorg_1_winrate > random():
        return gorg_1
    else:
        return gorg_2
    
