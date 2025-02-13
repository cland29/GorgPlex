from dataclasses import dataclass
from modifiers.modifier import modifier

@dataclass
class Gorg():
    '''
    Class to define a Gorg
    
    Args:
        modifiers: A modifier for a gorg
        isFlowerLover: Knowing if your gorg likes flowers
        '''
    name: str
    modifier: modifier
    isFlowerLover: bool = True

    