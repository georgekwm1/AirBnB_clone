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
        if not args:
            print("** class name missing **")
        else:
            class_name = args.split()[0]
            try:
                my_instance = eval(class_name)()
                storage.save()
                print(my_instance.id)
            except NameError:
                print("** class doesn't exit **")

    def do_show(self, args):
        """Prints the string representation of an instance"""
        if not args:
            print("** class name missing **")

        else:
            my_args = args.split()
            not_exist = False
            try:
                eval(my_args[0])
            except NameError:
                not_exist = True

            if (not_exist):
                print("** class doesn't exist **")

            elif len(my_args) < 2:
                print("** instance id missing **")

            elif f"{my_args[0]}.{my_args[1]}" not in storage.all().keys():
                print("** no instance found **")

            else:
                key = f"{my_args[0]}.{my_args[1]}"
                print(storage.all()[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if not args:
            print("** class name missing **")

        else:
            my_args = args.split()
            not_exist = False
            try:
                eval(my_args[0])
            except NameError:
                not_exist = True

            if (not_exist):
                print("** class doesn't exist **")

            elif len(my_args) < 2:
                print("** instance id missing **")

            elif f"{my_args[0]}.{my_args[1]}" not in storage.all().keys():
                print("** no instance found **")

            else:
                key = f"{my_args[0]}.{my_args[1]}"
                del storage.all()[key]
                storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances"""
        if not args:
            my_list = [str(storage.all()[key]) for key in storage.all().keys()]
            print(my_list)
        else:
            my_args = args.split()
            not_exist = False
            try:
                eval(my_args[0])
            except NameError:
                not_exist = True

            if not_exist:
                print("** class doesn't exist **")

            else:
                my_list = []
                for obj in storage.all().values():
                    if obj.__class__.__name__ == my_args[0]:
                        my_list.append(str(obj))
                print(my_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        my_dict = storage.all()
        if not args:
            print("** class name missing **")

        else:
            my_args = args.split()
            not_exist = False
            try:
                eval(my_args[0])
            except:
                not_exist = True
            if not_exist:
                print("** class doesn't exist **")

            elif len(my_args) == 1:
                print("** instance id missing **")

            else:
                key = f"{my_args[0]}.{my_args[1]}"
                if key not in my_dict.keys():
                    print(key)
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
                        elif my_value[0] == "-":
                            if my_value.replace("-", "").isdigit():
                                my_value = int(my_value)
                        else:
                            try:
                                my_value = float(my_value)
                            except ValueError:
                                pass
                        my_instance.__dict__[my_args[2]] = my_value
                        my_instance.save()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        HBNBCommand().onecmd(" ".join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
