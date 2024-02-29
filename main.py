"""
Main file for the buckshot roulette game i want to mimic
"""
import bullets
import player
import dealer
import time

player = player.Player()
dealer = dealer.Dealer()
bullets.checkallbullets()
bullets.loadbullets()
infinite = True

while infinite:
    while len(bullets.gunclip) > 0:
        choice = input("What will you do? Shoot yourself or the dealer?")
        # choice if the user shoots themselves
        if choice == "shoot myself" or choice == "Shoot me" or choice == "Shoot myself":
            # if bullet is live
            if bullets.gunclip[0] == "live":
                time.sleep(1)
                for i in range(1, 4):
                    time.sleep(2)
                    print(i * ".")
                time.sleep(1)
                print("BOOOOOOOM!!")
                time.sleep(2)
                print("A live one...")
                player.sethealth(player.health - 10)
                print(f"Your health is now {player.gethealth()}")
                bullets.gunclip.pop(0)
            # if bullet is a blank
            else:
                time.sleep(1)
                for i in range(1, 4):
                    time.sleep(2)
                    print(i * ".")
                time.sleep(1)
                print("*Click*!")
                time.sleep(2)
                print("A blank...")
                print(f"Your health is still {player.gethealth()}")
                bullets.gunclip.pop(0)

        # choice if the user shoots the dealer
        else:
            # if the bullet is live
            if bullets.gunclip[0] == "live":
                time.sleep(1)
                for i in range(1, 4):
                    time.sleep(2)
                    print(i * ".")
                time.sleep(1)
                print("BOOOOOOOM!!")
                time.sleep(2)
                print("A live one...")
                dealer.sethealth(dealer.health - 10)
                print(f"The dealer's health is now {dealer.gethealth()}")
                bullets.gunclip.pop(0)
            # if bullet is a blank
            else:
                time.sleep(1)
                for i in range(1, 4):
                    time.sleep(2)
                    print(i * ".")
                time.sleep(1)
                print("*Click*!")
                time.sleep(2)
                print("A blank...")
                print(f"The dealer's health is still {dealer.gethealth()}")
                bullets.gunclip.pop(0)

    if player.gethealth() > dealer.gethealth():
        print("Player wins!!")
    else:
        print("You lose...")

    end = input("Do you want to try again?")
    if end == "Yes" or end == "yes":
        infinite = True
    else:
        infinite = False
        print("Goodbye..")
