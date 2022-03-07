This is the repository for the COMP26020 Part III lab exercise (Compilers)
Written by Samuel Zureick, x83005sz

This is a simple program that is used for register allocation with live ranges.
The program takes two command line arguments, the first being the input file, and the second being the output file. 
example command: lab4_compiler.py input.txt output.txt
The input file should be an interference graph representing the problem.
The output file will specify the coloured graph generated by the algorithm.
The program can only allocated a maximum of 26 registers. If the wrong number of command line arguments are supplied or the number of registers being used is exceeded, the program will display an error message and halt.