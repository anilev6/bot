# --------------------NO LIBS WOW-------------------------------------------------------

break_points = ("good bye", "close", "exit")
available_commands = ("hello", "add", "change", "phone", "show_all", "help")

# --------------------DATA STORAGE------------------------------------------------------

data = {}


# --------------------A DECORATOR-------------------------------------------------------


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print("No such contact!")
        except ValueError:
            print("No such phone number!")
        except IndexError:
            print('A wrong request! To see avaliable list of commands type "help" ')

    return inner


# --------------------HANDLERS-------------------------------------------------------


@input_error
def hello(l):
    print("How can I help you?")


@input_error
def help(l):
    print("hello = greeting")
    print("add *name* *number* = adding a contact")
    print("change *name* *number*= chaning an existing contact")
    print("phone *name* = nuber")
    print("show_all = reveal the data")
    print("help = show all commands")
    print(f"{break_points}= kill the bot")


@input_error
def add(l):
    name, phone = l[1], l[2]
    if name in data:
        print("already exists!")
    else:
        data[name] = phone


@input_error
def change(l):
    if l[1] in data.keys():
        data[l[1]] = l[2]
    else:
        print("no such name in a book!")


@input_error
def phone(l):
    print(data[l[1]])


@input_error
def show_all(l):
    print(data)


# --------------------SET OF HANDLERS-----------------------------------------------------
# available_commands=("hello","add","change","phone" ,"show_all","help")
commands = (hello, add, change, phone, show_all, help)


# -----------------------------------MAIN--------------------------------------------------


def main():
    while True:
        user_input = input("> ").lower()

        if user_input in break_points:
            break

        command = user_input.split(" ")[0]
        if command in available_commands:
            index = available_commands.index(command)
            commands[index](user_input.split(" "))

        else:
            print("No such command! Please repeat")

    print("Good bye!")


if __name__ == "__main__":
    main()
