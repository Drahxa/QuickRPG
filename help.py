from tkinter import *
import random
import time

window = Tk()
rootHeight = 1700
rootWidth  = 2000
screenHeight = window.winfo_screenheight()
screenWidth  = window.winfo_screenwidth()
x = (screenWidth  / 2 ) - (rootWidth  / 2)
y = (screenHeight / 2 ) - (rootHeight / 2)

window.geometry(f'{rootHeight}x{rootWidth}+{int(x)}+{int(y)}')
level = 1
turn = 0
upgs = 0
enemies = [0, 1, 2, 3, 4]
ekill = 0




def battle():
   global level, lvlup, upgs, turn, enemy, ekill, health, healthe, attack, attacke, heal, amin, amax, aemin, aemax, hmin, hmax, hemin, hemax
   while healthe > 0 and health > 0:
     turn += 1
     if turn % 2 == 0:
      echose = ["0", "1"]
      turne = random.choice(echose)

      #if 1 is selected, they will attack
      if turne == "1":
        attacke = random.randint(aemin, aemax)
        health = health - attacke
        midLabel.config(text = (f"{enemy} has attacked you... -{attacke}Hp"))
        labelUpdate()
        print("LABEL SHOULD BE UPDATED ")
      #if 1 not selected, they will heal
      else:
        heal = random.randint(hemin, hemax)
        healthe += heal
        midLabel.config(text = (f"{enemy} has chosen Heal and healed +{heal}Hp\nYour turn."))
        labelUpdate()
    #if its not the enemy turn, its player turn 
     
     else:
      midLabel.config(text=(f"Your turn"))
      #if they choose attack, the enemy will lose hp
      pturnButtonsOnly()
      if choice == "a":
        attack = random.randint(amin, amax)
        healthe = healthe - attack
        midLabel.config(text = (f"\nYou attacked {enemy}... -{attack}Hp"))
        eturn()
      #if not, the player will heal
      else:
        heal = random.randint(hmin, hmax)
        health += heal
        midLabel.config(text = (f"\nYou healed +{heal}Hp"))
        labelUpdate()
        eturn()
   
   if healthe > health and health <= 0:
    midLabel.config(text = (f"{enemy} has beaten you."))
    turn = 0
    level = -1
    midLabel.config(text = (f"You've defeated a total of {ekill} enemies!"))
    #If enemy not won, Congratulate player
   else:
    midLabel.config(text = (f"Congrats, You've beat {enemy}!\n\n\n"))
    level += 1
    ekill += 1
    turn = 0

    lvlup = random.choice(echose)
    if lvlup == 1:
      midLabel.config(text = "You've gained a Level up!\nWhich attribute wuould you like to upgrade by 3?")
      upgradeButtonsOnly()
      if lvlup == "1":
        amin += 3
        upgs += 1
        labelUpdate()
        addEnemy()

      elif lvlup == "2":
        amax += 3
        upgs += 1
        labelUpdate()
        addEnemy()
      elif lvlup == "3":
        hmin += 3
        upgs += 1
        labelUpdate()
        addEnemy()
      elif lvlup == "4":
        hmax += 3
        upgs += 1
        labelUpdate()
        addEnemy()

    else:
      midLabel.config(text = "Only one choice available...")
      wanderonly()



def player():
  global health, amin, amax, hmin, hmax
  health = 20
  amin = 5 #Min player attack
  amax = 10 #Max player attack
  hmin = 5 #Min player heal
  hmax = 15 #Max player heal

def slime():
  global enemy, healthe, aemin, aemax, hemin, hemax
  enemy = "Slime"
  healthe = 10 
  aemin = 3  #Min enemy attack
  aemax = 7 #Max enemy attack
  hemin = 2  #Min enemy heal
  hemax = 3 #Max enemy heal
def rock():
  global enemy, healthe, aemin, aemax, hemin, hemax
  enemy = "Rock"
  healthe = 50 
  aemin = 1 #Min enemy attack
  aemax = 3 #Max enemy attack
  hemin = 1 #Min enemy heal
  hemax = 3 #Max enemy heal
def rupa():
  global enemy, healthe, aemin, aemax, hemin, hemax
  enemy = "Rupa"
  healthe = 20 
  aemin = 2 #Min enemy attack
  aemax = 5 #Max enemy attack
  hemin = 2 #Min enemy heal
  hemax = 10 #Max enemy heal
def eduardo():
  global enemy, healthe, aemin, aemax, hemin, hemax
  enemy = "Eduardo"
  healthe = 30
  aemin = 3 #Min enemy attack
  aemax = 5 #Max enemy attack
  hemin = 5 #Min enemy heal
  hemax = 10 #Max enemy heal
def theActualCannibalMrLeboeuf():
  global enemy, healthe, aemin, aemax, hemin, hemax
  enemy = "The Actual Cannibal Mr.Leboeuf"
  healthe = 100
  aemin = 15 #Min enemy attack
  aemax = 25 #Max enemy attack
  hemin = 10 #Min enemy heal
  hemax = 15 #Max enemy heal
def mzPaulino():
  global enemy, healthe, aemin, aemax, hemin, hemax
  enemy = "Mz.Paulino"
  healthe = 100
  aemin = 10 #Min enemy attack
  aemax = 15 #Max enemy attack
  hemin = 20 #Min enemy heal
  hemax = 30 #Max enemy heal
def developer():
  global enemy, healthe, aemin, aemax, hemin, hemax
  enemy = "Developer"
  healthe = 5000 
  aemin = 100 #Min enemy attack
  aemax = 200 #Max enemy attack
  hemin = 100 #Min enemy heal
  hemax = 150 #Max enemy heal


