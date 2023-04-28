# Define break points and available commands
BREAK_POINTS = "good bye", "close", "exit"

# Data storage
DATA = {}


# Decorator for handling input errors
def input_error(func):
    """Decorator that handles common input errors for command functions."""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "No such contact!"
        except ValueError:
            return "No such phone number!"
        except TypeError:
            return 'Invalid request! To see available list of commands type "help" '

    return inner


# Command functions
@input_error
def hello(*_):
    """Greet the user."""

    return "How can I help you?"


@input_error
def help(*_):
    """Show a list of available commands and their usage."""

    list_of_instructions = [
        "hello = greeting",
        "add *name* *number* = adding a contact",
        "change *name* *number*= changing an existing contact",
        "phone *name* = number",
        "show_all = reveal the data",
        "help = show all commands",
        f"{BREAK_POINTS} = exit the program",
    ]

    return "\n".join(list_of_instructions)


@input_error
def add(name, phone):
    """Add a new contact to the data."""
    if name in DATA:
        return "Contact already exists!"
    else:
        DATA[name] = phone
        return "successfully added"


@input_error
def change(name, number, *_):
    """Change the phone number for an existing contact."""
    if name in DATA:
        DATA[name] = number
        return "successfully changed"
    else:
        return "No such contact!"


@input_error
def phone(name, *_):
    """Show the phone number for a contact."""

    return DATA[name]


@input_error
def show_all(*_):
    """Show all contacts in the data."""

    return DATA


# Set of command functions
_commands = {
    "hello": hello,
    "add": add,
    "change": change,
    "phone": phone,
    "show_all": show_all,
    "help": help,
}


# command parser
@input_error
def command_parser(input):
    command, *data = input.split(" ")
    return command, *data


# Main loop
@input_error
def main():
    """Main function that runs the program."""
    while True:
        user_input = input("> ").lower()

        if user_input in BREAK_POINTS:
            break

        command, *data = command_parser(user_input)
        if (func := _commands.get(command)) is not None:
            print(func(*data))
        else:
            print(
                "No such command! Please repeat. To see available list of commands type 'help' "
            )

    print("Good bye!")


if __name__ == "__main__":
    main()
