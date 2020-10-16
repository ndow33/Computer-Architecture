elif instruction == CALL:
		# Get address of the next instruction after the CALL
		return_addr = pc + 2
​
		# Push it on the stack
		push_val(return_addr)
​
		# Get subroutine address from register
		reg_num = memory[pc + 1]
		subroutine_addr = register[reg_num]
​
		# Jump to it
		pc = subroutine_addr
​
	elif instruction == RET:
		# Get return addr from top of stack
		return_addr = pop_val()
​
		# Store it in the PC
		pc = return_addr
​
def push_val(value):
	# Decrement the stack pointer
	register[SP] -= 1
​
	# Copy the value onto the stack
	top_of_stack_addr = register[SP]
	memory[top_of_stack_addr] = value
​
def pop_val():
	# Get value from top of stack
	top_of_stack_addr = register[SP]
	value = memory[top_of_stack_addr] # Want to put this in a reg
​
	# Increment the SP
	register[SP] += 1
​
	return value
​
