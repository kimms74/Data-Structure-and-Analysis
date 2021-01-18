import os
from Factory import Factory

path = os.path.dirname(os.path.realpath(__file__))
f=Factory(path +'/Plan-2012.12.24.csv')
f.run()