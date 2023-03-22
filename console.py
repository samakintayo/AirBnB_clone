#!/usr/bin/python3
"""This program contains the entry point of the command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """the HBNB Command Interpreter.

    Attributes:
        prompt (str): a custom prompt string
    """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program.
        """
        return True

    def emptyline(self):
        """Handles empty line input.
        """
        return

    def do_EOF(self, line):
        """Handles end-of-file marker."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
