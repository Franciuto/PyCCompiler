import os
import platform
import re

# TITLE
title =  "Franciuto's C Compiler\nVersion 1.0\n"
print(title)

# SYSTEM IN USE
system = platform.system().lower()

# ASK FOR FILENAME
filename = input("Source code name: ").strip()
# Check if the file is a .c source code
while not filename.endswith(".c"):
	filename = input("File is not .c source code!\nSource code name: ").strip()
# Check if the file is in the current shell directory
while not any(f.lower() == filename.lower() for f in os.listdir()):
    files = [entry.name for entry in os.scandir() if entry.is_file() and entry.name.lower().endswith(".c")]
    print("Available .c files:", files)  # List available file
    filename = input("File not found!\nSource code name: ").strip()

# ASK FOR OUTPUT NAME
output_name = input("Output name: ")
# Check if output name is correct
while not re.match ("^[a-zA-Z0-9_-]{1,255}$", output_name):
	output_name = input("Output name is not valid!\nOutput name: ").strip().lower()

# ASK FOR METHOD
method = input("Compilation method:\n1. Direct\n2. Step by step\nChoose option: ")
# Check if method is correct
while not method in ["1","2"]:
	method = input("Method not found!\n1. Direct\n2. Step by step\nChoose option: ")

# ASK IF SHOW WARNINGS
global show_warnings
show_warnings = input("Show warnings (y/n): ").strip().lower()
show_warnings = show_warnings == "y"

# ASK IF STANDARD ANSI
global standard_ansi
standard_ansi = input("Use MinGW ANSI Studio compatibility (y/n): ")
show_warnings = show_warnings == "y"

# Basic command
command = (f'gcc {filename}')

def run (command, output, arguments = ""):
	command += f' -o {output} {arguments}'
	# Command addons
	if show_warnings:
		command += " -Wall -Wextra"
	if standard_ansi and system == "windows":
		command += " -D_USE_MINGW_ANSI_STUDIO"
	
	# Code execution
	execution = os.system(command)
	if execution == 0:
		print("Compilation done!")
	else:
		print(execution)

# Select your option
match method:
	case "1":
		run(command, output_name)
	case "2":
		run(command,f'{output_name}.i',"-E")
		run(command,f'{output_name}.s',"-S")
		run(command,f'{output_name}.o',"-c")
		run(command, output_name)

# If you are not on windows ask if you want to compile for Windows system (you need a porting of minGW on for your distribution)
if system != "windows":
	windows = input("Do you want to compile for Windows x86_64? (y/n): ").strip().lower()
	windows = windows == "y"
	if windows:
		run(f'x86_64-w64-mingw32-gcc {filename}', f'{output_name}.exe')