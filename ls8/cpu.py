"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # ram stores the istructions
        self.ram = [0] * 256
        # stores the values
        self.reg = [0] * 8
        # has a pointer
        self.pc = 0
        # halter
        self.halt = False

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI: these first three lines say insert 8 into memory at register/index 0
            0b00000000, # R0
            0b00001000, # 8 
            0b01000111, # PRN: these last three lines print R0 and halt the program
            0b00000000, # R0 
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
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
        # get the index
        pc = self.ram[self.pc+1]
        # get the value
        value = self.ram[self.pc+2]
        # store value at index
        self.reg[pc] = value
        # move up 3 indexes in ram
        self.pc += 3
    
    # print a value from reg
    def prn(self):
        # get the index to print from ram
        index = self.ram[self.pc+1]
        # print the value at index in reg
        print(self.reg[index])
        # move up 2 indexes in ram
        self.pc += 2
    
    # stop the run of the CPU
    def hlt(self):
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
        # instantiate boolean to start and stop the while loop

        while self.halt == False:
            # get the command
            instruction = self.ram[self.pc]

            # LDI
            if instruction == 0b10000010:
                self.ldi()

            # PRN
            elif instruction == 0b01000111:
                # print(f'PRN PC: {self.pc}')
                self.prn()

            # HLT    
            elif instruction == 0b00000001:
                # print(f'HLT PC: {self.pc}')
                self.hlt()

            else:
                print(f'unrecognized instruction: {instruction}')
                break
