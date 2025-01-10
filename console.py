#!/usr/bin/python3
"""
This module provides a command-line interface for the HBNB project.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    A command-line interface for the HBNB project.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit the application.
        """
        return True

    def help_quit(self, arg):
        """
        Quit the application.

        This method is called when the user enters the 'quit' command.
        It returns True to exit the command loop.
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        Handles the EOF (End Of File) signal.
        """
        print()
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
