# Define break points and available commands
BREAK_POINTS = ("good bye", "close", "exit")
AVAILABLE_COMMANDS = ("hello", "add", "change", "phone", "show_all", "help")

# Data storage
DATA = {}


# Decorator for handling input errors
def input_error(func):
    """Decorator that handles common input errors for command functions."""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print("No such contact!")
        except ValueError:
            print("No such phone number!")
        except IndexError:
            print('Invalid request! To see available list of commands type "help" ')

    return inner


# Command functions
@input_error
def hello(*_):
    """Greet the user."""
    print("How can I help you?")


@input_error
def help(*_):
    """Show a list of available commands and their usage."""
    print("hello = greeting")
    print("add *name* *number* = adding a contact")
    print("change *name* *number*= changing an existing contact")
    print("phone *name* = number")
    print("show_all = reveal the data")
    print("help = show all commands")
    print(f"{BREAK_POINTS} = exit the program")


@input_error
def add(arguments):
    """Add a new contact to the data.
    arguments is a list made of input: input.split(' ')"""
    name, phone = arguments[1], arguments[2]
    if name in DATA:
        print("Contact already exists!")
    else:
        DATA[name] = phone


@input_error
def change(arguments):
    """Change the phone number for an existing contact.
    arguments is a list made of input: input.split(' ')"""
    if arguments[1] in DATA:
        DATA[arguments[1]] = arguments[2]
    else:
        print("No such contact!")


@input_error
def phone(arguments):
    """Show the phone number for a contact.
    arguments is a list made of input: input.split(' ')"""
    print(DATA[arguments[1]])


@input_error
def show_all(*_):
    """Show all contacts in the data.
    arguments is a list made of input: input.split(' ')"""
    print(DATA)


# Set of command functions
COMMANDS = (hello, add, change, phone, show_all, help)


# Main loop
def main():
    """Main function that runs the program."""
    while True:
        user_input = input("> ").lower()

        if user_input in BREAK_POINTS:
            break

        command = user_input.split(" ")[0]
        if command in AVAILABLE_COMMANDS:
            index = AVAILABLE_COMMANDS.index(command)
            COMMANDS[index](user_input.split(" "))
        else:
            print("No such command! Please repeat")

    print("Good bye!")


if __name__ == "__main__":
    main()
