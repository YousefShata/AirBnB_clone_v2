#!/usr/bin/python3
"""
Command interpreter to control models
"""
import cmd
from models.base_model import BaseModel
import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNB class
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        Quit the cmd
        """
        return True

    def do_EOF(self, line):
        """
        End of File
        """
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass

    def do_create(self, obj):
        """
        Create a BaseModel Object
        """
        all_classes = [
               "BaseModel", "User", "Place", "State",
               "City", "Amenity", "Review"]

        args = obj.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in all_classes:
            print("** class doesn't exist **")
            return

        args = args[1:]

        if len(args) == 0:
            obj = globals()[class_name]()
            obj.save()
            print(obj.id)
            return

        params = {}
        for param in args:
            key_value = param.split('=')
            if len(key_value) == 2:
                key, value = key_value
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1].replace('_', ' ').replace('\\"', '"')
                elif '.' in value and all(
                    part.isdigit()
                    or (part.startswith('-') and part[1:].isdigit())
                    for part in value.split('.')
                ):
                    value = float(value)

                elif (
                    value.isdigit() or
                    (value[0] == '-' and value[1:].isdigit())
                ):
                    value = int(value)

                else:
                    continue

                params[key] = value

        obj = globals()[class_name](**params)
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """
        Show Data about a specific instance based on the Id
        """
        if len(arg) > 0:
            args = arg.split()
            name = args[0]
            all_classes = [
                "BaseModel", "User", "Place", "State",
                "City", "Amenity", "Review"]
            if name in all_classes:
                if len(args) > 1:
                    id = args[1]
                    all_values = models.storage.all()
                    search_string = f"{name}.{id}"
                    if search_string in all_values:
                        print(all_values[search_string])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """
        Delete a specific entry
        """
        if len(arg) > 0:
            args = arg.split()
            name = args[0]
            all_classes = [
                "BaseModel", "User", "Place", "State",
                "City", "Amenity", "Review"]
            if name in all_classes:
                if len(args) > 1:
                    id = args[1]
                    all_values = models.storage.all()
                    search_string = f"{name}.{id}"
                    if search_string in all_values:
                        del all_values[search_string]
                        models.storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """
        Show all instences
        """
        final_list = []
        all_values = models.storage.all()
        if len(arg) > 0:
            all_classes = [
                "BaseModel", "User", "Place", "State",
                "City", "Amenity", "Review"]
            if arg in all_classes:
                final_dic = {}
                for key, value in all_values.items():
                    if key.startswith(f"{arg}."):
                        final_list.append(str(value))
                print(final_list)
            else:
                print("** class doesn't exist **")
        else:
            for key, value in all_values.items():
                final_list.append(str(value))
            print(final_list)

    def do_update(self, arg):
        """
        Update a specific instence
        """
        if len(arg) > 0:
            args = arg.split()
            name = args[0]
            all_classes = [
                "BaseModel", "User", "Place", "State",
                "City", "Amenity", "Review"]
            if name in all_classes:
                if len(args) > 1:
                    id = args[1]
                    all_values = models.storage.all()
                    search_string = f"{name}.{id}"
                    if search_string in all_values:
                        if len(args) > 2:
                            attr = args[2]
                            if len(args) > 3:
                                val = args[3]
                                setattr(all_values[search_string], str(
                                    attr), str(val))
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
