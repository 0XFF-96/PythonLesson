# Aligned with opening dlimiter
# More indentation included to distinguish this from the rest.

def long_function_name(
		var_one, var_two, var_three,
		var_four):
	
	print(var_one)

# Hanging indents should add a level

foo = long_function_name(
	var_one, var_two, 	
	var_three, var_four)

#Arguments on first line forbidden when not using vertical alignment

# Further indentation required as indentation is not distinguishable

# Hanging indents *may* be indented to other than 4 spaces

# No extra indentation,

	if (this_is_one_thing and 
		that_is_anthoer_thing):
		do_something()

#Add a comment, which will provide some distinction in editors

# supporting syntax higlighting.

if (this_is_one_thing and
	that_is_another_thing):
	# since both conditions are true , we can frobnicate.
	do_something()

#Add some extra indentation on the conditional continuation line.

if (this_is_one_thing 
		and that_is_anthonerthing):

my_list = [
	1, 2, 3,
	4, 5, 6,
	]

result = some_function_that_takes_arguments(
	
