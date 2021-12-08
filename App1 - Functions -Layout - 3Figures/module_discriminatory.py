 # -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 18:44:10 2021

@author: s14761
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

##Discriminatory price auction

def CDF_tt(al, ah, kl, kh, T, t, P, N): 
    #Call function determin_are to know in which area falls the realization of the demand
    area, area_num = determine_area(al, ah)
    
    p = np.zeros(N+1)
    Fh = np.zeros(N+1)
    Fl = np.zeros(N+1)
    
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
        #Lower bound
        b1 = ((P*(ah-T))+(t*q11t))/q11s
        b2 = (t*q22t)/q22s
        b = max(b1,b2)
        eps = (P-b)/N  
        #CDF
        for i in range(N+1):
            p[i]=b+eps*(i)
            if i == 0:
                Fl[i]=0
                Fh[i]=0
            else:
                Fl[i]=((p[i]-b)*q11s)/((p[i]*q11s)-(t*q11t)-(b*q21s)+(t*q21t)-(P*q21r))
                Fh[i]=((p[i]-b)*q22s)/((p[i]*q22s)-(t*q22t)-(b*q12s)+(t*q12t))
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
        #CDF
        for i in range(N+1):
            p[i]=b+eps*(i)
            Fh[i]=((p[i]-b)*q22s)/((p[i]*q22s)-(t*q22t)-(p[i]*q12s)+(t*q12t))
            Fl[i]=((p[i]-b)*q11s)/((p[i]*q11s)-(t*q11t)-(p[i]*q21s)+(t*q21t)-(P*q21r))
    Fh[N] = 1
    Fl[N] =1    
    return Fh, Fl, p


def CDF_pc(al, ah, kl, kh, T, t, P, N): 
    #Call function determin_are to know in which area falls the realization of the demand
    area, area_num = determine_area(al, ah)
    
    p = np.zeros(N+1)
    Fh = np.zeros(N+1)
    Fl = np.zeros(N+1)
    
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
        #Lower bound
        b1 = t+((P-t)*(ah-T)/q11s)
        b2 = (t*(al+T))/q22s
        b = max(b1,b2)
        eps = (P-b)/N  
        #CDF
        for i in range(N+1):
            p[i]=b+eps*(i)
            if i == 0:
                Fl[i]=0
                Fh[i]=0
            else:
                Fl[i]=((p[i]-b)*q11s)/(((p[i]-t)*q11s)-((p[i]-t)*q21s)-((P-t)*q21r))
                Fh[i]=((p[i]-b)*q22s)/(((p[i]-t)*q22s)-((p[i]-t)*q12s))
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
        #CDF
        for i in range(N+1):
            p[i]=b+eps*(i)
            Fh[i]=((p[i]-b)*q22s)/(((p[i]-t)*q22s)-((p[i]-t)*q12s))
            Fl[i]=((p[i]-b)*q11s)/(((p[i]-t)*q11s)-((p[i]-t)*q21s)-((P-t)*q21r))
    Fh[N] = 1
    Fl[N] =1    
    return Fh, Fl, p


def welfare_tt(Fh, Fl, p, al, ah, T, t, kl, kh, P):
    area, area_num = determine_area(al, ah)
    Fh_diff = np.diff(Fh)
    Fl_diff = np.diff(Fl)
    
    Eh = sum (p[1:]*Fh_diff)
    El = sum (p[1:]*Fl_diff)
    
    E = (El*al/(al+ah))+(Eh*ah/(al+ah))
    CS_capita = P-E
    CS_aggregate = CS_capita*(al+ah)
    
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
        #Lower bound
        b1 = ((P*(ah-T))+(t*q11t))/q11s
        b2 = ((P*q12s)+(t*q22t)-(t*q12t))/q22s
        b = max(b1,b2)
        pil = (b*q22s)-(t*q22t)
        pih = (b*q11s)-(t*q11t)
        pi_aggregate = pil+pih
        CS_capita_adjusted = CS_capita-(b*q22r/(al+ah))
        CS_aggregate_adjusted = CS_capita_adjusted*(al+ah)
    welfare_aggregate = CS_aggregate + pi_aggregate
    welfare_aggregate_adjusted = CS_aggregate_adjusted + pi_aggregate
    return Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted

