import pandas as pd
import numpy as np


# Función clasificadora

def clasificador(variable):
    if variable <= 6:
        return 'Bajo'
    elif 6 < variable <= 12:
        return 'Medio'
    else:
        return 'Alto'


censo = pd.DataFrame({'id' : [1, 2, 3, 4],
                      'ed' : [3, 20, 12, 13]})

print(censo)

censo['nivel'] = censo['ed'].apply(clasificador)

print(censo)
