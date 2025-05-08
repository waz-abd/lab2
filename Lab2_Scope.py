# ENSF 692 Spring 2025
# May 8 Lab 2
# Exercise 2


# Trace through the execution of the following program. 
# Answer the questions in the comments with your group members.
# After discussing, use print statements to confirm your answers.

foo = 100
bar = foo
foo + bar

# POINT 1
# What is the value of foo at this point?
# What is the type of foo at this point?
# What is the value of bar at this point?
# What is the type of bar at this point?

spam = foo + bar
foo += 50
eggs = foo + bar
ham = [1, 2, 3]
baz = ham
ham.append(bar)

# POINT 2
# What is the value of foo at this point?
# What is the value of bar at this point?
# What is the value of spam at this point?
# What is the value of eggs at this point?
# What is the value of ham at this point?
# What is the value of baz at this point?

eggs = "Python is very flexible!"
spam = ham
ham = bar
bar += bar
foo = eggs
eggs = bar + ham
baz.append(bar)

# POINT 3
# What is the value of foo at this point?
# What is the value of bar at this point?
# What is the value of spam at this point?
# What is the value of eggs at this point?
# What is the value of ham at this point?
# What is the value of baz at this point?

# Print out the types and final values of each variable.
