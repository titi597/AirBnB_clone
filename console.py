#!/usr/bin/env python3
"""
This module contains the entry point of the command interpreter.
"""
import cmd
import sys
import models


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """

    prompt = "(hbnb) "

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it to the JSON file, and prints the id.
        Usage: create <class name>
        """
        if not line:
            print("** class name missing **")
            return

        try:
            new_instance = models.classes[line]()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key in models.storage.all():
            print(models.storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        Usage: destroy <class name> <id>
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key in models.storage.all():
            del models.storage.all()[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all [<class name>]
        """
        args = line.split()
        obj_list = []

        if not args:
            for obj in models.storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
            return

        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return

        for key, obj in models.storage.all().items():
            if args[0] == key.split('.')[0]:
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in models.storage.all():
            print("** no instance found **")
            return

        obj = models.storage.all()[key]
        setattr(obj, args[2], args[3].strip('"'))
        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
