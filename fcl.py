import numpy as np
import matplotlib.pyplot as plt


n_escenarios = 1000
n_años = 5

flujos_caja_libre = np.zeros((n_escenarios, n_años))

for i in range(n_escenarios):
    ingresos_simulados = np.random.normal(
            np.mean(datos_resultados['Ingresos']),
            np.std(datos_resultados['Ingresos']),
            n_años)

    costos_operativos_simulados = np.random.normal(
            np.mean(datos_resultados['Costos_Operativos']),
            np.std(datos_resultados['Costos_Operativos']),
            n_años)

    capex_simulado = np.random.normal(
            np.mean(datos_balance['CapEx']),
            np.std(datos_balance['CapEx']),
            n_años)

    ebitda = ingresos_simulados - costos_operativos_simulados
    fcl = ebitda - capex_simulado

    flujos_caja_libre[i] = fcl

tasa_descuento = 0.05

valor_presente_fcl = np.zeros(n_escenarios)
for i in range(n_escenarios):
    valor_presente_fcl[i] = np.sum(flujos_caja_libre[i] / (1 + tasa_descuento)**np.arange(1, n_años + 1))

media = np.mean(valor_presente_fcl)
mediana = np.median(valor_presente_fcl)
desviacion_estandar = np.std(valor_presente_fcl)

plt.hist(valor_presente_fcl, bins=50)
plt.title('Distribución del Valor Presente de FCL')
plt.xlabel('Valor Presente de FCL')
plt.ylabel('Frecuencia')
plt.show()
