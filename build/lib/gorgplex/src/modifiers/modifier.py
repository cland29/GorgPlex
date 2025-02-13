from dataclasses import dataclass

@dataclass
class Modifier:
    '''A modifier for a gorg
    
    args:
        strength: How loss a gorg inflicts if it wins
        skill: How good a gorg is. A gorgs odds of winning a fight at his skill/opponents skill'''
    strength: float
    skill: float