from tkinter import *
import random

window = Tk()
midLabel = Label(window, text = "One goal...\n\n                 SURVIVE\n\n\nYou're given the ability to attack and heal yourself. Encounter with enemies may happen...\n\n", font=("", 20))
midLabel.grid(row=1, column = 2)

turn = 0

#HOW BATTLING WORKS
def battle():
  global healthe, health, turn, echose, attacke, heal
  while healthe > 0 and health > 0:
    turn += 1
    #ENEMY TURN ON ODD TURNS
    if turn % 2 == 0:
      echose = ["0", "1"]
      turne = random.choice(echose)

      #IF 1 IS RANDOMLY SELECTED, THEY WILL ATTACK
      if turne == "1":
        eAttack()
        labelUpdate()
        print("ENEMY ATTACKED")
      #IF 1 IS NOT RANDOMLY SELECTED, THEY WILL HEAL
      else:
        eHeal()
        labelUpdate()
        print("ENEMY HEALED")

    #IT IS PLAYER TURN IF TURN IS NOT ODD
    else:#ONLY ENABLE ATTACK OR HEAL WHEN ITS YOUR TURN
      midLabel.config(text=(f"Your turn"))
      playerTurn()
  
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

player()
slime()
playerStat = Label(window, text = f"Player:\n\n\nHealh = {health}\n\nATK = {amin}-{amax}\n\nHeal = {hmin}-{hmax}", font = ("", 20))
playerStat.grid(row=1, column = 1, padx=(1, 200))

enemyStat = Label(window, text = f"{enemy}:\n\n\nHealh = {healthe}\n\nATK = {aemin}-{aemax}\n\nHeal = {hemin}-{hemax}", font = ("", 20))
enemyStat.grid(row=1, column = 3, padx=(200, 100))



def wanderAction():
  global midLabel, eselect, enemies
  enemies = [0, 1]
  eselect = random.choice(enemies)
  if eselect == 0:
    midLabel.configure(text = "You")

  elif eselect == 1:
    slime(), midLabel.config(text = f"\nYou've encounted {enemy}!"), battle()

  else:
    midLabel.config(text = "You broke the game!")
buttonWander = Button(window, text = "Wander Around", command = wanderAction).grid(row=4)



def attackAction():
  global healthe, midLabel
  attack = random.randint(amin, amax)
  healthe -= attack
  midLabel.config(text = (f"\nYou attacked {enemy}... -{attack}Hp"))
  labelUpdate()
  eturn()
buttonAttack = Button(window, text = "Attack", command = attackAction).grid(row = 3, column = 2)



def healAction():
  global health, heal
  heal = random.randint(hmin, hmax)
  health += random.randint(hmin, hmax)
  midLabel.config(text = (f"\nYou healed +{health}Hp"))
  labelUpdate()
  eturn()

def eHeal():
  global healthe, heal
  heal = random.randint(hemin, hemax)
  healthe += random.randint(hmin, hmax)
  midLabel.config(text = (f"\nEnemy healed +{health}Hp"))
  labelUpdate()


def eAttack():
  global attacke, health
  attacke = random.randint(aemin, aemax)
  health -= attacke
  midLabel.config(text = (f"\nEnemy attacked you... -{attacke}Hp"))
  labelUpdate()
  eturn()
  
buttonHeal = Button(window, text = "Heal", command = healAction).grid(row = 3, column = 3)



def upgMinA():
  global amin
  amin += 3
  labelUpdate()
  eturn()
buttonUpgMinA = Button(window, text = "Upg Min ATK", command = upgMinA).grid(row=2, column = 1)



def upgMaxA():
  global amax
  amax += 3
  labelUpdate()
  eturn()
buttonUpgMaxA = Button(window, text = "Upg Max ATK", command = upgMaxA)
buttonUpgMaxA.grid(row=2, column = 2)



def upgMinH():
  global hmin
  hmin += 3
  labelUpdate()
  eturn()
buttonUpgMinH = Button(window, text = "Upg Min Heal", command = upgMinH)
buttonUpgMinH.grid(row=2, column = 3)



def upgMaxH():
  global hmax
  hmax += 3
  labelUpdate()
  eturn()
buttonUpgMaxH = Button(window, text = "Upg Max Heal", command = upgMaxH)
buttonUpgMaxH.grid(row=2, column = 4)









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
def playerTurn():
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

  playerStat.grid(row=1, column = 1, padx=(1, 200))
  enemyStat.grid(row=1, column = 3, padx=(200, 100))

window.mainloop()