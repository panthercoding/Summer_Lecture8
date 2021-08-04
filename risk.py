import numpy as np

class Risk():

  #a risk data object consists of the number of attack and defending dice
  def __init__(self,attack_dice,def_dice):
    self.attack_dice = attack_dice
    self.def_dice = def_dice
  
  def roll(self):
    #obtain lists of each player's dice rolls
    attack_rolls = np.random.randint(1,6+1,size=self.attack_dice)
    def_rolls = np.random.randint(1,6+1,size=self.def_dice)

    #sort the lists in decreasing order
    attack_rolls = sorted(attack_rolls,reverse=True)
    def_rolls = sorted(def_rolls,reverse=True)

    return(attack_rolls,def_rolls)
  
  def casualties(self):
    #obtain the dice rolls for each player
    attack_rolls,def_rolls = self.roll()

    attack_casualties = 0; def_casualties = 0

    #comparing the corresponding pairs of rolls, which describes the number of battles that take place
    comparisons = min(self.attack_dice,self.def_dice)

    #we directly compare the jth highest defense roll with the jth highest attack roll 
    for j in range(comparisons):
      if (def_rolls[j]>=attack_rolls[j]):
        attack_casualties += 1 #attack loss
      else: #ATTACK ROLL > DEFENSE ROLL
        def_casualties += 1 #defensive loss
    
    #return the number of attack and defense casualties in that order
    return(attack_casualties,def_casualties)
  
def simulate_risk(n_trials,attack_dice,def_dice):

  #dictionary storing the number of casualties on both teams
  casualties = {"Attack":0,"Defense":0}

  for trial in range(n_trials):
    #obtaining the number of attack and defense casualties from a single battle
    att_deaths, def_deaths = Risk(attack_dice,def_dice).casualties()
    
    #updating the dictionaries with the new casualties
    casualties["Attack"]+=att_deaths
    casualties["Defense"]+=def_deaths

  return(casualties)

war = simulate_risk(10000,3,2) #100000 simulations with 3 attack dice and 2 defensive die

attack_losses = 100*war["Attack"]/(war["Attack"]+war["Defense"])
defense_losses = 100*war["Defense"]/(war["Attack"]+war["Defense"])

print("Attack Troop Losses: {}%".format(attack_losses))
print("Defense Troop Losses: {}%".format(defense_losses))

def simulate_war(att_troops,def_troops):
  #the two sides keep battling until one side has lost all troops
  while (att_troops>0 and def_troops>0):

    #determine the appropriate number of attack and defense dice
    num_attack_dice = min(3,att_troops)
    num_def_dice = min(2,def_troops)

    #simulate one battle
    war = simulate_risk(1,num_attack_dice,num_def_dice)

    #updating the number of attack and defense troops based on casualties
    att_troops-=war["Attack"] #attack casualties
    def_troops-=war["Defense"] #defense casualties
  
  if (att_troops>def_troops):
    return(1) #attack victory
  else:
    return(0) #defense victory

simulate_war(5,4)

def probability_attack_win(att_troops,def_troops,n_trials):
  att_wins = 0 #count attack wins

  for trial in range(n_trials):
    if (simulate_war(att_troops,def_troops)==1):
      att_wins+=1 #attack win has transpired
    
  #return proportion or estimated probability of attack wins
  return(att_wins/n_trials)

#10000 simulations with 10 attack troops and 8 defense troops
probability_attack_win(10,8,10000)
