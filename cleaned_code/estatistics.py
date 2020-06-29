import numpy as np

NULL_ANGLE = -50000


def get_mediana(vetor):
    v = sorted(vetor)
    if (len(v) % 2 == 1):
        return v[len(v) // 2]
    return v[int(len(v) / 2) - 1]


def moda(vetor):
    ocorrencia = {}
    for i in vetor:
        if i not in ocorrencia:
            ocorrencia[i] = 1
        else:
            ocorrencia[i] += 1

    max_ocorrencia = 0
    max_value = 0
    unico = True
    for value in ocorrencia:
        if (ocorrencia[value] > max_ocorrencia):
            unico = True
            max_value = value
            max_ocorrencia = ocorrencia[value]
        elif ocorrencia[value] == max_ocorrencia:
            unico = False
    if (unico):
        return max_value
    else:
        return get_mediana(vetor)