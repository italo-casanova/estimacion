import numpy as np
import matplotlib.pyplot as plt

def montecarlo(n_escenarios: int, n_años: int, ingresos: list, costos: list):
    valores_empresa = []
    for _ in range(n_escenarios):
        ingresos_simulados = np.random.normal(np.mean(ingresos), np.std(ingresos), n_años)
        costos_simulados = np.random.normal(np.mean(costos), np.std(costos), n_años)

        flujo_efectivo = ingresos_simulados - costos_simulados
        valor_presente = np.sum(flujo_efectivo / (1 + 0.05)**np.arange(1, n_años + 1))
        valores_empresa.append(valor_presente)
    return valores_empresa

ingresos = [2384154, 3202931, 3054026, 2896894, 2538593, 4199448, 3975295]
costos = [1657585, 2243976, 2506388, 2115570, 1990414, 2195098, 2402516]

n_escenarios = 1000
n_años = 5

valores_empresa = montecarlo(n_escenarios, n_años, ingresos, costos)

media = np.mean(valores_empresa)
mediana = np.median(valores_empresa)
desviacion_estandar = np.std(valores_empresa)

plt.hist(valores_empresa, bins=50)
plt.title('Distribución del Valor de la Empresa')
plt.xlabel('Valor de la Empresa')
plt.ylabel('Frecuencia')
plt.show()
