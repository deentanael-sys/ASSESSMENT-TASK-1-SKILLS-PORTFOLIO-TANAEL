#Instructions Given:

'''
Write a program that searches for a specific string within a list of strings. The list is
initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your
task is to search for "Sam".
'''

#Simple Solution:
Names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] #initializing the list with names completes 1st task

search_name = 'Sam' #defining the name to search for completes 2nd task

if search_name in Names: #checks if input is in the list completes 3rd task
    print("Found") #if found completes 4th task
else:
    print("Not Found") #if not found completes 4th task

#result will be "Found" since "Sam" is in the list

# End of activity