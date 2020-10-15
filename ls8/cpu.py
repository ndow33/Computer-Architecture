"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # store the filename given in the command line
        self.filename = sys.argv[1]
        # ram stores the istructions
        self.ram = [0] * 256
        # stores the values
        self.reg = [0] * 8
        # has a pointer that points to our ram address
        self.pc = 0
        # halter
        self.halt = False
        # stack pointer
        self.sp = 0xf4
        # store stack pointer in reg7
        self.reg[7] = self.sp

        self.instructions = {
                                'LDI': 0b10000010, 
                                'PRN': 0b01000111,
                                'HLT': 0b00000001,
                                'MULT': 0b10100010,
                                'PUSH': 0b01000101,
                                'POP': 0b01000110
                            }

    def load(self, filename = 'No File'):
        """Load a program into memory."""
        # load the file given in the command line
        filename = self.filename
        # create a set of numbers
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        # nums = set(nums)
        address = 0
        # get the file type
        file_type = filename.split('.')[1]

        if file_type != 'ls8':
            print(f'ERROR: {filename} is not an ls8 file')
        else:
            # read in the instructions into ram
            with open(filename, 'r') as f:
                for line in f:
                    # get rid of leading and trailing spaces
                    line = line.strip()
                    # if the first value is a number
                    if len(line) > 0:
                        if line[0] in nums:
                            # get the number by itself
                            line = line.split(' ')
                            value = int(line[0], 2)
                            # add it to the ram
                            self.ram[address] = value
                            address += 1      

        


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")
    
    # read a value from ram
    def ram_read(self, pc):
        return self.ram[pc]

    # write a value to ram
    def ram_write(self, pc, value):
        self.ram[pc] = value

    # write a value to reg
    def ldi(self):
        '''
        LDI register immediate
        Set the value of a register to an integer.
        '''
        # get the register
        register = self.ram[self.pc+1]
        # get the value
        value = self.ram[self.pc+2]
        # store value in register
        self.reg[register] = value
        # move up 3 indexes in ram
        self.pc += 3
    
    # print a value from reg
    def prn(self):
        '''
        PRN register pseudo-instruction
        Print numeric value stored in the given register.
        Print to the console the decimal integer value that is stored in the given register.
        '''
        # get the index to print from ram
        index = self.ram[self.pc+1]
        # print the value at index in reg
        print(self.reg[index])
        # move up 2 indexes in ram
        self.pc += 2

    # multiply two values stored in the register
    def mult(self):
        idx_a = self.ram[self.pc+1]
        idx_b = self.ram[self.pc+2]
        product = self.reg[idx_a] * self.reg[idx_b]
        self.reg[idx_a] = product
        self.pc += 3

    # push
    def push(self):
        '''
        PUSH register
        Push the value in the given register on the stack.
        Decrement the SP.
        Copy the value in the given register to the address pointed to by SP.
        '''
        # get the stack pointer minus 1
        pointer = self.sp-1
        # get the register index holding the value
        index = self.ram[self.pc+1]
        # get the value from the register
        value = self.reg[index]
        # write to ram
        self.ram_write(pointer, value)
        # decrement stack pointer
        self.sp-=1
        # increment ram pointer
        self.pc+=2
    
    # pop
    def pop(self):
        '''
        POP register
        Pop the value at the top of the stack into the given register.
        Copy the value from the address pointed to by SP to the given register.
        Increment SP.
        '''
        # get the stack pointer
        pointer = self.sp
        # get the register index that WILL hold the value
        index = self.ram[self.pc+1]
        # get the value from ram
        value = self.ram[pointer]
        # store it in reg
        self.reg[index] = value
        # increment stack pointer
        self.sp+=1
        # increment ram pointer 
        self.pc+=2

    
    # stop the run of the CPU
    def hlt(self):
        '''
        Halt the CPU (and exit the emulator).
        '''
        self.halt = True

    # useful for debugging
    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""

        while self.halt == False:
            # self.trace()
            # get the command
            instruction = self.ram[self.pc]

            # LDI
            if instruction == self.instructions['LDI']:
                self.ldi()

            # PRN
            elif instruction == self.instructions['PRN']:
                self.prn()
            
            # MULT
            elif instruction == self.instructions['MULT']:
                self.mult()

            # PUSH
            elif instruction == self.instructions['PUSH']:
                self.push()

            # POP
            elif instruction == self.instructions['POP']:
                self.pop()

            # HLT    
            elif instruction == self.instructions['HLT']:
                # print(self.sp - 1)
                self.hlt()

            else:
                print(f'unrecognized instruction: {instruction}')
                break
