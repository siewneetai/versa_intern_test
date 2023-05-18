import json


def run_predictor():
    result = []
    for count in range(1, 101):
        if count % 3 == 0 and count % 5 == 0:
            result.append("BIG BANG")
        elif count % 3 == 0:
            result.append("BIG")
        elif count % 5 == 0:
            result.append("BANG")
        else:
            result.append(count)
    display_result(result)
    write_to_file(result)


def display_result(data):
    num = 1
    for result in data:
        print(f"{num}: {result}")
        num = num+1


def write_to_file(data):
    with open('output.json', 'w') as file:
        json.dump(data, file)
        print("The output has been generated in output.json")


def display_menu():
    print("=" * 180)
    print(f"{'BIG BANG PREDICTOR' : ^180}")
    print("=" * 180)
    print(f"{'=====Choose Menu=====' : ^180}\n")
    print(f"{'1 - Run Predictor      2 - Exit' : ^180}\n")
    print("=" * 180)
    try:
        user_code = int(input("Enter your choice to proceed: "))  # accept user input for user_code
        if user_code == 1:
            run_predictor()
        elif user_code == 2:
            exit()
            print("\nPlease provide valid code!")  # display error message
    except ValueError:
        print("\nInvalid Input")  # if the value input is not integer then error message will be displayed


display_menu()
