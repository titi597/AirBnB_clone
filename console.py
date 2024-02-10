#!/usr/bin/python3
"""the console."""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
