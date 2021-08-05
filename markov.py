import numpy as np

#list of possible climate scenarios

climate = ["snow","sunshine","rain"]

#function to randomly simulate the weather on day X+1
#given the weather on the previous day x

def predict_next(previous):

  #if the previous day was snow 
  if (previous=="snow"):
    next = np.random.choice(climate,p=[0.3,0.4,0.3])
    #we select snow with 0.3 probability, sunshine with 0.4,
    #and rain with 0.3
    return(next)
  
  #if the previous day was sunshine
  elif (previous=="sunshine"):
    next = np.random.choice(climate,p=[0.2,0.5,0.3])
    #we select snow with 0.2 probability, sunshine with 0.5,
    #and rain with 0.3
    return(next)
  
  #if the previous day was rain
  else:
    next = np.random.choice(climate,p=[0.1,0.45,0.45])
    #we select snow with 0.1 probability, sunshine with 0.45,
    #and rain with 0.45
    return(next) 

#build a chain of weather forecasts

#we start with the weather at day_0 and n = how many days
def build_climate(day_0,n):

  #sequence starts with weather at day 0
  seq = [day_0]

  #for the next n-1 days
  for i in range(1,n):

    #predict the next day's weather based on the previous day
    next = predict_next(seq[-1])
    #add it to the sequence
    seq.append(next)

  #return the Markov chain of weather states
  return(seq)

def main():
  climate = ["snow","sunshine","rain"]
  day_0 = np.random.choice(climate)
  #randomly select day 0
  print(build_climate(day_0,10))

main()
