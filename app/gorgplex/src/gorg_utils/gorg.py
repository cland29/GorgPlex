from dataclasses import dataclass
from gorgplex.src.modifiers.modifier import Modifier


@dataclass
class Gorg:
    '''
    Class to define a Gorg
    
    Args:
        modifiers: A modifier for a gorg
        isFlowerLover: Knowing if your gorg likes flowers
        '''
    name: str
    modifier: Modifier
    isFlowerLover: bool = True

    def get_strength(self)->float:
        return self.modifier.strength
    
    def get_skill(self)->float:
        return self.modifier.skill

if __name__ == "__main__":
    print("hello world")

    tim = Gorg("tim", Modifier(4.5, 2.1))
    print(tim)