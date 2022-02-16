import manageCoins
import updatePrice
import displayPrice

def main():
    cont = "y"
    while cont == "y":
        print("Select function you want to access:\n1.Manage Coins\n2.Watch Prices\n3.Exit ")
        choice = input()

        if choice == "1":
            manageCoins.temp()
        elif choice == "2":
            displayPrice()
        elif choice == "3":
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()