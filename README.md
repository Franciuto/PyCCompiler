
# PyCCompiler

**PyCCompiler** is a Python script for compiling C source files using the GCC compiler. The script is designed to work on both Windows and Unix-like systems (Linux, macOS, etc.) and offers features such as cross-platform compilation for Windows from Linux systems, warning management, and support for MinGW ANSI Studio.


## Key Features

- **Multi-Platform Support**: Compatible with Windows and Unix-like systems (Linux, macOS).
- **Cross-Platform Compilation**: Ability to compile executables for Windows x86_64 from Linux systems using `x86_64-w64-mingw32-gcc`.
- **Warning Management**: Option to enable or disable warnings during compilation (`-Wall -Wextra`).
- **Support for MinGW ANSI Studio**: Compatibility with MinGW ANSI Studio on Windows systems.
- **User-Friendly Interface**: Interactive input to guide users through the compilation process.

## Requirements

To use **PyCCompiler**, make sure you have the following tools installed:

- **Python 3.x**: The script is written in Python 3.
- **GCC (GNU Compiler Collection)**: Required to compile C source files.
- **x86_64-w64-mingw32-gcc** (only for cross-platform compilation): If you want to compile for Windows from a Linux system, install this package for your distrubution.


## Installation and usage

1. Clone this repository or download the Python script:
   ```bash
   git clone https://github.com/Franciuto/PyCCompiler.git
 2. Open a terminal and go in the folder where your `.c` source code is stored
 3. Start the script from the terminal using `python`
 4. Compile
