import env
import os


# Main menu where it all starts
def show_main_menu():
    print("1: Wallet(s)")
    print("2: Option 2")
    print("3: Option 3")
    print("4: Option 4")
    print("0: Exit")

# Wallet menu for creating, listing and managing wallets
def show_wallet_menu():
    print("1: List Wallet")
    print("2: Create Wallet")
    print("0: Main Menu")

def get_protocol_params():
    # Dump protocol parameters to temp location
    # cardano-cli shelley query protocol-parameters --mainnet --out-file protocol.json
    cmd_params = env.CCLI
    print(cmd_params)

show_main_menu()
option = int(input("Enter your option:"))

while option != 0:
    if option == 1:
        # do stuff here
        print("You selected option 1")
        show_wallet_menu()
        option = int(input("Enter your option:"))
        while option != 0:
            if option == 1:
                print("You selected option 1")
            elif option == 2:
                print("You selected Option 2")
            else:
                print("Invalid option")
                option = 0
    elif option == 2:
        # do stuff here
        print("You selected option 2")
        get_protocol_params()
    elif option == 3:
        # do stuff here
        print("You selected option 3")
    elif option == 4:
        # do stuff here
        print("You selected option 4")
    else:
        # do stuff here
        print("You selected an  invalid option.")
    show_main_menu()
    option = int(input("Enter your option:"))