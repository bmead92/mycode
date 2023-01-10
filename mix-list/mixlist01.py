#!/usr/bin/env python3
import random
my_list = ['192.168.0.5', 5060, 'UP' ]
iplist = [5060, '80', 55, '10.0.0.1', '10.20.30.1']
print('The first item in the list (IP): ' + my_list[0] )
print("The second item in the list (port): " + str(my_list[1]) )
print("The last item in the list (state): " + my_list[2] )
print('IP address from iplist: ' + iplist[3] + ' and ' + iplist[4])
wordbank= ["indentation", "spaces"] 
tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']
wordbank.append(4)
num = input(f'Please type in a number between 1 and {len(tlgstudents)} \n')
num = int(num)
student_name = tlgstudents[num - 1]
print(f"{random.choice(tlgstudents)} always uses {wordbank[-1]} {wordbank[1]} to indent.")

