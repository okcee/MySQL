'''
i_horas=int(input("¿Cuántas horas has trabajado? "))
f_coste=float(input("¿Cuánto es salario acordado por hora trabajada? "))
f_paga=i_horas*f_coste
print(f"La paga que corresponde es igual a {f_paga} Euros")
'''

def calcular_paga(horas, coste):
    paga = horas * coste
    return paga
horas = int(input("Horas: "))
coste = float(input("Coste: "))
paga = calcular_paga(horas, coste)
print("La paga es: ", paga, "euros")
