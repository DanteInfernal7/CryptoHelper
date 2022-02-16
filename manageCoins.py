import keyboard as keyboard

import dbConnect
myDb = dbConnect.dbConnector()
myCursor = myDb.cursor()

def temp():
    print("Select function:\n1.Add Coin to Track\n2.Remove Coin from List\n3.Display Coins ")
    choice = input()

    if choice == "1":
        addCoin()
    elif choice == "2":
        removeCoin()
    elif choice == "3":
        display()
    else:
        print("Invalid Input")

def display():
    myCursor.execute('SELECT * FROM coins')
    coins = myCursor.fetchall()

    for coin in coins:
        print(coin)

def addCoin():
    val = []
    looper = "y"
    myCursor.execute('SELECT coin_id FROM coins ORDER BY coin_id DESC LIMIT 1')
    last = int((myCursor.fetchall()[0])[0])
    display()
    while looper == "y":
        last = last + 1
        name = input("Enter coin name: ")
        dispname = input("Enter coin display name: ")
        temp = (last,name,dispname)
        val.append(temp)
        del temp
        looper = input("Are there more entries? \n y or n? ")
    query = "INSERT INTO coins (coin_id, coin_name, coin_display_name) VALUES (%s, %s, %s)"
    myCursor.executemany(query,val)
    del val
    myDb.commit()
    display()

def removeCoin():
    looper = "y"
    display()
    while looper == "y":
        id = input("Enter coin ID to remove: ")
        myCursor.execute('DELETE FROM coins WHERE coin_id = ' + id)
        myDb.commit()
        looper = input("Are there more deletions? \n y or n? ")


