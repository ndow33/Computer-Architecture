#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

# print8 filename = r'C:\Users\ndow3\Desktop\github repos\CS\Computer-Architecture\ls8\examples\print8.ls8'
filename = r'C:\Users\ndow3\Desktop\github repos\CS\Computer-Architecture\ls8\examples\mult.ls8'

cpu.load(filename)
cpu.run()