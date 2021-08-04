#import dependencies
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

#dice function that will randomly roll an n-sided dice with n=6 as the default number of sides
def dice(n=6):
  #return number between 1 and n
  return(np.random.randint(1,n+1))

#simulates a random walk k times around the 40-square monopoly board
#each square is labeled from 0 (start/GO) to 39

def board_walk(k):
  #starting location
  start = 0
  #list of visited locations
  walk = []

  while (start<40*k): #the loop will end once we walk around the board k times
  
    walk.append(start%40) #add location to the walk

    movement = dice()+dice() #movement is the sum of two random dice
    start+=movement
  
  return(walk) #return the list of visited locations

#simulates multiple trials in which each trial consists of walking around the board a certain
#number of times, as defined by the parameter n_walks.

def board_multiple(n_trials,n_walks):
  #keeps track of all squares visited
  squares_list = []

  for trial in range(n_trials):
    #runs a random walk
    walk = board_walk(n_walks)

    for square in walk:
      #adds all of the locations to our comprehensive list of locations
      squares_list.append(square)
  
  return(squares_list)

"""
Next, we will construct a **histogram** of all of the visited locations (squares 0 through 39) and their corresponding frequencies)
"""
locations = board_multiple(10000,5)

fig = plt.figure(figsize=(15,5))

plt.hist(locations,bins=[0.5+i for i in range(-1,40)],density=True)
