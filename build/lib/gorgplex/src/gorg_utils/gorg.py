from dataclasses import dataclass
from gorgplex.src.modifiers.modifier import Modifier
print("Hello world")

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

if __name__ == "__main__":
    print("hello world")

    tim = Gorg("tim", Modifier(4.5, 2.1))
    print(tim)