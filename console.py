#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program by executing EOF"""
        print()
        return True

    def emptyline(self):
        """Empty line method"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in globals():
            print("** class doesn't exist **")
        else:
            new_instance = globals()[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        objects = storage.all()
        if not arg:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            obj = objects.get(key)
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        objects = storage.all()
        if not arg:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            obj = objects.get(key)
            if obj is None:
                print("** no instance found **")
            else:
                del objects[key]
                storage.save()

    def do_all(self, arg):
        """Prints all instances based on the class name"""
        args = arg.split()
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        elif args[0] not in globals():
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in objects.values()
                   if type(obj).__name__ == args[0]])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
