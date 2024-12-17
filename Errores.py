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
	
def den(a):
	c = a[0]
	s = 0
	for x in a:
		s += abs(x-c)
		c = x
	
	return s/(a.size-1)


print("Modelo propio:")

denominador = den(celulas)
cel_mod = linearG(dias)
error = celulas - cel_mod
print( "\nMAE lineal: ", np.sum( abs(error) )/150 )
print( "MSE lineal:", np.sum( np.square(error) )/150 )
print( "MASE lineal:", np.sum( abs(error) / denominador )/150 )
print( "MAPE lineal:", np.sum( abs((100 * error)/celulas ) )/150 )
print( "sMAPE lineal:", np.sum( abs((200 * abs(error))/(celulas + cel_mod)) )/150 )
cel_mod = quadraticG(dias)
error = celulas - cel_mod
print( "\nMAE cuadrático: ", np.sum( abs(error) )/150 )
print( "MSE cuadrático:", np.sum( np.square(error) )/150 )
print( "MASE cuadrático:", np.sum( abs(error) / denominador )/150 )
print( "MAPE cuadrático:", np.sum( abs(100 * error/celulas ) )/150 )
print( "sMAPE cuadrático:", np.sum( abs((200 * abs(error))/(celulas + cel_mod)) )/150 )
cel_mod = expoG(dias)
error = celulas - cel_mod
print( "\nMAE exponencial: ", np.sum( abs(error) )/150 )
print( "MSE exponencial:", np.sum( np.square(error) )/150 )
print( "MASE exponencial:", np.sum( abs(error) / denominador )/150 )
print( "MAPE exponencial:", np.sum( abs(100 * error/celulas ) )/150 )
print( "sMAPE exponencial:", np.sum( abs((200 * abs(error))/(celulas + cel_mod)) )/150 )
cel_mod = gompertzG(dias)
error = celulas - cel_mod
print( "\nMAE gompertz: ", np.sum( abs(error) )/150 )
print( "MSE gompertz:", np.sum( np.square(error) )/150 )
print( "MASE gompertz:", np.sum( abs(error) / denominador )/150 )
print( "MAPE gompertz:", np.sum( abs(100 * error/celulas ) )/150 )
print( "sMAPE gompertz:", np.sum( abs((200 * abs(error))/(celulas + cel_mod)) )/150 )
cel_mod = logisG(dias)
error = celulas - cel_mod
print( "\nMAE logistico: ", np.sum( abs(error) )/150 )
print( "MSE logistico:", np.sum( np.square(error) )/150 )
print( "MASE logistico:", np.sum( abs(error) / denominador )/150 )
print( "MAPE logistico:", np.sum( abs(100 * error/celulas ) )/150 )
print( "sMAPE logistico:", np.sum( abs((200 * abs(error))/(celulas + cel_mod)) )/150 )
cel_mod = SSlogisG(dias)
error = celulas - cel_mod
print( "\nMAE SSlogistico: ", np.sum( abs(error) )/150 )
print( "MSE SSlogistico:", np.sum( np.square(error) )/150 )
print( "MASE SSlogistico:", np.sum( abs(error) / denominador )/150 )
print( "MAPE SSlogistico:", np.sum( abs(100 * error/celulas ) )/150 )
print( "sMAPE SSlogistico:", np.sum( abs((200 * abs(error))/(celulas + cel_mod)) )/150 )


with open("tiemposEstandar.txt", "r+") as file1:
	for line in file1:
		celulas_est = np.append(celulas_est, int(line.split()[0]))

def linearE(t):
	return 1360.68*t - 40934.11
	
def quadraticE(t):
	return 5.486*t*t + 422.5*t - 14040
	
def expoE(t):
	return np.exp(4.331823)*np.exp(0.0459824*t)
	
def gompertzE(t):
	return 203296.3*(0.000001560454**(0.971191**t))

def logisE(t):
	return 199100/(1+np.exp((106.2-t)/22.39))

def SSlogisE(t):
	return 248800/(1+np.exp((4.774-np.log(t))/0.2849))

print("\nModelo Poleszczuk")

denominador = den(celulas_est)
cel_mod = linearE(dias_est)
error = celulas_est - cel_mod
print( "\nMAE lineal: ", np.sum( abs(error) )/170 )
print( "MSE lineal:", np.sum( np.square(error) )/170 )
print( "MASE lineal:", np.sum( abs(error) / denominador )/170 )
print( "MAPE lineal:", np.sum( abs((100 * error)/celulas_est ) )/170 )
print( "sMAPE lineal:", np.sum( abs((200 * abs(error))/(celulas_est + cel_mod)) )/170 )
cel_mod = quadraticE(dias_est)
error = celulas_est - cel_mod
print( "\nMAE cuadrático: ", np.sum( abs(error) )/170 )
print( "MSE cuadrático:", np.sum( np.square(error) )/170 )
print( "MASE cuadrático:", np.sum( abs(error) / denominador )/170 )
print( "MAPE cuadrático:", np.sum( abs(100 * error/celulas_est ) )/170 )
print( "sMAPE cuadrático:", np.sum( abs((200 * abs(error))/(celulas_est + cel_mod)) )/170 )
cel_mod = expoE(dias_est)
error = celulas_est - cel_mod
print( "\nMAE exponencial: ", np.sum( abs(error) )/170 )
print( "MSE exponencial:", np.sum( np.square(error) )/170 )
print( "MASE exponencial:", np.sum( abs(error) / denominador )/170 )
print( "MAPE exponencial:", np.sum( abs(100 * error/celulas_est ) )/170 )
print( "sMAPE exponencial:", np.sum( abs((200 * abs(error))/(celulas_est + cel_mod)) )/170 )
cel_mod = gompertzE(dias_est)
error = celulas_est - cel_mod
print( "\nMAE gompertz: ", np.sum( abs(error) )/170 )
print( "MSE gompertz:", np.sum( np.square(error) )/170 )
print( "MASE gompertz:", np.sum( abs(error) / denominador )/170 )
print( "MAPE gompertz:", np.sum( abs(100 * error/celulas_est ) )/170 )
print( "sMAPE gompertz:", np.sum( abs((200 * abs(error))/(celulas_est + cel_mod)) )/170 )
cel_mod = logisE(dias_est)
error = celulas_est - cel_mod
print( "\nMAE logistico: ", np.sum( abs(error) )/170 )
print( "MSE logistico:", np.sum( np.square(error) )/170 )
print( "MASE logistico:", np.sum( abs(error) / denominador )/170 )
print( "MAPE logistico:", np.sum( abs(100 * error/celulas_est ) )/170 )
print( "sMAPE logistico:", np.sum( abs((200 * abs(error))/(celulas_est + cel_mod)) )/170 )
cel_mod = SSlogisE(dias_est)
error = celulas_est - cel_mod
print( "\nMAE SSlogistico: ", np.sum( abs(error) )/170 )
print( "MSE SSlogistico:", np.sum( np.square(error) )/170 )
print( "MASE SSlogistico:", np.sum( abs(error) / denominador )/170 )
print( "MAPE SSlogistico:", np.sum( abs(100 * error/celulas_est ) )/170 )
print( "sMAPE SSlogistico:", np.sum( abs((200 * abs(error))/(celulas_est + cel_mod)) )/170 )
