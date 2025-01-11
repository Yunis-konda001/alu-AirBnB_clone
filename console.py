#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB clone."""
    
    # Custom prompt
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF signal."""
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """Override the default behavior to do nothing on an empty line."""
        pass

    def help_quit(self):
        """Help information for quit command."""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help information for EOF command."""
        print("EOF command to exit the program")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
