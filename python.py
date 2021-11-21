import random
import time
import winsound

winsound.PlaySound("smb_coin.wav", winsound.SND_FILENAME)
print("""
██████╗░██╗░░░██╗░██████╗░██████╗██╗░█████╗░███╗░░██╗  
██╔══██╗██║░░░██║██╔════╝██╔════╝██║██╔══██╗████╗░██║  
██████╔╝██║░░░██║╚█████╗░╚█████╗░██║███████║██╔██╗██║  
██╔══██╗██║░░░██║░╚═══██╗░╚═══██╗██║██╔══██║██║╚████║  
██║░░██║╚██████╔╝██████╔╝██████╔╝██║██║░░██║██║░╚███║  
╚═╝░░╚═╝░╚═════╝░╚═════╝░╚═════╝░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝  

██████╗░██╗░░░██╗░█████╗░██╗░░░░░███████╗████████╗████████╗███████╗
██╔══██╗██║░░░██║██╔══██╗██║░░░░░██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝
██████╔╝██║░░░██║██║░░██║██║░░░░░█████╗░░░░░██║░░░░░░██║░░░█████╗░░
██╔══██╗██║░░░██║██║░░██║██║░░░░░██╔══╝░░░░░██║░░░░░░██║░░░██╔══╝░░
██║░░██║╚██████╔╝╚█████╔╝███████╗███████╗░░░██║░░░░░░██║░░░███████╗
╚═╝░░╚═╝░╚═════╝░░╚════╝░╚══════╝╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝

""")
print("Hey lets play russian rulet!")
print("")

time.sleep(1)

print("[1]1player [2]2player [3]endless [4]tutorial")

mode = input("what mode will you like to play >> ")

if mode == "1":
    time.sleep(1)

    print("ya hoo!")

    time.sleep(1)

    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

    winsound.PlaySound("smb_coin.wav", winsound.SND_FILENAME)
    print("""

░██████╗░░█████╗░██╗
██╔════╝░██╔══██╗██║
██║░░██╗░██║░░██║██║
██║░░╚██╗██║░░██║╚═╝
╚██████╔╝╚█████╔╝██╗
░╚═════╝░░╚════╝░╚═╝
    """)


    while True:
        inputt = input("input a guess between 1 and 6 >> ")
        inputt = int(inputt)

        randombullets = random.randint(1,6)

        if inputt == randombullets:
            winsound.PlaySound("smb_gameover.wav", winsound.SND_FILENAME)
            print("""
██████╗░███████╗░█████╗░██████╗░
██╔══██╗██╔════╝██╔══██╗██╔══██╗
██║░░██║█████╗░░███████║██║░░██║
██║░░██║██╔══╝░░██╔══██║██║░░██║
██████╔╝███████╗██║░░██║██████╔╝
╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░
            """)
            break

        else:
            print("well done")
            time.sleep(0.5)
            print("next player!")

            player2 = random.randint(1,6)
            time.sleep(0.5)
            print("player 2 guesses ")
            print(player2)
            time.sleep(0.5)
            print("...")
            time.sleep(0.5)
            print("...")
            time.sleep(0.5)
            print("...")
            randombullets2 = random.randint(1,6)
        
        if player2 == randombullets2:
            winsound.PlaySound("smb_world_clear.wav", winsound.SND_FILENAME)
            print("""
░██╗░░░░░░░██╗██╗███╗░░██╗██╗
░██║░░██╗░░██║██║████╗░██║██║
░╚██╗████╗██╔╝██║██╔██╗██║██║
░░████╔═████║░██║██║╚████║╚═╝
░░╚██╔╝░╚██╔╝░██║██║░╚███║██╗
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝
            """)
            break

