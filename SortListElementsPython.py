# In python, we can adopt proper statements and tools that can help sort values
# One can sort values in ascending or sort them in descending order
# In this short example, we are demonstrating sorting items in ascending order
print("|-----------------------------------------------------------------------------------|")
print("Hello world ")
print("This lesson shows value sorting in Ascending and Descending order")
# Below is the list to work with, called theList, with 28 elements
theList = [2,3,5,9,3,4,6,8,4,8,3,2,6,2,9,2,7,2,5,0,20,4,16,8,12,1]    # This is the list for demonstration
print("The Size of the list is: ", len(theList), "Items")   # This helps us get the size of the list

# To sort the values/elements, we use the sorted statement in python
theList = sorted(theList, reverse=False)   # This returns the sorted list in Ascending order
# That is, from smallest to largest
print("|------------------------The list in Ascending order is:----------------------------|")
print(theList)
theList = sorted(theList, reverse=True)   # This returns the sorted list in Descending order
# That is, from largest to smallest
print("|----------------------The list in Descending order is:-----------------------------|")
print(theList)
theList = sorted(theList)   # This returns the sorted list in Descending order
# That is, from largest to smallest
print("|--------Order goes to default of Ascening if true/false is not specified):---------|")
print(theList)


#------------OUTPUTS------------

#   |-----------------------------------------------------------------------------------|
#   Hello world 
#   This lesson shows value sorting in Ascending and Descending order
#   The Size of the list is:  26 Items
#   |------------------------The list in Ascending order is:----------------------------|
#   [0, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 8, 8, 8, 9, 9, 12, 16, 20]
#   |----------------------The list in Descending order is:-----------------------------|
#   [20, 16, 12, 9, 9, 8, 8, 8, 7, 6, 6, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 2, 2, 1, 0]
#   |--------Order goes to default of Ascening if true/false is not specified):---------|
#   [0, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 8, 8, 8, 9, 9, 12, 16, 20]