def welfare_pc(Fh, Fl, p, al, ah, T, t, kl, kh, P):
    area, area_num = determine_area(al, ah)
    Fh_diff = np.diff(Fh)
    Fl_diff = np.diff(Fl)
    
    Eh = sum (p[1:]*Fh_diff)
    El = sum (p[1:]*Fl_diff)
    
    E = (El*al/(al+ah))+(Eh*ah/(al+ah))
    CS_capita = P-E
    CS_aggregate = CS_capita*(al+ah)
    
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
        #Lower bound
        b1 = t+((P-t)*(ah-T)/q11s)
        b2 = (((P-t)*q12s)+(t*(al+T)))/q22s
        b = max(b1,b2)
        pil = (b-t)*q22s
        pih = (b-t)*q11s
        pi_aggregate = pil+pih
        CS_capita_adjusted = CS_capita-(b*q22r/(al+ah))
        CS_aggregate_adjusted = CS_capita_adjusted*(al+ah)
    welfare_aggregate = CS_aggregate + pi_aggregate
    welfare_aggregate_adjusted = CS_aggregate_adjusted + pi_aggregate
    return Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted

def plot_welfare_tt(al, kl, kh, T, t, P, N, N2):
    ah_lst = np.linspace(41, 99, N2)
    
    Eh_lst = []
    El_lst = []
    E_lst = []
    CS_capita_lst = []
    CS_capita_adjusted_lst = []
    CS_aggregate_lst = []
    CS_aggregate_adjusted_lst = []
    pil_lst = []
    pih_lst = []
    pi_aggregate_lst = []
    welfare_aggregate_lst = []
    welfare_aggregate_adjusted_lst = []
    
    for ah in ah_lst:
        Fh, Fl, p = CDF_tt(al, ah, kl, kh, T, t, P, N)
        Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted = welfare_tt(Fh, Fl, p, al, ah, T, t, kl, kh, P)
        Eh_lst.append(Eh)
        El_lst.append(El)
        E_lst.append(E)
        CS_capita_lst.append(CS_capita)
        CS_capita_adjusted_lst.append(CS_capita_adjusted)
        CS_aggregate_lst.append(CS_aggregate)
        CS_aggregate_adjusted_lst.append(CS_aggregate_adjusted)
        pil_lst.append(pil)
        pih_lst.append(pih)
        pi_aggregate_lst.append(pi_aggregate)
        welfare_aggregate_lst.append(welfare_aggregate)
        welfare_aggregate_adjusted_lst.append(welfare_aggregate_adjusted)
        
    return ah_lst, Eh_lst, El_lst, E_lst, CS_capita_lst, CS_capita_adjusted_lst, CS_aggregate_lst, CS_aggregate_adjusted_lst, pil_lst, pih_lst, pi_aggregate_lst, welfare_aggregate_lst, welfare_aggregate_adjusted_lst

def plot_welfare_pc(al, kl, kh, T, t, P, N, N2):
    ah_lst = np.linspace(41, 99, N2)
    
    Eh_lst = []
    El_lst = []
    E_lst = []
    CS_capita_lst = []
    CS_capita_adjusted_lst = []
    CS_aggregate_lst = []
    CS_aggregate_adjusted_lst = []
    pil_lst = []
    pih_lst = []
    pi_aggregate_lst = []
    welfare_aggregate_lst = []
    welfare_aggregate_adjusted_lst = []

    
    for ah in ah_lst:
        Fh, Fl, p = CDF_pc(al, ah, kl, kh, T, t, P, N)
        Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted = welfare_pc(Fh, Fl, p, al, ah, T, t, kl, kh, P)
        Eh_lst.append(Eh)
        El_lst.append(El)
        E_lst.append(E)
        CS_capita_lst.append(CS_capita)
        CS_capita_adjusted_lst.append(CS_capita_adjusted)
        CS_aggregate_lst.append(CS_aggregate)
        CS_aggregate_adjusted_lst.append(CS_aggregate_adjusted)
        pil_lst.append(pil)
        pih_lst.append(pih)
        pi_aggregate_lst.append(pi_aggregate)
        welfare_aggregate_lst.append(welfare_aggregate)
        welfare_aggregate_adjusted_lst.append(welfare_aggregate_adjusted)
        
    return ah_lst, Eh_lst, El_lst, E_lst, CS_capita_lst, CS_capita_adjusted_lst, CS_aggregate_lst, CS_aggregate_adjusted_lst, pil_lst, pih_lst, pi_aggregate_lst, welfare_aggregate_lst, welfare_aggregate_adjusted_lst

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


