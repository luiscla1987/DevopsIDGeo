import numpy as np
from scipy import stats


def uma_função_fictícia():
    """Não faz nada, mas tem requisitos. :)"""
    matriz1 = np.random.rand(5, 5)
    print(stats.describe(matriz1))


if __name__ == '__main__':
    uma_função_fictícia()