if mode == "3":
    time.sleep(1)

    print("ya hoo!")

    time.sleep(1)

    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    while True:
        winsound.PlaySound("smb_coin.wav", winsound.SND_FILENAME)
        print("""

░██████╗░░█████╗░██╗
██╔════╝░██╔══██╗██║
██║░░██╗░██║░░██║██║
██║░░╚██╗██║░░██║╚═╝
╚██████╔╝╚█████╔╝██╗
░╚═════╝░░╚════╝░╚═╝
        """)


        while True:
            inputt = input("input a guess between 1 and 6 >> ")
            inputt = int(inputt)

            randombullets = random.randint(1,6)

            if inputt == randombullets:
                winsound.PlaySound("smb_gameover.wav", winsound.SND_FILENAME)
                print("""
██████╗░███████╗░█████╗░██████╗░
██╔══██╗██╔════╝██╔══██╗██╔══██╗
██║░░██║█████╗░░███████║██║░░██║
██║░░██║██╔══╝░░██╔══██║██║░░██║
██████╔╝███████╗██║░░██║██████╔╝
╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░
                """)
                break

            else:
                print("well done")
                time.sleep(0.5)
                print("next player!")

                player2 = random.randint(1,6)
                time.sleep(0.5)
                print("player 2 guesses ")
                print(player2)
                time.sleep(0.5)
                print("...")
                time.sleep(0.5)
                print("...")
                time.sleep(0.5)
                print("...")
                randombullets2 = random.randint(1,6)
        
            if player2 == randombullets2:
                winsound.PlaySound("smb_world_clear.wav", winsound.SND_FILENAME)
                print("""
░██╗░░░░░░░██╗██╗███╗░░██╗██╗
░██║░░██╗░░██║██║████╗░██║██║
░╚██╗████╗██╔╝██║██╔██╗██║██║
░░████╔═████║░██║██║╚████║╚═╝
░░╚██╔╝░╚██╔╝░██║██║░╚███║██╗
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝
                """)
                break

if mode == "2":
    time.sleep(1)

    print("ya hoo!")

    time.sleep(1)

    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

    winsound.PlaySound("smb_coin.wav", winsound.SND_FILENAME)
    print("""

░██████╗░░█████╗░██╗
██╔════╝░██╔══██╗██║
██║░░██╗░██║░░██║██║
██║░░╚██╗██║░░██║╚═╝
╚██████╔╝╚█████╔╝██╗
░╚═════╝░░╚════╝░╚═╝
    """)


    while True:
        inputt1 = input("player1 >> input a guess between 1 and 6 >> ")
        inputt1 = int(inputt1)

        randombullets = random.randint(1,6)

        if inputt1 == randombullets:
            winsound.PlaySound("smb_gameover.wav", winsound.SND_FILENAME)
            print("""
██████╗░██╗░░░░░░█████╗░██╗░░░██╗███████╗██████╗░░░███╗░░
██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗░████║░░
██████╔╝██║░░░░░███████║░╚████╔╝░█████╗░░██████╔╝██╔██║░░
██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██╔══╝░░██╔══██╗╚═╝██║░░
██║░░░░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║███████╗
╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚══════╝

██████╗░███████╗░█████╗░██████╗░
██╔══██╗██╔════╝██╔══██╗██╔══██╗
██║░░██║█████╗░░███████║██║░░██║
██║░░██║██╔══╝░░██╔══██║██║░░██║
██████╔╝███████╗██║░░██║██████╔╝
╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░
            """)
            break

        inputt2 = input("player2 >> input a guess between 1 and 6 >> ")
        inputt2 = int(inputt2)

        randombullets = random.randint(1,6)

        if inputt2 == randombullets:
            winsound.PlaySound("smb_gameover.wav", winsound.SND_FILENAME)
            print("""
██████╗░██╗░░░░░░█████╗░██╗░░░██╗███████╗██████╗░██████╗░
██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗╚════██╗
██████╔╝██║░░░░░███████║░╚████╔╝░█████╗░░██████╔╝░░███╔═╝
██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██╔══╝░░██╔══██╗██╔══╝░░
██║░░░░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║███████╗
╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚══════╝

██████╗░███████╗░█████╗░██████╗░
██╔══██╗██╔════╝██╔══██╗██╔══██╗
██║░░██║█████╗░░███████║██║░░██║
██║░░██║██╔══╝░░██╔══██║██║░░██║
██████╔╝███████╗██║░░██║██████╔╝
╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░
            """)
            break

if mode == "4":
    print("""
    the way you play russain roulette is theres
    5 blanks and 1  bullet iis a very random sort of game
    just guess a number and then the computer
    wil guess unless your in two player
        """)
    
    print("[1]1player [2]2player [3]endless [4]tutorial")

    mode = input("what mode will you like to play >> ")