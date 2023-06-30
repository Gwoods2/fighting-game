from random import choice

def print_choices():
    print("What do you do?")
    print("1. mash buttons")
    print("2. anti-air")
    print("3. block")
    print("4. throw")
    print("5. wait.")

def boss_rush():
    print("Finally, his patience breaks and he rushes at you and starts swinging.")
    print_choices()
    r4 = input("> ")
    if r4 == "3":
        print("You block his attacks, patiently waiting for you chance to punish.")
        print("You then combo him for his whole life bar!")
        return True
    else:
        print("While you were trying to do that, he combos you for your whole life bar!")
        return False
    
def boss_jump():
    print("Finally, his patience breaks and he jumps in.")
    print_choices()
    r4 = input("> ")
    if r4 == "2":
        print("You hit him with an anti-air, then combo him for his entire life bar!")
        return True
    else:
        print("While you were trying to do that, his foot hits your face.")
        print("He then combos you for your entire life bar.")
        return False
    
def boss_turtle():
    print("He decides to play it safe and shoot projectiles from far away.")
    print_choices()
    r4 = input("> ")
    if r4 == "4":
        print("You walk up, carefully avoiding his projectiles.")
        print("Then you grab him and suplex him!")
        return True
    else:
        print("It's no use, he's too far away for that to work and he hits you with a projectile every time you try.")
        return False
    
boss_random = [boss_rush, boss_jump, boss_turtle]

def round_1():
    print("Your opponent looks like a panic masher.")
    print("ROUND ONE\nFIGHT")
    print("Your opponent immediately dashes at you and starts punching.")
    print_choices()
    r1 = input("> ")

    if r1 == "1":
        print("You try to mash buttons back, but his attacks are faster.")
        print("He keeps punching you until your character falls down.")
        return False

    elif r1 == "2":
        print("You try to hit him with a Shoryuken.")
        print("Unfortunately, you miss, and then he combos you to pieces.")
        return False

    elif r1 == "3":
        print("You block his attacks.")
        print("You patiently wait for your opponent to throw out an unsafe move, then punish it with a combo.")
        print("YOU WIN!")
        return True

    elif r1 == "4":
        print("You try to throw your opponent.")
        print("Unfortunately, he keeps punching you during the startup frames.")
        print("Stupid rushdowns.")
        return False

    elif r1 == "5":
        print("You wait patiently, to try to figure out what your opponent is going to do.")
        print("Unfortunately, your opponent does not respect your waiting and keeps punching you in the face.")
        return False

def round_2():
    print("Your opponent looks like a jumper.")
    print("ROUND TWO\nFIGHT")
    print("Your opponent immediately jumps at you.")
    print_choices()
    r2 = input("> ")

    if r2 == "1":
        print("You try to mash buttons, but he jumps over you and combos off of the air attack.")
        print("He keeps punching you until your character falls down.")
        return False

    elif r2 == "2":
        print("You try to hit him with a Shoryuken.")
        print("It easily intercepts him out of the air.")
        print("You then proceed to juggle him for his entire health bar.")
        print("YOU WIN!")
        return True

    elif r2 == "3":
        print("You block his attacks.")
        print("Unfortunately, he then follows with a sweep and combos you.")
        return False

    elif r2 == "4":
        print("You try to throw your opponent.")
        print("Unfortunately, he is not on the ground to grab.")
        print("He then hits you with the air attack and combos you to death.")
        return False

    elif r2 == "5":
        print("You wait patiently, to try to figure out what your opponent is going to do.")
        print("Unfortunately, while you are thinking his foot hits your face and he combos you for your entire life bar.")
        return False
    
def round_3():
    print("Your opponent looks like a turtle.")
    print("ROUND THREE\nFIGHT")
    print("Your opponent immediately dashes backwards and crouch blocks.")
    print_choices()
    r3 = input("> ")

    if r3 == "1":
        print("You try to mash buttons, but he blocks all of them.")
        print("Every time you use an unsafe attack he follow with a punish and goes back to blocking.")
        return False

    elif r3 == "2":
        print("You try to hit him with a Shoryuken.")
        print("It misses and he punishes.")
        return False

    elif r3 == "3":
        print("You try to block his attacks.")
        print("Unfortunately, he does not approach.")
        print("He keeps shooting projectiles and doing chip damage until you are knocked out.")
        return False

    elif r3 == "4":
        print("You try to throw your opponent.")
        print("You walk over slowly, blocking his occiaisonal projectiles.")
        print("You grab him, spin him up into the air, and slam him down hard on the ground.")
        print("YOU WIN!")
        return True

    elif r3 == "5":
        print("You wait patiently, to try to figure out what your opponent is going to do.")
        print("Unfortunately, while you are thinking he keeps shooting projectiles until the chip damage knocks you out.")
        return False

def round_4():
    print("Your opponent looks... thoughtful.")
    print("ROUND FOUR\nFIGHT")
    print("Your opponent steps back and forth, trying to sus out what you will do.")
    print_choices()
    r3 = input("> ")

    if r3 == "1":
        print("You try to mash buttons, but he blocks all of them.")
        print("When you slip and use an unsafe attack, he punishes and combos you to death.")
        return False

    elif r3 == "2":
        print("You try to hit him with a Shoryuken.")
        print("It misses and he punishes.")
        return False

    elif r3 == "3":
        print("You try to block his attacks.")
        print("Unfortunately, he does not approach.")
        print("He keeps shooting projectiles and doing chip damage until you are knocked out.")
        return False

    elif r3 == "4":
        print("You try to throw your opponent.")
        print("Every time you get close, he starts using fast safe attacks.")
        print("He eventually chews through your entire life bar.")
        return False

    elif r3 == "5":
        print("You wait patiently, to try to figure out what your opponent is going to do.")
        print("He hasn't commited to anything yet, but you know you can get him to slip up.")
        win_r4 = choice(boss_random)()
        if win_r4 == True:
            return True
        else:
            return False



print("You enter your first fighting game tournament!")
win = round_1()
# print(f"Did the win work? {win}")

if win == True:
    print("\n")
    win = round_2()
    # print(f"Did r2 win work? {win}")
else:
    print("GAME OVER")

if win == True:
    print("\n")
    win = round_3()
    # print(f"Did r3 work? {win}")
else:
    print("GAME OVER")

if win == True:
    print("\n")
    win = round_4()
else:
    print("GAME OVER")

if win == True:
    print("\n")
    print("You are the new Fighting Game champion!\nHuzzah!")
else:
    print("GAME OVER")