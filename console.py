import cmd

class HBNBCommand(cmd.Cmd):
    """HBNB Command Line Interface"""
prompt = "(hbnb) "

def do_EOF(self, line):
    """"This is the EOF function that exits the command loop"""
    return True

def do_something(self, line):
    print(line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()