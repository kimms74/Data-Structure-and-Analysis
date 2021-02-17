from Factory import Factory
import os

path = os.path.dirname(os.path.realpath(__file__))
Filename=path + '/Plan-2012.12.24.csv'
f=Factory(Filename,0.7)
f.run()