#import dependencies
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

#dice function that will randomly roll an n-sided dice with n=6 as the default number of sides
def dice(n=6):
  #return number between 1 and n
  return(np.random.randint(1,n+1))