if __name__=='__main__': 
    
    #Colors
    '''
    colors = {
        "charcoal": "#264653ff",
        "persian-green": "#2a9d8fff",
        "orange-yellow-crayola": "#e9c46aff",
        "sandy-brown": "#f4a261ff",
        "burnt-sienna": "#e76f51ff"}
    '''
    colors = {
        "c": "#264653ff",
        "p-g": "#2a9d8fff",
        "o-y-c": "#e9c46aff",
        "s-b": "#f4a261ff",
        "b-s": "#e76f51ff"}
    
  
    
    import matplotlib.pyplot as plt 
    al = 15
    ah = 50.5
    kl = 60
    kh = 60
    T = 40
    t = 1.25
    P = 7
    N = 100
    N2 = 400
    tmax = determine_tmax(al, ah, T, P)
    
    #Determine the area
    area, area_num = determine_area(al, ah)
    
    #CDF_tt
    Fh_tt, Fl_tt, p_tt = CDF_tt(al, ah, kl, kh, T, t, P, N)   
    Eh_tt, El_tt, E_tt, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted=welfare_tt(Fh_tt, Fl_tt, p_tt, al, ah, T, t, kl, kh, P)
    fig, ax = plt.subplots()
    ax.plot(p_tt, Fh_tt, label = 'Fh_tt',  color = colors["c"])
    ax.plot(p_tt, Fl_tt, label = 'Fl_tt', color = colors["p-g"])
    ax.plot([Eh_tt,Eh_tt], [0,1], label = 'Eh_tt',  color = colors["c"])
    ax.plot([El_tt,El_tt], [0,1], label = 'El_tt', color = colors["p-g"])
    ax.plot([E_tt,E_tt], [0,1], label = 'E_tt', color = colors["o-y-c"])
    
    #CDF_pc
    Fh_pc, Fl_pc, p_pc = CDF_pc(al, ah, kl, kh, T, t, P, N)   
    Eh_pc, El_pc, E_pc, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted=welfare_pc(Fh_pc, Fl_pc, p_pc, al, ah, T, t, kl, kh, P)
    fig, ax = plt.subplots()
    ax.plot(p_pc, Fh_pc, label = 'Fh_pc',  color = colors["c"], alpha=1)
    ax.plot(p_pc, Fl_pc, label = 'Fl_pc', color = colors["p-g"], alpha=1)
    ax.plot([Eh_pc,Eh_pc], [0,1], label = 'Eh_pc',  color = colors["c"], alpha=1)
    ax.plot([El_pc,El_pc], [0,1], label = 'El_pc', color = colors["p-g"], alpha=1)
    ax.plot([E_pc,E_pc], [0,1], label = 'E_pc', color = colors["o-y-c"], alpha=1)
    
    #CDF comparison
    fig, ax = plt.subplots()
    ax.plot(p_tt, Fh_tt, label = 'Fh_tt',  color = colors["c"])
    ax.plot(p_tt, Fl_tt, label = 'Fl_tt', color = colors["p-g"])
    ax.plot([Eh_tt,Eh_tt], [0,1], label = 'Eh_tt',  color = colors["c"])
    ax.plot([El_tt,El_tt], [0,1], label = 'El_tt', color = colors["p-g"])
    ax.plot([E_tt,E_tt], [0,1], label = 'E_tt', color = colors["o-y-c"])
    ax.plot(p_pc, Fh_pc, label = 'Fh_pc',  color = colors["c"], alpha=0.2)
    ax.plot(p_pc, Fl_pc, label = 'Fl_pc', color = colors["p-g"], alpha=0.2)
    ax.plot([Eh_pc,Eh_pc], [0,1], label = 'Eh_pc',  color = colors["c"], alpha=0.2)
    ax.plot([El_pc,El_pc], [0,1], label = 'El_pc', color = colors["p-g"], alpha=0.2)
    ax.plot([E_pc,E_pc], [0,1], label = 'E_pc', color = colors["o-y-c"], alpha=0.2)
    
    #Welfare tt
    ah_lst_tt, Eh_lst_tt, El_lst_tt, E_lst_tt, CS_capita_lst_tt, CS_capita_adjusted_lst_tt, CS_aggregate_lst_tt, CS_aggregate_adjusted_lst_tt, pil_lst_tt, pih_lst_tt, pi_aggregate_lst_tt, welfare_aggregate_lst_tt, welfare_aggregate_adjusted_lst_tt=plot_welfare_tt(al, kl, kh, T, t, P, N, N2)
    fig, ax = plt.subplots()
    ax.plot(ah_lst_tt, Eh_lst_tt, label = 'Eh_lst_tt', color = colors["c"], alpha=1)
    ax.plot(ah_lst_tt, El_lst_tt, label = 'El_lst_tt', color = colors["p-g"], alpha=1)
    ax.plot(ah_lst_tt, E_lst_tt, label = 'E_lst_tt', color = colors["o-y-c"], alpha=1)
    fig, ax = plt.subplots()
    ax.plot(ah_lst_tt, CS_aggregate_adjusted_lst_tt, label = 'CS_aggregate_adjusted_lst_tt', color = colors["b-s"], alpha=1)
    ax.plot(ah_lst_tt, CS_aggregate_lst_tt, label = 'CS_aggregate_lst_tt', color = colors["c"], alpha=1)
    fig, ax = plt.subplots()
    ax.plot(ah_lst_tt, pil_lst_tt, label = 'pil_lst_tt', color = colors["c"], alpha=1)
    ax.plot(ah_lst_tt, pih_lst_tt, label = 'pih_lst_tt', color = colors["p-g"], alpha=1)
    fig, ax = plt.subplots()
    ax.plot(ah_lst_tt, welfare_aggregate_adjusted_lst_tt, label = 'CS_aggregate_adjusted_lst_tt', color = colors["b-s"], alpha=1)
    ax.plot(ah_lst_tt, welfare_aggregate_lst_tt, label = 'CS_aggregate_lst_tt', color = colors["c"], alpha=1)
    
    
    #Welfare pc
    ah_lst_pc, Eh_lst_pc, El_lst_pc, E_lst_pc, CS_capita_lst_pc, CS_capita_adjusted_lst_pc, CS_aggregate_lst_pc, CS_aggregate_adjusted_lst_pc, pil_lst_pc, pih_lst_pc, pi_aggregate_lst_pc, welfare_aggregate_lst_pc, welfare_aggregate_adjusted_lst_pc=plot_welfare_pc(al, kl, kh, T, t, P, N, N2)
    fig, ax = plt.subplots()
    ax.plot(ah_lst_pc, Eh_lst_pc, label = 'Eh_lst_pc', color = colors["c"], alpha=0.2)
    ax.plot(ah_lst_pc, El_lst_pc, label = 'El_lst_pc', color = colors["p-g"], alpha=0.2)
    ax.plot(ah_lst_pc, E_lst_pc, label = 'E_lst_pc', color = colors["o-y-c"], alpha=0.2)
    fig, ax = plt.subplots()
    ax.plot(ah_lst_pc, CS_aggregate_adjusted_lst_pc, label = 'CS_aggregate_adjusted_lst_pc', color = colors["b-s"], alpha=0.2)
    ax.plot(ah_lst_pc, CS_aggregate_lst_pc, label = 'CS_aggregate_lst_pc', color = colors["c"], alpha=0.2)
    fig, ax = plt.subplots()
    ax.plot(ah_lst_pc, pil_lst_pc, label = 'pil_lst_pc', color = colors["c"], alpha=0.2)
    ax.plot(ah_lst_pc, pih_lst_pc, label = 'pih_lst_pc', color = colors["p-g"], alpha=0.2)
    fig, ax = plt.subplots()
    ax.plot(ah_lst_pc, welfare_aggregate_adjusted_lst_pc, label = 'CS_aggregate_adjusted_lst_pc', color = colors["b-s"], alpha=0.2)
    ax.plot(ah_lst_pc, welfare_aggregate_lst_pc, label = 'CS_aggregate_lst_pc', color = colors["c"], alpha=0.2)
    
    #Compare welfare
    ah_lst_tt, Eh_lst_tt, El_lst_tt, E_lst_tt, CS_capita_lst_tt, CS_capita_adjusted_lst_tt, CS_aggregate_lst_tt, CS_aggregate_adjusted_lst_tt, pil_lst_tt, pih_lst_tt, pi_aggregate_lst_tt, welfare_aggregate_lst_tt, welfare_aggregate_adjusted_lst_tt=plot_welfare_tt(al, kl, kh, T, t, P, N, N2)
    ah_lst_pc, Eh_lst_pc, El_lst_pc, E_lst_pc, CS_capita_lst_pc, CS_capita_adjusted_lst_pc, CS_aggregate_lst_pc, CS_aggregate_adjusted_lst_pc, pil_lst_pc, pih_lst_pc, pi_aggregate_lst_pc, welfare_aggregate_lst_pc, welfare_aggregate_adjusted_lst_pc=plot_welfare_pc(al, kl, kh, T, t, P, N, N2)
    fig, ax = plt.subplots()
    ax.plot(ah_lst_tt, Eh_lst_tt, label = 'Eh_lst_tt', color = colors["c"], alpha=1)
    ax.plot(ah_lst_tt, El_lst_tt, label = 'El_lst_tt', color = colors["p-g"], alpha=1)
    ax.plot(ah_lst_tt, E_lst_tt, label = 'E_lst_tt', color = colors["o-y-c"], alpha=1) 
    ax.plot(ah_lst_pc, Eh_lst_pc, label = 'Eh_lst_pc', color = colors["c"], alpha=0.2)
    ax.plot(ah_lst_pc, El_lst_pc, label = 'El_lst_pc', color = colors["p-g"], alpha=0.2)
    ax.plot(ah_lst_pc, E_lst_pc, label = 'E_lst_pc', color = colors["o-y-c"], alpha=0.2)
    fig, ax = plt.subplots()
    ax.plot(ah_lst_tt, CS_aggregate_adjusted_lst_tt, label = 'CS_aggregate_adjusted_lst_tt', color = colors["b-s"], alpha=1)
    ax.plot(ah_lst_tt, CS_aggregate_lst_tt, label = 'CS_aggregate_lst_tt', color = colors["c"], alpha=1)
    ax.plot(ah_lst_pc, CS_aggregate_adjusted_lst_pc, label = 'CS_aggregate_adjusted_lst_pc', color = colors["b-s"], alpha=0.2)
    ax.plot(ah_lst_pc, CS_aggregate_lst_pc, label = 'CS_aggregate_lst_pc', color = colors["c"], alpha=0.2)
    fig, ax = plt.subplots()
    ax.plot(ah_lst_tt, pil_lst_tt, label = 'pil_lst_tt', color = colors["c"], alpha=1)
    ax.plot(ah_lst_tt, pih_lst_tt, label = 'pih_lst_tt', color = colors["p-g"], alpha=1)
    ax.plot(ah_lst_pc, pil_lst_pc, label = 'pil_lst_pc', color = colors["c"], alpha=0.2)
    ax.plot(ah_lst_pc, pih_lst_pc, label = 'pih_lst_pc', color = colors["p-g"], alpha=0.2)
    fig, ax = plt.subplots()
    ax.plot(ah_lst_tt, welfare_aggregate_adjusted_lst_tt, label = 'CS_aggregate_adjusted_lst_tt', color = colors["b-s"], alpha=1)
    ax.plot(ah_lst_tt, welfare_aggregate_lst_tt, label = 'CS_aggregate_lst_tt', color = colors["c"], alpha=1)
    ax.plot(ah_lst_pc, welfare_aggregate_adjusted_lst_pc, label = 'CS_aggregate_adjusted_lst_pc', color = colors["b-s"], alpha=0.2)
    ax.plot(ah_lst_pc, welfare_aggregate_lst_pc, label = 'CS_aggregate_lst_pc', color = colors["c"], alpha=0.2)
    