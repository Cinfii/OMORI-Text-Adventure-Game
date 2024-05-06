# Note: this was done on day 2 technically
import art


print("OMORI")
print("Don't worry, everything is going to be ok. . . ")
print("No matter what happens, promise me that we'll always be there for each other. . . .")
print("Promise me. . . ")

print(art.omori)
print("Welcome to White Space.")
print("You have been here for at long as you can remember")

door = input("You see a door. Open it? y or n.")
if door == "y":
    print("You stared at the door but could not open it.")

laptop = input("Your laptop is in front of you. Use it. Type y or n. ")
if laptop == "y":
    print("You booted up your laptop.")
    what_to_do = input("What would you like to do? Stare at the screen (a), open your journal (b) or log off (c). ")
    if what_to_do == "a":
        print("You stared at the screen.")
    elif what_to_do == "b":
        print("""
        OMORI'S JOURNAL:
        Day ???:
        Today, I spent time in White Space. Everything was ok.""")
    else:
        print("The heat from your laptop warmed your lap. It felt nice.")

tissues = input("You see a box of tissues. Would you like to interact? Type y or n. ")
if tissues == "y":
    print("A tissue box for wiping your sorrows away.")

sketchbook = input("Behind you there is a sketchbook. Open it? Type y or n. ")
if sketchbook == "y":
    print(art.sketchbook1)
    more1 = input("Look at more art? Type y or n. ")
    if more1 == "y":
        print(art.sketchbook2)
        more2 = input("Look at more art? Type y or n. ")
        if more2 == "y":
            print(art.sketchbook3)
            print("You get scared and close the sketchbook.")
    else:
        print("You close the sketchbook.")

cat = input("To your right there is a black cat. Interact? Type y or n. ")
print(art.sketchbook1)
if cat == "y":
    print("MEWO says 'Meow? (Waiting for something to happen?)'")

if door and laptop and tissues and sketchbook and cat == "y":
    print("There was a heavy rumbling, something fell nearby.")
    investigate = input("Investigate? Type y or n. ")
    if investigate == "y":
        direction = input("Which direction will you go? North (n), South (s), East (e), West (w). ")
        while direction != "s":
            print("You find nothing! ")
            direction = input("Which direction will you go? North (n), South (s), East (e), West (w). ")
        if direction == "s":
            print("You got a SHINY KNIFE.")
            print("You decide to go to the door.")
            open_door = input("What do you do? Open the door (y) or do nothing (n).")
            if open_door == "y":
                print("GAME OVER!")
                print("Thank you for playing!!!")


