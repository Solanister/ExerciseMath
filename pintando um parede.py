l = float(input('Largura da parede:'))
a = float(input('Altura da parede: '))
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(l, a, l*a))
print('Para pintar essa parede, você presisará de {}L de tinta.'.format(l*a / 2))
#Considere que a cada 2m² de parede, necessitamos de 1L de tinta.
