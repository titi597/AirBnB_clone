#!/usr/bin/python3
"""the console."""
import cmd
import json
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()  # Print a new line before exiting
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id"""
        if not arg:
            print("** class name missing **")
            return
        classes = {"BaseModel": BaseModel, "User": User}
        args = arg.split()
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        try:
            with open("file.json", 'r') as file:
                objs = json.load(file)
        except FileNotFoundError:
            print("** no instance found **")
            return
        if key not in objs.keys():
            print("** no instance found **")
        else:
            print(objs[key])

    def do_destroy(self, arg):
        """Deletes an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        try:
            with open("file.json", 'r') as file:
                objs = json.load(file)
        except FileNotFoundError:
            print("** no instance found **")
            return
        if key not in objs.keys():
            print("** no instance found **")
        else:
            del objs[key]
            with open("file.json", 'w') as file:
                json.dump(objs, file)

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        try:
            with open("file.json", 'r') as file:
                objs = json.load(file)
        except FileNotFoundError:
            print("[]")
            return
        objs_list = [str(obj) for key, obj in objs.items() if args[0] in key]
        print(objs_list)

    def do_update(self, arg):
        """Updates an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        try:
            with open("file.json", 'r') as file:
                objs = json.load(file)
        except FileNotFoundError:
            print("** no instance found **")
            return
        if key not in objs.keys():
            print("** no instance found **")
            return
        if args[2] in ["id", "created_at", "updated_at"]:
            print("** attribute can't be updated **")
            return
        obj = objs[key]
        setattr(obj, args[2], args[3])
        objs[key] = obj
        with open("file.json", 'w') as file:
            json.dump(objs, file)

    def emptyline(self):
        """Do nothing on empty input line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
