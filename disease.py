import numpy as np

prob_exposure = 0.1 #10% chance of exposure
prob_tired = 0.4 #40% chance of tiredness for any given patient

#probability of virus given exposure/tiredness state
def prob_virus(e,t):
  probabilities = {(0,0):0.01, #1% chance of virus if NOT exposed to infected person and NOT tired
                   (1,0):0.4, #40% chance of virus if exposed to infected person but NOT tired
                   (0,1):0.1 #10% chance of virus if NOT exposed to infected person but tired
                   ,(1,1):0.7} #70% chance of virus if exposed to infected person and tired
  return(probabilities[(e,t)])

def prob_fever(virus): #0-no virus, 1-virus present
  prob = {0:0.05, #5% chance of fever if no virus
          1:0.5} #50% chance of fever if virus is prevalent
  return(prob[virus])

def prob_cough(virus): #0-no virus, 1-virus present
  prob = {0:0.15, #15% chance of coughing if virus is not present
          1:0.8} #80% chance of coughing if virus is present
  return(prob[virus])
  
#simulates medical cases for a large number of patients

def simulate_disease(n_patients):

  #we seek to find P(virus | cough), the probability of having a virus given that the patient has a cough
  #P(virus | fever), which is defined analagously, and P(virus), which is the general probability of having the virus.
  
  cough_cases = 0 
  fever_cases = 0
  virus_cough_cases = 0 #number of cough cases with a virus
  virus_fever_cases = 0 #number of fever cases with a virus
  virus_cases=0 #total number of virus cases

  for trial in range(n_patients):
    #randomly simulating all patient information, including exposure (e), tiredness (t), virus, fever, and cough.
    #these information are stored in binary with 1 (has condition) and 0 (does not have specified condition)

     e = np.random.choice([1,0],p=[prob_exposure,1-prob_exposure])
     t = np.random.choice([1,0],p=[prob_tired,1-prob_tired])

     p_virus = prob_virus(e,t)
     virus = np.random.choice([1,0],p=[p_virus,1-p_virus])
  
     fever = np.random.choice([1,0],p=[prob_fever(virus),1-prob_fever(virus)])
     cough = np.random.choice([1,0],p=[prob_cough(virus),1-prob_cough(virus)])

    #checking if a patient has a cough and then checking if they also have the virus
     if (cough==1):
       cough_cases+=1
       if (virus==1):
         virus_cough_cases+=1
    
    #checking if a patient has a fever and then checking if they also have the virus
     if (fever==1):
       fever_cases+=1
       if (virus==1):
         virus_fever_cases+=1

    #checking if the patient has the virus
     if (virus==1):
        virus_cases+=1
    
  return(virus_cough_cases/cough_cases,virus_fever_cases/fever_cases,virus_cases/n_patients)
    
    #1st variable is the proportion of cough cases with a virus infection
    #2nd variable is the proportion of fever cases with a virus infection
    #3rd variable is the overall proportion of virus cases

simulate_disease(n_patients=10000)
