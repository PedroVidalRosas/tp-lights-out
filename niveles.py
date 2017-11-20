def niveles(nivel):
    #Devuelve un mapa dependiendo el nivel

    if type(nivel)!= int:
        return []

    if nivel < 0 or nivel > 5:

        return []

    if nivel == 1:
        mapa = ['   A B C D E',
                '1 |0 0 . 0 0',
                '2 |0 . 0 . 0',
                '3 |. 0 0 0 .',
                '4 |0 . 0 . 0',
                '5 |0 0 . 0 0']
        return mapa

    if nivel == 2:
        mapa = ['   A B C D E',
                '1 |. 0 . 0 .',
                '2 |0 0 . 0 0',
                '3 |. 0 . 0 .',
                '4 |0 . 0 . 0',
                '5 |0 . 0 . 0']
        return mapa

    if nivel == 3:
        mapa = ['   A B C D E',
                '1 |0 . . . 0',
                '2 |0 0 . 0 0',
                '3 |. . 0 . .',
                '4 |0 . 0 . .',
                '5 |0 . 0 0 .']
        return mapa
    if nivel == 4:
        mapa = ['   A B C D E',
                '1 |0 0 . 0 0',
                '2 |. . . . .',
                '3 |0 0 . 0 0',
                '4 |. . . . 0',
                '5 |0 0 . . .']
        return mapa
    if nivel == 5:
        mapa = ['   A B C D E',
               '1 |. . . 0 0',
               '2 |. . . 0 0',
               '3 |. . . . .',
               '4 |0 0 . . .',
               '5 |0 0 . . .']
        return mapa