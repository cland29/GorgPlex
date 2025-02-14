from gorgplex.src.gorg_utils.gorg import Gorg
from gorgplex.src.gorg_utils.gorg_battler import *
from gorgplex.src.modifiers.modifier import Modifier
import matplotlib.pyplot as plt
import numpy as np

def vizualize_strength(gorg:Gorg)->None:
    '''Creates 10,000 gorgs of various strengths and skills and shows the change of being beats and your win or loss'''

    op_strength = np.linspace(0.1, 1, 1000)
    op_skill = np.linspace(0.1, 1, 1000)

    

    X, Y = np.meshgrid(op_strength, op_skill)

    kelly_list = np.empty((1000, 1000))
    roi_list = np.empty((1000, 1000))


    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            op_gorg = Gorg(None, modifier=Modifier(X[i][j], Y[i][j]))
            kelly = get_kelly_on_fight(gorg, op_gorg)
            roi = get_roi_on_fight(gorg, op_gorg)
            kelly_list[i, j] = kelly
            roi_list[i, j] = roi

    plt.contourf(X, Y, roi_list)
    plt.colorbar()
    plt.title(f"{gorg.name}'s roi against Ops")
    plt.xlabel("Op Strength")
    plt.ylabel("Op Skill")
    plt.show()


