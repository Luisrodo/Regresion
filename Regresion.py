import matplotlib.pyplot as plt
import numpy as np
from glob import glob

celulas = []
celulas_est = []
dias = np.arange(1, 151)
dias_est = np.arange(1, 171)
with open("tiemposGompertz.txt", "r+") as file1:
	for line in file1:
		celulas = np.append(celulas, int(line.split()[0]))

def linearG(t):
	return 799.4*t - 20448.7
	
def quadraticG(t):
	return 4.1586*t*t + 171.411*t - 4540.8611
	
def expoG(t):
	return np.exp(6.524127)*np.exp(0.041208*t)
	
def gompertzG(t):
	return 158514.3*(0.0006150401**(0.9803927**t))

def logisG(t):
	return 111500/(1+np.exp((98.08-t)/21.49))

def SSlogisG(t):
	return 150400/(1+np.exp((4.746-np.log(t))/0.3105))


plt.plot(dias, celulas, 'ko', markersize = 2)
plt.title('Número de células cancerígenas según el día de simulación')
plt.xlabel('Dias')
plt.ylabel('Nº de células cancerígenas')
plt.savefig('graficaGompertz.png')
plt.clf()

plt.plot(dias, celulas, 'ko', markersize = 2)
ln, = plt.plot(dias, linearG(dias), 'r', label = 'Lineal')
qu, = plt.plot(dias, quadraticG(dias), 'b', label = 'Cuadratica')
ex, = plt.plot(dias, expoG(dias), 'g', label = 'Exponencial')
plt.axis([0, 150, -5000, 110000])
plt.title('Número de células cancerígenas según el día de simulación')
plt.xlabel('Dias')
plt.ylabel('Nº de células cancerígenas')
plt.legend(handles=[ln,qu,ex])
plt.savefig('graficaGompertzLin.png')
plt.clf()

plt.plot(dias, celulas, 'ko', markersize = 2)
gm, = plt.plot(dias, gompertzG(dias), 'r', label = 'Gompertz')
#lo, = plt.plot(dias, logisG(dias), 'b', label = 'Logistica')
ls, = plt.plot(dias, SSlogisG(dias), 'b', label = 'Logistica')
plt.title('Número de células cancerígenas según el día de simulación')
plt.xlabel('Dias')
plt.ylabel('Nº de células cancerígenas')
plt.legend(handles=[gm,ls])
plt.savefig('graficaGompertzSin.png')
plt.clf()

with open("tiemposEstandar.txt", "r+") as file1:
	for line in file1:
		celulas_est = np.append(celulas_est, int(line.split()[0]))

def linearE(t):
	return 1360.68*t - 40934.11
	
def quadraticE(t):
	return 5.486*t*t + 422.5*t - 14040
	
def expoE(t):
	return np.exp(4.331823)*np.exp(0.059824*t)
	
def gompertzE(t):
	return 203296.3*(0.000001560454**(0.971191**t))

def logisE(t):
	return 199100/(1+np.exp((106.2-t)/22.39))

def SSlogisE(t):
	return 248800/(1+np.exp((4.774-np.log(t))/0.2849))

plt.plot(dias_est, celulas_est, 'ko', markersize = 2)
plt.title('Número de células cancerígenas según el día de simulación')
plt.xlabel('Dias')
plt.ylabel('Nº de células cancerígenas')
plt.savefig('graficaEstandar.png')
plt.clf()

plt.plot(dias_est, celulas_est, 'ko', markersize = 2)
lne, = plt.plot(dias_est, linearE(dias_est), 'r', label = 'Lineal')
que, = plt.plot(dias_est, quadraticE(dias_est), 'b', label = 'Cuadratica')
exe, = plt.plot(dias_est, expoE(dias_est), 'g', label = 'Exponencial')
plt.axis([0, 170, -5000, 210000])
plt.title('Número de células cancerígenas según el día de simulación')
plt.xlabel('Dias')
plt.ylabel('Nº de células cancerígenas')
plt.legend(handles=[lne,que,exe])
plt.savefig('graficaEstandarLin.png')
plt.clf()

plt.plot(dias_est, celulas_est, 'ko', markersize = 2)
gme, = plt.plot(dias_est, gompertzE(dias_est), 'r', label = 'Gompertz')
#loe, = plt.plot(dias_est, logisE(dias_est), 'b', label = 'Logistica')
lse, = plt.plot(dias_est, SSlogisE(dias_est), 'b', label = 'Logistica')
plt.title('Número de células cancerígenas según el día de simulación')
plt.xlabel('Dias')
plt.ylabel('Nº de células cancerígenas')
plt.legend(handles=[gme,lse])
plt.savefig('graficaEstandarSin.png')
plt.clf()

