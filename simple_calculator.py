print("################################################")
print("# SPRING 2020                                  #")
print("# BILEN                                        #")
print("#        SCORE CALCULATOR FOR ECON224:         #")
print("#            (UP TO FINAL EXAM)                #")
print("#                                              #")
print("################################################")
print("")
print("Instructions: You can use this simple calculator") 
print("to calculate the points you accumulated going towards") 
print("the final exam. You can insert what you see on Blackboard") 
print("and get your score before final which is be out of 70 points.")
print("")

ps1 = int(input("How many points did you get from Problem Set 1?"))
ps2 = int(input("How many points did you get from Problem Set 2?"))
ps3 = int(input("How many points did you get from Problem Set 3?"))
ps4 = int(input("How many points did you get from Problem Set 4?"))
ps5 = int(input("How many points did you get from Problem Set 5?"))
ps6 = int(input("How many points did you get from Problem Set 6?"))

m1 = int(input("How many points did you get from Midterm 1?"))
m2 = int(input("How many points did you get from Midterm 2?"))

#fin = int(input("How many points did you get from Midterm 1?"))

psets = [ps1, ps2, ps3, ps4, ps5, ps6]

psets.remove(min(psets))

overall = sum(psets) + 0.25*m1 + 0.25*m2

print("Your score before the final exam is " + str(overall) +  "/70")