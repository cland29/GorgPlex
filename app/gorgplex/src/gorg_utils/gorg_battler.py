from gorgplex.src.gorg_utils.gorg import Gorg
from random import random

def get_win_ratio(gorg_1:Gorg, gorg_2: Gorg)->float:
    '''Returns a percentage chance that gore_1 would beat gore_2 in a fight'''
    return gorg_1.get_skill() / (gorg_1.get_skill() + gorg_2.get_skill())

def fight_gorgs(gorg_1: Gorg, gorg_2: Gorg)->Gorg:
    '''Pits two gorgs against each other, and then returns the winner'''
    gorg_1_winrate = get_win_ratio(gorg_1, gorg_2)

    if gorg_1_winrate > random():
        return gorg_1
    else:
        return gorg_2
    
def get_kelly_on_fight(gorg_1: Gorg, gorg_2: Gorg)->float:
    '''
    Returns the kelly criteron for a gorg fight
    '''
    winrate = get_win_ratio(gorg_1, gorg_2)

    return winrate/gorg_2.get_strength() - (1-winrate)/gorg_1.get_strength()


def get_roi_on_fight(gorg_1: Gorg, gorg_2: Gorg, kelly_percent: float = 1.0, have_max_kelly: bool = True, max_kelly_amount: float = 1.0)->float:
    '''
    Returns the roi for a gorg fight

    Args:
        Gorg_1: The first gorg in the fight that you bet on
        Gorg_2: The second gorg in the fight that you bet on
        kelly_percent: used to bet a percent kelly, like a half or quarter kelly
        have_max_kelly: cap the kelly at a certain percentage
        max_kelly: The maximum kelly is allowed to be if have_max_kelly is True
    '''
    percent_won = gorg_1.get_strength()   # Once skill is out done, Gorgs always win by their strength
    percent_lost = gorg_2.get_strength()  # Same here
    winrate = get_win_ratio(gorg_1, gorg_2)
    kelly = get_kelly_on_fight(gorg_1, gorg_2)

    if have_max_kelly:
        if kelly > max_kelly_amount:
            kelly = max_kelly_amount
    if kelly < 0:
        kelly = 0

    kelly *= kelly_percent

    return ((1 + percent_won*kelly)**winrate)*((1 - percent_lost*kelly)**(1-winrate))


    

    
