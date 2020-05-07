from math import sqrt  #import sqrt from library math

#Search for square shapes

figure = str(input('Input figure name: '))

if figure == 'triangle':

    a = int(input())
    b = int(input())
    c = int(input()) 	# input a,b,c of the parties triangle

    p = (a + b + c) / 2
    t = (p * (p - a) * (p - b) * (p - c))         #Heron formula
    q = sqrt(t)
    print(q)	#output

elif figure == 'rectangle':
    a = int(input())
    b = int(input()) #input of parties rectangle
    print(a*b)	#output

elif figure == 'circle':
    r = int(input())	#a circle
    print(3.14 * r**2)  #Circle Square Formula
