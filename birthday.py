#import dependencies
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

#label days of the year from 1 to 366
days = [day for day in range(1,366+1)]
print(days)

#the function generates a sample room with n people
#outputs: 1 if two people have a mutual birthday and 0 otherwise

def sample_birthday(n_people):

  #dictionary to store the # of people with each birthday
  counts = {day:0 for day in days}

  for person in range(n_people):
    #randomly select a birthday
    birthdate = np.random.choice(days)
    counts[birthdate]+=1 #add it to the counts
  
  if (max(counts.values())>1):
    return(1) #common birthday
  
  else:
    return(0) #no shared birthday

def simulate_birthday(n_people,n_trials):

  num_shared = 0 #counts the number of rooms with shared birthdays
  for trial in range(n_trials):
    if (sample_birthday(n_people)==1):
      num_shared+=1 #shared birthday
  
  return(num_shared/n_trials)
  #approximate probability of having mutual birthday

simulate_birthday(23,10000)
#We see that there is an approximately 50% chance when 23 people are in the room.
