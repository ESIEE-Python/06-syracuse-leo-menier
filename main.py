"""
 Ce fichier sert a exéctuer la suite de syrcause sous forme de liste
"""


# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """
     ceci est une docstring et les modifications
     ligne 23 sont également éffectuées pour pouvoir augmenter la note du pylint
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """
    l = [ ]
    while n != 1:
        l.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    l.append(1)
    return l


def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """

    return len(l)

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    # votre code ici
    tva = 1
    while l[0]<l[tva]:
        tva+=1
    return tva


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """

    # votre code ici
    return max(l)


#### Fonction principale


def main():
    """
     Cette fonction permet d'éxécuter toutes les autres afon d'avoir les résultats
    """
    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr)-1)
    print(temps_de_vol_en_altitude(lsyr)-1)
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
