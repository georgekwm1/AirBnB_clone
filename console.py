#!/usr/bin/python3
"""Defines the HBNBCommand class."""
import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """The HBNBCommand class."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, args):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel."""
        classes = [Amenity, BaseModel, City, Place, Review, State, User]
        if not args:
            print("** class name missing **")
        else:
            class_found = False
            for cls in classes:
                if args == cls.__name__:
                    my_instance = cls()
                    my_instance.save()
                    print(my_instance.id)
                    class_found = True
                    break
                if not class_found:
                    print("** class doesn't exit **")

    def do_show(self, args):
        """ Prints the string representation of an instance"""
        classes = [Amenity, BaseModel, City, Place, Review, State, User]
        if not args:
            print("** class name missing **")
        else:
            for cls in classes:
                my_args = args.split()
                if my_args[0] != f"{cls}":
                    print("** class doesn't exist **")

                elif len(my_args) < 2:
                    print("** instance id missing **")

                elif f"{cls}.{my_args[1]}" not in storage.all().keys():
                    print("** no instance found **")

                else:
                    key = f"{cls}.{my_args[1]}"
                    my_instance = cls.__name__(storage.all()[key])
                    print(my_instance)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        classes = [Amenity, BaseModel, City, Place, Review, State, User]
        if not args:
            print("** class name missing **")

        else:
            for cls in classes:
                my_args = args.split()
                if my_args[0] != f"{cls}":
                    print("** class doesn't exist **")

                elif len(my_args) < 2:
                    print("** instance id missing **")

                elif f"{cls}.{my_args[1]}" not in storage.all().keys():
                    print("** no instance found **")

                else:
                    key = f"{cls}.{my_args[1]}"
                    del storage.all()[key]
                    storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances"""

        my_dict = storage.all()
        my_list = []
        if not args or args == "BaseModel":
            for key in my_dict.keys():
                my_instance = BaseModel(**my_dict[key])
                my_list.append(str(my_instance))
            print(my_list)

        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """ Updates an instance based on the class name and id"""

        my_dict = storage.all()
        if not args:
            print("** class name missing **")
        else:
            my_args = args.split()
            if my_args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(my_args) == 1:
                print("** instance id missing **")
            else:
                key = f"BaseModel.{my_args[1]}"
                if key not in my_dict.keys():
                    print("** no instance found **")
                else:
                    if len(my_args) == 2:
                        print("** attribute name missing **")
                    elif len(my_args) == 3:
                        print("** value missing **")
                    else:
                        my_instance = my_dict[key]
                        my_value = my_args[3]
                        if my_value[0] == '"' and my_value[-1] == '"':
                            my_value = my_value.strip('"')
                        elif my_value.isdigit():
                            my_value = int(my_value)
                        elif my_value[0] == '-':
                            if my_value.replace('-', '').isdigit():
                                my_value = int(my_value)
                        else:
                            try:
                                my_value = float(my_value)
                            except ValueError:
                                pass
                        my_dict[key][my_args[2]] = my_value
                        my_instance = BaseModel(**my_dict[key])
                        my_instance.save()


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