#ADD LEVEL TO PLAYER LABEL
global midLabel
midLabel = Label(window, text = "One goal...\n\n                 SURVIVE\n\n\nYou're given the ability to attack and heal yourself. Encounter with enemies may happen...\n\n", font=("", 20))
midLabel.grid(row=1, column = 2)
player()
slime()
playerStat = Label(window, text = f"Player:\n\n\nHealh = {health}\n\nATK = {amin}-{amax}\n\nHeal = {hmin}-{hmax}", font = ("", 20))
playerStat.grid(row=1, column = 1, padx=(1, 200))

enemyStat = Label(window, text = f"{enemy}:\n\n\nHealh = {healthe}\n\nATK = {aemin}-{aemax}\n\nHeal = {hemin}-{hemax}", font = ("", 20))
enemyStat.grid(row=1, column = 3, padx=(200, 100))


def wanderAction():
  global midLabel, eselect
  eselect = random.choice(enemies)
  if eselect == 0:
    midLabel.configure(text = "You've got a bunus Upgrade!\n Choose what you'd like to upgrade!")
    upgradeButtonsOnly()

  elif eselect == 1:
    slime(), midLabel.config(text = f"\nYou've encounted {enemy}!"), battle()
  elif eselect == 2:
    rock(), midLabel.config(text = f"\nYou've encounted {enemy}!"), battle()
  elif eselect == 3:
    rupa(), midLabel.config(text = f"\nYou've encounted {enemy}!"), battle()
  elif eselect == 4:
    eduardo(), midLabel.config(text = f"\nYou've encounted {enemy}!"), battle()
  elif eselect == 5:
    mzPaulino(), midLabel.config(text = f"\nYou've encounted {enemy}!"), battle()
  elif eselect == 6:
    theActualCannibalMrLeboeuf(), midLabel.config(text = (f"\nYou've encounted {enemy}(Good luck 💀)\n\n")), battle()
  elif eselect == 7:
    developer(), midLabel.config(text = (f"\nYou've encounted The {enemy}!")), battle()
  else:
    midLabel.config(text = "You broke the game!")
buttonWander = Button(window, text = "Wander Around", command = wanderAction).grid(row=4)





def attackAction():
  global choice
  choice = "a"
buttonAttack = Button(window, text = "Attack", command = attackAction).grid(row = 3, column = 2)

def healAction():
  global choice
  choice = "h"
buttonHeal = Button(window, text = "Heal", command = healAction).grid(row = 3, column = 3)

def upgMinA():
  global lvlup
  if lvlup == 1:
    lvlup = "1"
  else:
    amin += 1
    wanderonly()
buttonUpgMinA = Button(window, text = "Upg Min ATK", command = upgMinA).grid(row=2, column = 1)

def upgMaxA():
  global lvlup
  if lvlup == 1:
    lvlup = "2"
  else:
    amax += 1
    wanderonly()
buttonUpgMaxA = Button(window, text = "Upg Max ATK", command = upgMaxA).grid(row=2, column = 2)

def upgMinH():
  global lvlup
  if lvlup == 1:
    lvlup = "3"
  else:
    hmin += 1
    wanderonly()
buttonUpgMinH = Button(window, text = "Upg Min Heal", command = upgMinH).grid(row=2, column = 3)

def upgMaxH():
  global lvlup
  if lvlup == 1:
    lvlup = "4"
  else:
    hmax += 1
    wanderonly()
buttonUpgMaxH = Button(window, text = "Upg Max Heal", command = upgMaxH).grid(row=2, column = 4)









def eturn():
  buttonWander.config(state = DISABLED)
  buttonAttack.config(state = DISABLED)
  buttonHeal.config(state = DISABLED)
  buttonUpgMinA.config(state = DISABLED)
  buttonUpgMaxA.config(state = DISABLED)
  buttonUpgMinH.config(state = DISABLED)
  buttonUpgMaxH.config(state = DISABLED)
def wanderonly():
  buttonWander.config(state = ACTIVE)
  buttonAttack.config(state = DISABLED)
  buttonHeal.config(state = DISABLED)
  buttonUpgMinA.config(state = DISABLED)
  buttonUpgMaxA.config(state = DISABLED)
  buttonUpgMinH.config(state = DISABLED)
  buttonUpgMaxH.config(state = DISABLED)
def pturnButtonsOnly():
  buttonWander.config(state = DISABLED)
  buttonAttack.config(state = ACTIVE)
  buttonHeal.config(state = ACTIVE)
  buttonUpgMinA.config(state = DISABLED)
  buttonUpgMaxA.config(state = DISABLED)
  buttonUpgMinH.config(state = DISABLED)
  buttonUpgMaxH.config(state = DISABLED)
def upgradeButtonsOnly():
  buttonWander.config(state = DISABLED)
  buttonAttack.config(state = DISABLED)
  buttonHeal.config(state = DISABLED)
  buttonUpgMinA.config(state = ACTIVE)
  buttonUpgMaxA.config(state = ACTIVE)
  buttonUpgMinH.config(state = ACTIVE)
  buttonUpgMaxH.config(state = ACTIVE)
def labelUpdate():
  global enemyStat, playerStat

  enemyStat.grid(row=1, column = 1, padx=(1, 200))
  playerStat.grid(row=1, column = 3, padx=(200, 100))



def addEnemy():

  global enemies
  if upgs == 50:
    enemies = [0, 1, 2, 3, 4, 5, 6, 7]
  elif upgs == 10:
    enemies = [0, 1, 2, 3, 4, 5, 6]
window.mainloop()