# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 10:37:54 2021

@author: Godfather
"""
import numpy as np

#Fin t such that the equilibrium is in mixed strategies

def determine_tmax(al, ah, T, P):
    tmax=P*(ah-T)*(al+T)/((T*ah)-(al*al))
    return tmax

def determine_area(al, ah):
    if al+ah <= 60:
        area = 'B'
        area_num = 1
    else:
        area = 'C'
        area_num = 0
    return area, area_num

#Uniform price auction
def u_tt(al, ah, kl, kh, T, t, P, N): 
    #Call function determin_are to know in which area falls the realization of the demand
    area, area_num = determine_area(al, ah)
    
    #Area B. As when the auction is discriminatory:
    if area_num == 1:
        #Spot
        q11s = al+ah
        q12s = 0
        q21s = 0
        q22s = al+ah
        #Redisptach
        q21r=(ah-T)-q21s
        q22r=q22s-(al+T) #This value never enters in the CDF, since in the redispatch market, it is multiplied by 0
        #Transmission
        q11t=al
        q12t=0
        q21t=0
        q22t=T
        #Lower bound
        b1 = ((P*(ah-T))+(t*q11t))/q11s
        b2 = (t*q22t)/q22s
        b = max(b1,b2)
        eps = (P-b)/N  
        #CDF. As when the auction is discriminatory
    else:
        #Spot
        q11s = kh
        q12s = (al+ah-kh)
        q21s = (al+ah-kl)
        q22s = kl
        #Redisptach
        q21r=(ah-T)-q21s
        q22r=q22s-(al+T) #This value never enters in the CDF, since in the redispatch market, it is multiplied by 0
        #Transmission
        q11t=max(0,kh-ah)
        q12t=max(0,ah-kh)
        q21t=max(0,al-kl) #In fact, for the parameters of the model, q21t=0
        q22t=T
        #Lower bound
        b1 = ((P*(ah-T))+(t*q11t))/q11s
        b2 = ((P*q12s)+(t*q22t)-(t*q12t))/q22s
        b = max(b1,b2)
        eps = (P-b)/N         
    return b1, b2

def u_pc(al, ah, kl, kh, T, t, P, N): 
    #Call function determin_are to know in which area falls the realization of the demand
    area, area_num = determine_area(al, ah)
        
    #Area B. As when the auction is discriminatory:
    if area_num == 1:
        #Spot
        q11s = al+ah
        q12s = 0
        q21s = 0
        q22s = al+ah
        #Redisptach
        q21r=(ah-T)-q21s
        q22r=q22s-(al+T) #This value never enters in the CDF, since in the redispatch market, it is multiplied by 0
        #Lower bound
        b1 = t+((P-t)*(ah-T)/q11s)
        b2 = (t*(al+T))/q22s
        b = max(b1,b2)
        eps = (P-b)/N  
        #CDF. As when the auction is discriminatory
    #Area C:        
    else:
        #Spot
        q11s = kh
        q12s = (al+ah-kh)
        q21s = (al+ah-kl)
        q22s = kl
        #Redisptach
        q21r=(ah-T)-q21s
        q22r=q22s-(al+T) #This value never enters in the CDF, since in the redispatch market, it is multiplied by 0
        #Lower bound
        b1 = t+((P-t)*(ah-T)/q11s)
        b2 = (((P-t)*q12s)+(t*(al+T)))/q22s
        b = max(b1,b2)
        eps = (P-b)/N   
    return b1, b2

def u_welfare_tt(Fh, Fl, p, al, ah, T, t, kl, kh, P):
    area, area_num = determine_area(al, ah)
        
    #Area B:
    if area_num == 1:
        #Spot
        q11s = al+ah
        q12s = 0
        q21s = 0
        q22s = al+ah
        #Redisptach
        q21r=(ah-T)-q21s
        q22r=q22s-(al+T) #This value never enters in the CDF, since in the redispatch market, it is multiplied by 0
        #Transmission
        q11t=al
        q12t=0
        q21t=0
        q22t=T
        #CS
        Fh_diff = np.diff(Fh)
        Fl_diff = np.diff(Fl)
        
        Eh = sum (p[1:]*Fh_diff)
        El = sum (p[1:]*Fl_diff)
        
        E = (El*al/(al+ah))+(Eh*ah/(al+ah))
        CS_capita = P-E
        CS_aggregate = CS_capita*(al+ah)
        #Lower bound
        b1 = ((P*(ah-T))+(t*q11t))/q11s
        b2 = (t*q22t)/q22s
        b = max(b1,b2)
        pil = (b*q22s)-(t*q22t)
        pih = (b*q11s)-(t*q11t)
        pi_aggregate = pil+pih
        CS_capita_adjusted = CS_capita-(b*q22r/(al+ah))
        CS_aggregate_adjusted = CS_capita_adjusted*(al+ah)
    else:
        #Spot
        q11s = kh
        q12s = (al+ah-kh)
        q21s = (al+ah-kl)
        q22s = kl
        #Redisptach
        q21r=(ah-T)-q21s
        q22r=q22s-(al+T) #This value never enters in the CDF, since in the redispatch market, it is multiplied by 0
        #Transmission
        q11t=max(0,kh-ah)
        q12t=max(0,ah-kh)
        q21t=max(0,al-kl) #In fact, for the parameters of the model, q21t=0
        q22t=T
        #CS
        E = P
        CS_capita = 0
        CS_aggregate = 0
        CS_capita_adjusted = 0
        CS_aggregate_adjusted = 0
        #Profits
        #Profits equilibrium 1        
        pil = (P*q22s)-(t*q22t)
        pih = P*(ah-T)
        pi_aggregate = pil+pih
        #Profits equilibrium 2
        '''        
        pil = (P*q12s)-(t*max(0,al-q11s))
        pih = (P*q11s)-(t*q11t)
        pi_aggregate = pil+pih
        '''
    welfare_aggregate = CS_aggregate + pi_aggregate
    welfare_aggregate_adjusted = CS_aggregate_adjusted + pi_aggregate
    return Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted

def u_welfare_pc(Fh, Fl, p, al, ah, T, t, kl, kh, P):
    area, area_num = determine_area(al, ah)
    
    #Area B:
    if area_num == 1:
        #Spot
        q11s = al+ah
        q12s = 0
        q21s = 0
        q22s = al+ah
        #Redisptach
        q21r=(ah-T)-q21s
        q22r=q22s-(al+T) #This value never enters in the CDF, since in the redispatch market, it is multiplied by 0
        #CS
        Fh_diff = np.diff(Fh)
        Fl_diff = np.diff(Fl)
        
        Eh = sum (p[1:]*Fh_diff)
        El = sum (p[1:]*Fl_diff)
        
        E = (El*al/(al+ah))+(Eh*ah/(al+ah))
        CS_capita = P-E
        CS_aggregate = CS_capita*(al+ah)
        #Lower bound
        b1 = t+((P-t)*(ah-T)/q11s)
        b2 = (t*(al+T))/q22s
        b = max(b1,b2)
        pil = (b-t)*q22s
        pih = (b-t)*q11s
        pi_aggregate = pil+pih
        CS_capita_adjusted = CS_capita-(b*q22r/(al+ah))
        CS_aggregate_adjusted = CS_capita_adjusted*(al+ah)
    else:
        #Spot
        q11s = kh
        q12s = (al+ah-kh)
        q21s = (al+ah-kl)
        q22s = kl
        #Redisptach
        q21r=(ah-T)-q21s
        q22r=q22s-(al+T) #This value never enters in the CDF, since in the redispatch market, it is multiplied by 0
        #CS
        E = P
        CS_capita = 0
        CS_aggregate = 0
        CS_capita_adjusted = 0
        CS_aggregate_adjusted = 0
        #Profits
        #Profits equilibrium 1        
        pil = (P-t)*q22s
        pih = (P-t)*(ah-T)
        pi_aggregate = pil+pih
        #Profits equilibrium 2
        '''        
        pil = (P-t)*q12s
        pih = (P-t)*q11s
        pi_aggregate = pil+pih
        '''
    welfare_aggregate = CS_aggregate + pi_aggregate
    welfare_aggregate_adjusted = CS_aggregate_adjusted + pi_aggregate
    return Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted
