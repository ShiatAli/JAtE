import csv
import random
empire = 13
holder_num = "15000"
county_name = "sacramento"
def emp_num(i):
    switcher={
        13:"nevada",
        15:"sacramento"
    }
    return switcher.get(i,"manleyan")
     
def char_relig(i):
    switcher={
        0:"sedevacantist",
        1:"mainline",
        2:"mormon",
        3:'trailwalker',
        4:'zenist'
    }
    return switcher.get(i,"manleyan")
print ("Write to " + "c_" + county_name + '\n\n')
print ("#e_" + emp_num(empire) + '\n')
print ("2047.1.1={" + '\n')
print ('\t' + "holder=" + holder_num + '\n')
print ("}")

#Character history
print(holder_num + '= { #' + "c_" + county_name)
print('\t' + 'name="Xob"')
print('\t' + 'culture=valleyan')
print('\t' + 'religion=' + char_relig(random.randrange(0,5)))
print ('\t'+ str(random.randrange(2015,2043))+'.'+str(random.randrange(1,12))+".1={birth=yes}" + '\n')