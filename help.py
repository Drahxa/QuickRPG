from tkinter import *
import random

window = Tk()
rootHeight = 1700
rootWidth  = 2000
screenHeight = window.winfo_screenheight()
screenWidth  = window.winfo_screenwidth()
x = (screenWidth  / 2 ) - (rootWidth  / 2)
y = (screenHeight / 2 ) - (rootHeight / 2)

window.geometry(f'{rootHeight}x{rootWidth}+{int(x)}+{int(y)}')
turn = 0
def battle():
   global level, lvlup, upgs, turn, enemy, elist, ekill, health, healthe, attack, attacke, heal, amin, amax, aemin, aemax, hmin, hmax, hemin, hemax
   while healthe > 0 and health > 0:
     turn += 1
     if turn % 2 == 0:
      echose = ["0", "1"]
      turne = random.choice(echose)

      #if 1 is selected, they will attack
      if turne == "1":
        attacke = random.randint(aemin, aemax)
        health = health - attacke
        midLabel.config(text = (f"{enemy} has attacked you... - {attacke}Hp\nYour hp: {health}\n\n"))
      #if 1 not selected, they will heal
      else:
        heal = random.randint(hemin, hemax)
        healthe += heal
        midLabel.config(text = (f"{enemy} has chosen Heal and healed {heal} Hp"))
        midLabel.config(text = (f"{enemy} now has {healthe}Hp\n\nYour turn."))
    #if its not the enemy turn, its player turn 
     else:
      midLabel.config(text=(f"Your turn"))
      #if they choose attack, the enemy will lose hp
      if choice == "a":
        attack = random.randint(amin, amax)
        healthe = healthe - attack
        print(f"\nYou attacked {enemy}... - {attack}Hp\n{enemy}'s hp: {healthe}\n\n")
      #if not, the player will heal
      else:
        heal = random.randint(hmin, hmax)
        health += heal
        print(f"\nYou healed {heal}Hp, You now have {health}Hp\n\n")

def player():
  global health, amin, amax, hmin, hmax
  health = 20
  amin = 5 #Min player attack
  amax = 10 #Max player attack
  hmin = 5 #Min player heal
  hmax = 15 #Max player heal

#My self selected stats
def slime():
  global enemy, healthe, aemin, aemax, hemin, hemax
  enemy = "Slime"
  healthe = 10 
  aemin = 3  #Min enemy attack
  aemax = 7 #Max enemy attack
  hemin = 2  #Min enemy heal
  hemax = 3 #Max enemy heal


#ADD LEVEL TO PLAYER LABEL
midLabel = Label(window, text = "One goal...\n\n                 SURVIVE\n\n\nYou're given the ability to attack and heal yourself. Encounter with enemies may happen...\n\n", font=("", 20)).grid(row=1, column = 2)
player()
slime()
enemyStat = Label(window, text = f"Player:\n\n\nHealh = {health}\n\nATK = {amin}-{amax}\n\nHeal = {hmin}-{hmax}", font = ("", 20)).grid(row=1, column = 1, padx=(1, 200))
playerStat = Label(window, text = f"{enemy}:\n\n\nHealh = {healthe}\n\nATK = {aemin}-{aemax}\n\nHeal = {hemin}-{hemax}", font = ("", 20)).grid(row=1, column = 3, padx=(200, 100))

buttonWander = Button(window, text = "Wander Around").grid(row=4)
buttonAttack = Button(window, text = "Attack").grid(row = 3, column = 2)
buttonHeal = Button(window, text = "Heal").grid(row = 3, column = 3)
buttonUpgMinA = Button(window, text = "Upg Min ATK").grid(row=2, column = 1)
buttonUPgMaxA = Button(window, text = "Upg Max ATK").grid(row=2, column = 2)
buttonUPgMinH = Button(window, text = "Upg Min Heal").grid(row=2, column = 3)
buttonUpgmaxH = Button(window, text = "Upg Max Heal").grid(row=2, column = 4)

window.mainloop()