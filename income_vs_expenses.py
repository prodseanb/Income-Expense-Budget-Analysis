# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:56:37 2021
Income/Expense Line Graph Budget Analysis
@author: Sean Bachiller
"""
import matplotlib.pyplot as plt




# plot 1 values 
x1 = ["Month 1","Month 2","Month 3", "Month 4", "Month 5", "Month 6"] 
y1 = [] 
# plot 2 values 
x2 = ["Month 1","Month 2","Month 3", "Month 4", "Month 5", "Month 6"] 
y2 = []

            
def income():
    for i in range(1,7): # loop 6 times
        try:
            # Prompt for income
            print('Enter the amount of income earned for month', i )
            plot1 = float(input())
            y1.append(plot1) # append to list
                      
         
        except ValueError:
            y1.clear()
            print('Invalid input.')
income()
while True: # validation -- if user input contains a string, list length will always be < 6
    if len(y1) < 6:
        y1.clear()
        print('\nEvaluation incomplete. Only numeric values are allowed. Please try again.\n')
        income()
    else:
        break
    
def expenses():
    for i in range(1,7): # loop 6 times
        try:
            # Prompt for expenses
            print('Enter the amount spent for month', i )
            plot2 = float(input())
            y2.append(plot2) # append to list
            

        except ValueError:
            y2.clear()
            print('Invalid input.')
expenses()      
while True: # validation -- if user input contains a string, list length will always be < 6
    if len(y2) < 6:
        y2.clear()
        print('\nEvaluation incomplete. Only numeric values are allowed. Please try again.\n')
        expenses()     
    else:
        break
              
              
# plotting the points  
plt.plot(x1, y1, label = "Income", color='green', marker='o', markerfacecolor='green', markersize=6) 
plt.plot(x2, y2, label = "Expenses", color='red', marker='o', markerfacecolor='red', markersize=6) 
# naming the x axis 
plt.xlabel('evaluation period') 
# naming the y axis 
plt.ylabel('earned/spent') 
  
# giving a title to my graph 
plt.title('A 6-month income/expense budget analysis') 

plt.legend() # show a legend
plt.show() # show the plot
