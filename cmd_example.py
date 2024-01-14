import cmd

class MyCmdInterpreter(cmd.Cmd):
    prompt = "(hbnb) "

    def do_greet(self, line):
        """Greet the user."""
        print("Hello,", line)

    def do_add(self, line):
        """Add two numbers."""
        try:
            numbers = [float(x) for x in line.split()]
            result = sum(numbers)
            print("Sum:", result)
        except ValueError:
            print("Invalid input. Please provide numbers.")

    def do_exit(self, line):
        """Exit the interpreter."""
        print("Exiting the interpreter.")
        return True

if __name__ == "__main__":
    interpreter = MyCmdInterpreter()
    interpreter.cmdloop("Welcome to MyCmdInterpreter. Type 'help' for available commands.")
