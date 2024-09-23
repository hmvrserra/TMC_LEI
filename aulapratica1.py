import numpy as np
import matplotlib.pyplot as plt


###EX 1
##Variáveis
x = np.array([1., 2., 3., 4.])
y = np.array([0., 3., 2., 5.])

plt.plot(x, y, 'r.')
#plt.show()

numDados = x.shape[0]
z = np.ones((numDados, 2))
print("Z inicial: \n", z)

z[:,1] = x
print("Z modificado: \n", z)

##Transposta
zt = z.T
print("Z transposto: \n", zt)

##Produto de Matrizes
prod = zt@z
print("Produto de Matrizes: \n", prod)

##Inversa
from numpy.linalg import inv

a = inv(zt@z)
print("Inversa: \n", a)

##Função
beta = a@zt@y
print("Beta: \n", beta)

##Plot
xx = np.arange(x[0], x[-1]+.1, .1)
yy = beta[0] + beta[1]*xx
plt.plot(x, y, 'r.')
plt.plot(xx, yy, 'b')
x_prev = 5
y_prev = beta[0] + beta[1]*x_prev
plt.plot(x_prev, y_prev, 'go')
plt.show()


###EX 2
