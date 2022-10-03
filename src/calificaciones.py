def lee_entero(mensaje):
    res=int(input(mensaje))
    return res


def calcula_nota_cuestinario(aciertos,errores,total_respuestas):
    return 10*(aciertos/total_respuestas - errores(50-total_respuestas))

def calcula_nota_cuatrimestre(cuestionarios, pr, ex):
    res=10.0
    if pr<5:
        res=3.0
    else:
        res=0.1*((cuestionarios[0] + cuestionarios[1]+ cuestionarios[2]) + 0.1 * pr + 0.6* ex)
        return res

def lee_real(mensaje):
    res = float(input(mensaje))
    return res

def calcula_nota_evaluacion_continua(C1,C2):
    res=10
    if C1<4 or C2<4:
        res=4.0
    else:
        res=(C1+C2)/2
    return res