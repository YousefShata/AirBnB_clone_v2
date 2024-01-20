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
        if obj:
            if (obj == "BaseModel"):
                mod = BaseModel()
                mod.save()
                print(mod.id)
            elif (obj == "User"):
                mod = User()
                mod.save()
                print(mod.id)
            elif (obj == "Place"):
                mod = Place()
                mod.save()
                print(mod.id)
            elif (obj == "State"):
                mod = State()
                mod.save()
                print(mod.id)
            elif (obj == "City"):
                mod = City()
                mod.save()
                print(mod.id)
            elif (obj == "Amenity"):
                mod = Amenity()
                mod.save()
                print(mod.id)
            elif (obj == "Review"):
                mod = Review()
                mod.save()
                print(mod.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

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
