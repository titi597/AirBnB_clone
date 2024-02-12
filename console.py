#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        print(all_objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        del all_objects[key]
        storage.save()

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(all_objects[key], args[2], args[3])
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
            return
        args = arg.split()
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in objects.items() if args[0] in key])

    def do_quit(self, arg):
        """Quits the command line"""
        return True

    def do_EOF(self, arg):
        """Exits the command line"""
        return True

    def emptyline(self):
        """Handles empty line"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
