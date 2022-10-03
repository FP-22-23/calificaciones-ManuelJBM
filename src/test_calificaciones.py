from calificaciones import *

def main():
    aciertos=lee_entero('Dame tus aciertos: ')
    errores=lee_entero('Dame tus errores: ')
    total_respuestas=lee_entero('Dame el total de respuestas correctas del test: ')
    nota=calcula_nota_cuestinario(aciertos,errores,total_respuestas)
    print('Tu notas es:', nota)

if __name__ == '__main__':
    main()

def main():
    C1=lee_real('Dame la nota del C1: ')
    C2=lee_real('Dame la nota del C2: ')
    C3=lee_real('Dame la nota del C3: ')
    pr1=lee_real('Dame la nota del proyecto en python: ')
    ex1=lee_real('Dame la nota del examen práctico de Python: ')
    cuatrimestre1=calcula_nota_cuatrimestre(C1,C2,C3,pr1,ex1)
    print('La nota del primer cuatrimestre es: ', cuatrimestre1)
    C4=lee_real('Dame la nota del C4: ')
    C5=lee_real('Dame la nota del C5: ')
    C6=lee_real('Dame la nota del C6: ')
    pr2=lee_real('Dame la nota del proyecto en Java: ')
    ex2=lee_real('Dame la nota del examen práctico de Java: ')
    cuatrimestre2=calcula_nota_cuatrimestre(C4,C5,C6,pr2,ex2)
    print('La nota del segundo cuatrimestre es: ', cuatrimestre2)
    print('Tu nota de evaluación continua es: ', calcula_nota_evaluacion_continua((cuatrimestre1+cuatrimestre2)/2))



if __name__ == '__main__':
    main()
