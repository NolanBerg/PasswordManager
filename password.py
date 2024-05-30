RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'

pwd = input("Enter the master password: ")

masterpswd = "1"
attempts = 0
while pwd != masterpswd:
    if attempts >= 3:
        print(f"\n{RED}You have no more password attempts.{RESET}")
        quit()
    pwd = input(f"\n{RED}The password you entered is incorrect.{RESET}\n\nEnter the master password: ")
    attempts += 1
    

def view():
    with open("password.txt", "r") as f:
        print("\n")
        for line in f.readlines():
            print(line.rstrip())

def add():
    website = input("\nWhat website is this password for: ")
    username = input("\nEnter username: ")
    password = input("\nEnter password: ")

    with open("password.txt", "a") as f:
        f.write(f"{GREEN}{website} {RESET}\n\n    {BLUE}username:{RESET} {username} {GREEN}|{RESET} {BLUE}password:{RESET} {password}\n\n")

while True:
    mode = input("\nType view, add, or quit to manage password list: ").strip().lower()
    if mode == "quit":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print(f"\n{RED}INVALID ENTRY{RESET}")
        continue
