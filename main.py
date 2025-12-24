import sys
import shutil
import subprocess
import os
#TestChange123
def main():
    while True:
        sys.stdout.write("$ ")
        command = input()

        # Split the input into parts
        split_input = command.split()
        if not split_input:
            continue  # nothing was typed

        type_cmd = split_input[0]  # this is the program / builtin
        args = split_input[1:]     # these are the arguments

        builtins = ["echo", "exit", "type", "pwd"]

        # Builtin commands
        if type_cmd == "exit":
            sys.exit(0)
        elif type_cmd == "echo":
            sys.stdout.write(" ".join(args) + "\n")
        elif type_cmd == "type":
            # Example for type builtin
            command_path = shutil.which(args[0]) if args else None
            if args and args[0] in builtins:
                sys.stdout.write(f"{args[0]} is a shell builtin\n")
            elif command_path is not None and os.access(command_path, os.X_OK):
                sys.stdout.write(f"{args[0]} is {command_path}\n")
            else:
                sys.stdout.write(f"{args[0]}: not found\n")
        elif type_cmd == "pwd":
            pwd = os.getcwd()
            sys.stdout.write(f"{pwd} \n")

        # External programs
        else:
            # Find executable in PATH
            exe_path = shutil.which(type_cmd)

            if exe_path:  # If found
                subprocess.run([type_cmd] + args)
            else:
                sys.stdout.write(f"{type_cmd}: command not found\n")

if __name__ == "__main__":
    main()