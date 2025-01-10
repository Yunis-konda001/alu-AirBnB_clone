#!/usr/bin/python3
"""
This module provides a command-line interface for the HBNB project.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Define Hbnb command interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit the application.
        """
        return True

    def help_quit(self):
        """
        Quit the application.
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        print("")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
