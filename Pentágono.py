from turtle import *
def  pentágono(lado):
    #Desenha um triangulo de lado.
    color('gray', 'red')
    begin_fill()
    for i in range(5):
        forward(lado)
        left(72)
    end_fill()
pentágono(150)
done()
