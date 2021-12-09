 # -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 18:44:10 2021

@author: s14761
"""


import numpy as np

#Fin t such that the equilibrium is in mixed strategies

def determine_tmax(al, ah, T, t, P):
    tmax=P*(ah-T)*(al+T)/((T*ah)-(al*al))
    bl_hat=t*T/(al+T)
    bh_hat=(P*(ah-T)+(t*al))/(al+ah)
    return tmax, bl_hat, bh_hat

def determine_area(al, ah):
    if al+ah <= 60:
        area = 'B'
        area_num = 1
    else:
        area = 'C'
        area_num = 0
    return area, area_num

def d_strategies_tt(al, ah, kl, kh, T, t, P, N): 
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
        q22r=q22s-(al+T) #This value never enters in the d_strategies, since in the redispatch market, it is multiplied by 0
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
        #d_strategies
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
        q22r=q22s-(al+T) #This value never enters in the d_strategies, since in the redispatch market, it is multiplied by 0
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
        #d_strategies
        for i in range(N+1):
            p[i]=b+eps*(i)
            Fh[i]=((p[i]-b)*q22s)/((p[i]*q22s)-(t*q22t)-(p[i]*q12s)+(t*q12t))
            Fl[i]=((p[i]-b)*q11s)/((p[i]*q11s)-(t*q11t)-(p[i]*q21s)+(t*q21t)-(P*q21r))
    Fh[N] = 1
    Fl[N] =1    
    return Fh, Fl, p, b1, b2

def u_strategies_tt(al, ah, kl, kh, T, t, P, N): 
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
        q22r=q22s-(al+T) #This value never enters in the d_strategies, since in the redispatch market, it is multiplied by 0
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
        #d_strategies
        for i in range(N+1):
            p[i]=b+eps*(i)
            if i == 0:
                Fl[i]=0
                Fh[i]=0
            else:
                Fl[i]=((p[i]-b)*q11s)/((p[i]*q11s)-(t*q11t)-(b*q21s)+(t*q21t)-(P*q21r))
                Fh[i]=((p[i]-b)*q22s)/((p[i]*q22s)-(t*q22t)-(b*q12s)+(t*q12t))
    else:
        #Spot
        q11s = kh
        q12s = (al+ah-kh)
        q21s = (al+ah-kl)
        q22s = kl
        #Redisptach
        q21r=(ah-T)-q21s
        q22r=q22s-(al+T) #This value never enters in the d_strategies, since in the redispatch market, it is multiplied by 0
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
        #d_strategies
        for i in range(N+1):
            p[i]=b+eps*(i)
            Fl[i]=0
            Fh[i]=0         
    return Fh, Fl, p, b1, b2

def d_strategies_pc(al, ah, kl, kh, T, t, P, N): 
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
        q22r=q22s-(al+T) #This value never enters in the d_strategies, since in the redispatch market, it is multiplied by 0
        #Lower bound
        b1 = t+((P-t)*(ah-T)/q11s)
        b2 = (t*(al+T))/q22s
        b = max(b1,b2)
        eps = (P-b)/N  
        #d_strategies
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
        q22r=q22s-(al+T) #This value never enters in the d_strategies, since in the redispatch market, it is multiplied by 0
        #Lower bound
        b1 = t+((P-t)*(ah-T)/q11s)
        b2 = (((P-t)*q12s)+(t*(al+T)))/q22s
        b = max(b1,b2)
        eps = (P-b)/N  
        #d_strategies
        for i in range(N+1):
            p[i]=b+eps*(i)
            Fh[i]=((p[i]-b)*q22s)/(((p[i]-t)*q22s)-((p[i]-t)*q12s))
            Fl[i]=((p[i]-b)*q11s)/(((p[i]-t)*q11s)-((p[i]-t)*q21s)-((P-t)*q21r))
    Fh[N] = 1
    Fl[N] =1    
    return Fh, Fl, p, b1, b2

def u_strategies_pc(al, ah, kl, kh, T, t, P, N): 
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
        q22r=q22s-(al+T) #This value never enters in the d_strategies, since in the redispatch market, it is multiplied by 0
        #Lower bound
        b1 = t+((P-t)*(ah-T)/q11s)
        b2 = (t*(al+T))/q22s
        b = max(b1,b2)
        eps = (P-b)/N  
        #d_strategies
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
        q22r=q22s-(al+T) #This value never enters in the d_strategies, since in the redispatch market, it is multiplied by 0
        #Lower bound
        b1 = t+((P-t)*(ah-T)/q11s)
        b2 = (((P-t)*q12s)+(t*(al+T)))/q22s
        b = max(b1,b2)
        eps = (P-b)/N   
        #d_strategies
        for i in range(N+1):
            p[i]=b+eps*(i)
            Fl[i]=0
            Fh[i]=0
    return Fh, Fl, p, b1, b2

def d_welfare_tt(Fh, Fl, p, al, ah, T, t, kl, kh, P):
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
        q22r=q22s-(al+T) #This value never enters in the d_strategies, since in the redispatch market, it is multiplied by 0
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
        #CS_capita_adjusted cannot be negative:
        if CS_capita_adjusted < 0:
            CS_capita_adjusted = 0
        else: 
            CS_capita_adjusted = CS_capita_adjusted
        CS_aggregate_adjusted = CS_capita_adjusted*(al+ah)
    else:
        #Spot
        q11s = kh
        q12s = (al+ah-kh)
        q21s = (al+ah-kl)
        q22s = kl
        #Redisptach
        q21r=(ah-T)-q21s
        q22r=q22s-(al+T) #This value never enters in the d_strategies, since in the redispatch market, it is multiplied by 0
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
        #CS_capita_adjusted cannot be negative:
        if CS_capita_adjusted < 0:
            CS_capita_adjusted = 0
        else: 
            CS_capita_adjusted = CS_capita_adjusted
        CS_aggregate_adjusted = CS_capita_adjusted*(al+ah)
    welfare_aggregate = CS_aggregate + pi_aggregate
    welfare_aggregate_adjusted = CS_aggregate_adjusted + pi_aggregate
    return Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted
           
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
        q22r=q22s-(al+T) #This value never enters in the d_strategies, since in the redispatch market, it is multiplied by 0
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
        q22r=q22s-(al+T) #This value never enters in the d_strategies, since in the redispatch market, it is multiplied by 0
        #Transmission
        q11t=max(0,kh-ah)
        q12t=max(0,ah-kh)
        q21t=max(0,al-kl) #In fact, for the parameters of the model, q21t=0
        q22t=T
        #CS
        Eh = P
        El = P
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

def d_welfare_pc(Fh, Fl, p, al, ah, T, t, kl, kh, P):
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
        q22r=q22s-(al+T) #This value never enters in the d_strategies, since in the redispatch market, it is multiplied by 0
        #Lower bound
        b1 = t+((P-t)*(ah-T)/q11s)
        b2 = (t*(al+T))/q22s
        b = max(b1,b2)
        pil = (b-t)*q22s
        pih = (b-t)*q11s
        pi_aggregate = pil+pih
        CS_capita_adjusted = CS_capita-(b*q22r/(al+ah))
        #CS_capita_adjusted cannot be negative:
        if CS_capita_adjusted < 0:
            CS_capita_adjusted = 0
        else: 
            CS_capita_adjusted = CS_capita_adjusted
        CS_aggregate_adjusted = CS_capita_adjusted*(al+ah)
    else:
        #Spot
        q11s = kh
        q12s = (al+ah-kh)
        q21s = (al+ah-kl)
        q22s = kl
        #Redisptach
        q21r=(ah-T)-q21s
        q22r=q22s-(al+T) #This value never enters in the d_strategies, since in the redispatch market, it is multiplied by 0
        #Lower bound
        b1 = t+((P-t)*(ah-T)/q11s)
        b2 = (((P-t)*q12s)+(t*(al+T)))/q22s
        b = max(b1,b2)
        pil = (b-t)*q22s
        pih = (b-t)*q11s
        pi_aggregate = pil+pih
        CS_capita_adjusted = CS_capita-(b*q22r/(al+ah))
        #CS_capita_adjusted cannot be negative:
        if CS_capita_adjusted < 0:
            CS_capita_adjusted = 0
        else: 
            CS_capita_adjusted = CS_capita_adjusted
        CS_aggregate_adjusted = CS_capita_adjusted*(al+ah)
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
        q22r=q22s-(al+T) #This value never enters in the d_strategies, since in the redispatch market, it is multiplied by 0
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
        q22r=q22s-(al+T) #This value never enters in the d_strategies, since in the redispatch market, it is multiplied by 0
        #CS
        Eh = 0
        El = 0
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

def d_simulate_model(al, ah, kl, kh, T, t, P, N, model, auction):
    
    if auction == 'discriminatory':    
        if model == 'tt':
            Fh, Fl, p, b1_tt, b2_tt = d_strategies_tt(al, ah, kl, kh, T, t, P, N)
            Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted = d_welfare_tt(Fh, Fl, p, al, ah, T, t, kl, kh, P) 
        else:
            Fh, Fl, p, b1_pc, b2_pc = d_strategies_pc(al, ah, kl, kh, T, t, P, N)
            Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted = d_welfare_pc(Fh, Fl, p, al, ah, T, t, kl, kh, P)
        return Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted
    else:
        if model == 'tt':
            Fh, Fl, p, b1_tt, b2_tt = d_strategies_tt(al, ah, kl, kh, T, t, P, N)
            Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted = u_welfare_tt(Fh, Fl, p, al, ah, T, t, kl, kh, P) 
        else:
            Fh, Fl, p, b1_pc, b2_pc = d_strategies_pc(al, ah, kl, kh, T, t, P, N)
            Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted = u_welfare_pc(Fh, Fl, p, al, ah, T, t, kl, kh, P)
        return Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted


def d_plot_welfare_tt(al, kl, kh, T, t, P, N, N2):
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
        Fh, Fl, p, b1_tt, b2_tt = d_strategies_tt(al, ah, kl, kh, T, t, P, N)
        Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted = d_welfare_tt(Fh, Fl, p, al, ah, T, t, kl, kh, P)
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

def u_plot_welfare_tt(al, kl, kh, T, t, P, N, N2):
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
        Fh, Fl, p, b1_tt, b2_tt = u_strategies_tt(al, ah, kl, kh, T, t, P, N)
        Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted = u_welfare_tt(Fh, Fl, p, al, ah, T, t, kl, kh, P)
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


def d_plot_welfare_pc(al, kl, kh, T, t, P, N, N2):
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
        Fh, Fl, p, b1_pc, b2_pc = d_strategies_pc(al, ah, kl, kh, T, t, P, N)
        Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted = d_welfare_pc(Fh, Fl, p, al, ah, T, t, kl, kh, P)
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

def u_plot_welfare_pc(al, kl, kh, T, t, P, N, N2):
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
        Fh, Fl, p, b1_pc, b2_pc = u_strategies_pc(al, ah, kl, kh, T, t, P, N)
        Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted = u_welfare_pc(Fh, Fl, p, al, ah, T, t, kl, kh, P)
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
        
    #Parameters
    al = 15
    ah = 50.5
    kl = 60
    kh = 60
    T = 40
    t = 1.25
    P = 7
    N = 100
    N2 = 400
    tmax, bl_hat, bh_hat = determine_tmax(al, ah, T, t, P)
    
    ####################################
    ### Discriminatory price auction ###
    ####################################
    
    ##Call the functions
    #Determine the area
    area, area_num = determine_area(al, ah)
    #d_strategies_tt
    Fh_tt, Fl_tt, p_tt, b1_tt, b2_tt = d_strategies_tt(al, ah, kl, kh, T, t, P, N)   
    Eh_tt, El_tt, E_tt, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted=d_welfare_tt(Fh_tt, Fl_tt, p_tt, al, ah, T, t, kl, kh, P)
    #d_strategies_pc
    Fh_pc, Fl_pc, p_pc, b1_pc, b2_pc = d_strategies_pc(al, ah, kl, kh, T, t, P, N)   
    Eh_pc, El_pc, E_pc, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted=d_welfare_pc(Fh_pc, Fl_pc, p_pc, al, ah, T, t, kl, kh, P)
    #Welfare tt
    ah_lst_tt, Eh_lst_tt, El_lst_tt, E_lst_tt, CS_capita_lst_tt, CS_capita_adjusted_lst_tt, CS_aggregate_lst_tt, CS_aggregate_adjusted_lst_tt, pil_lst_tt, pih_lst_tt, pi_aggregate_lst_tt, welfare_aggregate_lst_tt, welfare_aggregate_adjusted_lst_tt=d_plot_welfare_tt(al, kl, kh, T, t, P, N, N2)
    #Welfare pc
    ah_lst_pc, Eh_lst_pc, El_lst_pc, E_lst_pc, CS_capita_lst_pc, CS_capita_adjusted_lst_pc, CS_aggregate_lst_pc, CS_aggregate_adjusted_lst_pc, pil_lst_pc, pih_lst_pc, pi_aggregate_lst_pc, welfare_aggregate_lst_pc, welfare_aggregate_adjusted_lst_pc=d_plot_welfare_pc(al, kl, kh, T, t, P, N, N2)
    #Compare welfare
    ah_lst_tt, Eh_lst_tt, El_lst_tt, E_lst_tt, CS_capita_lst_tt, CS_capita_adjusted_lst_tt, CS_aggregate_lst_tt, CS_aggregate_adjusted_lst_tt, pil_lst_tt, pih_lst_tt, pi_aggregate_lst_tt, welfare_aggregate_lst_tt, welfare_aggregate_adjusted_lst_tt=d_plot_welfare_tt(al, kl, kh, T, t, P, N, N2)
    ah_lst_pc, Eh_lst_pc, El_lst_pc, E_lst_pc, CS_capita_lst_pc, CS_capita_adjusted_lst_pc, CS_aggregate_lst_pc, CS_aggregate_adjusted_lst_pc, pil_lst_pc, pih_lst_pc, pi_aggregate_lst_pc, welfare_aggregate_lst_pc, welfare_aggregate_adjusted_lst_pc=d_plot_welfare_pc(al, kl, kh, T, t, P, N, N2)
    
    ###############################################
    ### Discriminatory price auction: tt vs. pc ###
    ###############################################  
    ##Plot the functions
    import matplotlib.pyplot as plt
    
    #d_profits comparison
    fig, ax = plt.subplots()
    ax.plot(ah_lst_tt, pih_lst_tt, label = 'pih_tt',  color = colors["c"])
    ax.plot(ah_lst_tt, pil_lst_tt, label = 'pil_tt', color = colors["p-g"])
    ax.plot(ah_lst_pc, pih_lst_pc, label = 'Fh_pc',  color = colors["c"], alpha=0.2)
    ax.plot(ah_lst_pc, pil_lst_pc, label = 'Fl_pc', color = colors["p-g"], alpha=0.2)
  
    #d_strategies_tt
    fig, ax = plt.subplots()
    ax.plot(p_tt, Fh_tt, label = 'Fh_tt',  color = colors["c"])
    ax.plot(p_tt, Fl_tt, label = 'Fl_tt', color = colors["p-g"])
    ax.plot([Eh_tt,Eh_tt], [0,1], label = 'Eh_tt',  color = colors["c"])
    ax.plot([El_tt,El_tt], [0,1], label = 'El_tt', color = colors["p-g"])
    ax.plot([E_tt,E_tt], [0,1], label = 'E_tt', color = colors["o-y-c"])
    
    #d_strategies_pc
    fig, ax = plt.subplots()
    ax.plot(p_pc, Fh_pc, label = 'Fh_pc',  color = colors["c"], alpha=1)
    ax.plot(p_pc, Fl_pc, label = 'Fl_pc', color = colors["p-g"], alpha=1)
    ax.plot([Eh_pc,Eh_pc], [0,1], label = 'Eh_pc',  color = colors["c"], alpha=1)
    ax.plot([El_pc,El_pc], [0,1], label = 'El_pc', color = colors["p-g"], alpha=1)
    ax.plot([E_pc,E_pc], [0,1], label = 'E_pc', color = colors["o-y-c"], alpha=1)
    
    #d_strategies comparison
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
    
    #d_strategies paper
    fig, ax = plt.subplots(ncols = 3, figsize = (20, 9))
    #Axes1. tt
    ax[0].plot(p_tt, Fh_tt, label = 'Fh_tt',  color = colors["c"])
    ax[0].plot(p_tt, Fl_tt, label = 'Fl_tt', color = colors["p-g"])
    ax[0].plot([Eh_tt,Eh_tt], [0,1], label = 'Eh_tt',  color = colors["c"])
    ax[0].plot([El_tt,El_tt], [0,1], label = 'El_tt', color = colors["p-g"])
    ax[0].plot([E_tt,E_tt], [0,1], label = 'E_tt', color = colors["o-y-c"])
    ax[0].text(4.55, 0.8, "$F_h^{tt}(b)$", fontsize=18)
    ax[0].text(4.55, 0.95, "$F_l^{tt}(b)$", fontsize=18)
    ax[0].text(1.25, 1.01, "$E_l^{tt}$", fontsize=18)
    ax[0].text(2.2, 1.01, "$E^{tt}$", fontsize=18)
    ax[0].text(2.9, 1.01, "$E_h^{tt}$", fontsize=18)
    ax[0].set_ylim(0, 1.1)
    ax[0].set(xticks=[0, b1_tt, P], xticklabels=['0', '${b}^{tt}$', 'P'],
              yticks=[0, 1], yticklabels=['0', '1'])
    ax[0].set_ylabel('$\\theta_h$', fontsize=18)
    ax[0].set_xlabel('$\\theta_l$', fontsize=18)
    ax[0].set_title('strategies tt', fontsize=20)
    #Axes2. tt vs. pc
    ax[1].plot(p_tt, Fh_tt, label = 'Fh_tt',  color = colors["c"])
    ax[1].plot(p_tt, Fl_tt, label = 'Fl_tt', color = colors["p-g"])
    ax[1].plot([Eh_tt,Eh_tt], [0,1], label = 'Eh_tt',  color = colors["c"])
    ax[1].plot([El_tt,El_tt], [0,1], label = 'El_tt', color = colors["p-g"])
    ax[1].plot([E_tt,E_tt], [0,1], label = 'E_tt', color = colors["o-y-c"])
    ax[1].text(4.55, 0.8, "$F_h^{tt}(b)$", fontsize=18)
    ax[1].text(4.55, 0.95, "$F_l^{tt}(b)$", fontsize=18)
    ax[1].text(1.25, 1.01, "$E_l^{tt}$", fontsize=18)
    ax[1].text(2.2, 1.01, "$E^{tt}$", fontsize=18)
    ax[1].text(2.9, 1.01, "$E_h^{tt}$", fontsize=18)
        
    ax[1].plot(p_pc, Fh_pc, label = 'Fh_pc',  color = colors["c"], alpha=0.3)
    ax[1].plot(p_pc, Fl_pc, label = 'Fl_pc', color = colors["p-g"], alpha=0.3)
    ax[1].plot([Eh_pc,Eh_pc], [0,1], label = 'Eh_pc',  color = colors["c"], alpha=0.3)
    ax[1].plot([El_pc,El_pc], [0,1], label = 'El_pc', color = colors["p-g"], alpha=0.3)
    ax[1].plot([E_pc,E_pc], [0,1], label = 'E_pc', color = colors["o-y-c"], alpha=0.3)
    ax[1].set_ylim(0, 1.1)
    ax[1].set(xticks=[0, b1_tt, b1_pc, P], xticklabels=['0', '${b}^{tt}$', '${b}^{pc}$', 'P'],
              yticks=[0, 1], yticklabels=['0', '1'])
    ax[1].set_ylabel('$\\theta_h$', fontsize=18)
    ax[1].set_xlabel('$\\theta_l$', fontsize=18)
    ax[1].set_title('strategies tt vs. pc', fontsize=20)
    #Axes3. pc
    ax[2].plot(p_pc, Fh_pc, label = 'Fh_pc',  color = colors["c"], alpha=0.3)
    ax[2].plot(p_pc, Fl_pc, label = 'Fl_pc', color = colors["p-g"], alpha=0.3)
    ax[2].plot([Eh_pc,Eh_pc], [0,1], label = 'Eh_pc',  color = colors["c"], alpha=0.3)
    ax[2].plot([El_pc,El_pc], [0,1], label = 'El_pc', color = colors["p-g"], alpha=0.3)
    ax[2].plot([E_pc,E_pc], [0,1], label = 'E_pc', color = colors["o-y-c"], alpha=0.3)
    ax[2].text(4.55+1.2, 0.75, "$F_h^{pc}(b)$", fontsize=18, alpha=1)
    ax[2].text(4.55+1.2, 1.01, "$F_l^{pc}(b)$", fontsize=18, alpha=1)
    ax[2].text(1.25+1.2, 1.01, "$E_l^{pc}$", fontsize=18, alpha=1)
    ax[2].text(2.2+1.2, 1.01, "$E^{pc}$", fontsize=18, alpha=1)
    ax[2].text(2.9+1.2, 1.01, "$E_h^{pc}$", fontsize=18, alpha=1)
    ax[2].set_ylim(0, 1.1)
    ax[2].set(xticks=[0, b1_pc, P], xticklabels=['0', '${b}^{pc}$', 'P'],
              yticks=[0, 1], yticklabels=['0', '1'])
    ax[2].set_ylabel('$\\theta_h$', fontsize=18)
    ax[2].set_xlabel('$\\theta_l$', fontsize=18)
    ax[2].set_title('strategies pc', fontsize=20)
    plt.show()
    

 
    #Welfare tt
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
    fig, ax = plt.subplots()
    ax.plot(ah_lst_tt, Eh_lst_tt, label = 'Eh_lst_tt', color = colors["c"], alpha=1)
    ax.plot(ah_lst_tt, El_lst_tt, label = 'El_lst_tt', color = colors["p-g"], alpha=1)
    ax.plot(ah_lst_tt, E_lst_tt, label = 'E_lst_tt', color = colors["o-y-c"], alpha=1) 
    ax.plot(ah_lst_pc, Eh_lst_pc, label = 'Eh_lst_pc', color = colors["c"], alpha=0.3)
    ax.plot(ah_lst_pc, El_lst_pc, label = 'El_lst_pc', color = colors["p-g"], alpha=0.3)
    ax.plot(ah_lst_pc, E_lst_pc, label = 'E_lst_pc', color = colors["o-y-c"], alpha=0.3)
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
    
    #d_welfare paper
    fig, ax = plt.subplots(ncols = 4, figsize = (20, 9))
    #Axes1. E
    ax[0].plot(ah_lst_tt, Eh_lst_tt, label = 'Eh_lst_tt', color = colors["c"], alpha=1)
    ax[0].plot(ah_lst_tt, El_lst_tt, label = 'El_lst_tt', color = colors["p-g"], alpha=1)
    ax[0].plot(ah_lst_tt, E_lst_tt, label = 'E_lst_tt', color = colors["o-y-c"], alpha=1) 
    ax[0].plot(ah_lst_pc, Eh_lst_pc, label = 'Eh_lst_pc', color = colors["c"], alpha=0.3)
    ax[0].plot(ah_lst_pc, El_lst_pc, label = 'El_lst_pc', color = colors["p-g"], alpha=0.3)
    ax[0].plot(ah_lst_pc, E_lst_pc, label = 'E_lst_pc', color = colors["o-y-c"], alpha=0.3)
    
    ax[0].text(40, 1.4, "$E^{tt}$", fontsize=18)
    ax[0].text(40, 0.78, "$E_h^{tt}$", fontsize=18)
    ax[0].text(40, 2.5, "$E_l^{tt}$", fontsize=18)

    ax[0].set_ylim(0.75, 7.5)
    ax[0].set(xticks=[41, 70, 99], xticklabels=['41', '70', '99'],
              yticks=[1, 7], yticklabels=['1', 'P'])
    ax[0].set_xlabel('$\\theta_h$', fontsize=18)
    ax[0].set_ylabel('expected price', fontsize=18)
    ax[0].yaxis.set_label_coords(-0.02, 0.5)
    ax[0].set_title('expected price tt vs. pc', fontsize=20)
    #Axes2. CS_adjusted
    ax[1].plot(ah_lst_tt, CS_aggregate_adjusted_lst_tt, label = 'CS_aggregate_adjusted_lst_tt', color = colors["b-s"], alpha=1)
    ax[1].plot(ah_lst_tt, CS_aggregate_lst_tt, label = 'CS_aggregate_lst_tt', color = colors["c"], alpha=1)
    ax[1].plot(ah_lst_pc, CS_aggregate_adjusted_lst_pc, label = 'CS_aggregate_adjusted_lst_pc', color = colors["b-s"], alpha=0.3)
    ax[1].plot(ah_lst_pc, CS_aggregate_lst_pc, label = 'CS_aggregate_lst_pc', color = colors["c"], alpha=0.3)
    
    ax[1].text(75, 150, "$CS^{tt}$", fontsize=18)
    ax[1].text(43, 150, "$CS_{adjusted}^{tt}$", fontsize=18)
    
    ax[1].set_ylim(0, 350)
    ax[1].set(xticks=[41, 70, 99], xticklabels=['41', '70', '99'],
              yticks=[0, 350], yticklabels=['0', '350'])
    ax[1].set_xlabel('$\\theta_h$', fontsize=18)
    ax[1].set_ylabel('CS adjusted', fontsize=18)
    ax[1].yaxis.set_label_coords(-0.02, 0.5)
    ax[1].set_title('CS adjusted tt vs. pc', fontsize=20)
    #Axes3. profits
    ax[2].plot(ah_lst_tt, pih_lst_tt, label = 'pih_lst_tt', color = colors["c"], alpha=1)
    ax[2].plot(ah_lst_tt, pil_lst_tt, label = 'pil_lst_tt', color = colors["p-g"], alpha=1)
    #ax[2].plot(ah_lst_pc, pih_lst_pc, label = 'pih_lst_pc', color = colors["c"], alpha=0.3)
    ax[2].plot(ah_lst_pc, pil_lst_pc, label = 'pil_lst_pc', color = colors["p-g"], alpha=0.3)
    
    ax[2].text(70, 140, "$\pi_l^{tt}$", fontsize=18)
    ax[2].text(50, 140, "$\pi_h^{tt}$", fontsize=18)
    
    ax[2].set_ylim(0, 420)
    ax[2].set(xticks=[41, 70, 99], xticklabels=['41', '70', '99'],
              yticks=[0, 420], yticklabels=['0', '420'])
    ax[2].set_xlabel('$\\theta_h$', fontsize=18)
    ax[2].set_ylabel('profits', fontsize=18)
    ax[2].yaxis.set_label_coords(-0.02, 0.5)
    ax[2].set_title('profits tt vs. pc', fontsize=20)
    #Axes4. welfare
    ax[3].plot(ah_lst_tt, welfare_aggregate_adjusted_lst_tt, label = 'CS_aggregate_adjusted_lst_tt', color = colors["b-s"], alpha=1)
    ax[3].plot(ah_lst_tt, welfare_aggregate_lst_tt, label = 'CS_aggregate_lst_tt', color = colors["c"], alpha=1)
    ax[3].plot(ah_lst_pc, welfare_aggregate_adjusted_lst_pc, label = 'CS_aggregate_adjusted_lst_pc', color = colors["b-s"], alpha=0.3)
    ax[3].plot(ah_lst_pc, welfare_aggregate_lst_pc, label = 'CS_aggregate_lst_pc', color = colors["c"], alpha=0.3)
    
    ax[3].text(43, 500, "$welfare^{tt}$", fontsize=18)
    ax[3].text(65, 440, "$welfare_{adjusted}^{tt}$", fontsize=18)
    
    ax[3].set(xticks=[41, 70, 99], xticklabels=['41', '70', '99'],
              yticks=[250, 800], yticklabels=['250', '800'])
    ax[3].set_xlabel('$\\theta_h$', fontsize=18)
    ax[3].set_ylabel('welfare adjusted', fontsize=18)
    ax[3].yaxis.set_label_coords(-0.02, 0.5)
    ax[3].set_title('welfare adjusted tt vs. pc', fontsize=20)
    plt.show()

    #Heatcolor map
    N2 = 100
    ah_lst = np.linspace(99, 41, N2)
    al_lst = np.linspace(1, 19, N2)
    
    #Initialize tt
    El_lst_tt = []
    Eh_lst_tt = []
    E_lst_tt = []
    CS_aggregate_adjusted_lst_tt = []
    pil_lst_tt = []
    pih_lst_tt = []
    pi_aggregate_lst_tt = []
    welfare_aggregate_adjusted_lst_tt = []
    
    #Initialize pc
    El_lst_pc = []
    Eh_lst_pc = []
    E_lst_pc = []
    CS_aggregate_adjusted_lst_pc = []
    pil_lst_pc = []
    pih_lst_pc = []
    pi_aggregate_lst_pc = []
    welfare_aggregate_adjusted_lst_pc = []

    for ah in ah_lst:
            
        #temp_lst_tt = []
        temp_El_lst_tt = []
        temp_Eh_lst_tt = []
        temp_E_lst_tt = []
        temp_CS_aggregate_adjusted_lst_tt = []
        temp_pil_lst_tt = []
        temp_pih_lst_tt = []
        temp_pi_aggregate_lst_tt = []
        temp_welfare_aggregate_adjusted_lst_tt = []
        
        #temp_lst_pc = []
        temp_El_lst_pc = []
        temp_Eh_lst_pc = []
        temp_E_lst_pc = []
        temp_CS_aggregate_adjusted_lst_pc = []
        temp_pil_lst_pc = []
        temp_pih_lst_pc = []
        temp_pi_aggregate_lst_pc = []
        temp_welfare_aggregate_adjusted_lst_pc = []
      
        for al in al_lst:
            Eh_tt, El_tt, E_tt, CS_capita_tt, CS_capita_adjusted_tt, CS_aggregate_tt, CS_aggregate_adjusted_tt, pil_tt, pih_tt, pi_aggregate_tt, welfare_aggregate_tt, welfare_aggregate_adjusted_tt=d_simulate_model(al, ah, kl, kh, T, t, P, N, model = 'tt', auction='discriminatory')
            Eh_pc, El_pc, E_pc, CS_capita_pc, CS_capita_adjusted_pc, CS_aggregate_pc, CS_aggregate_adjusted_pc, pil_pc, pih_pc, pi_aggregate_pc, welfare_aggregate_pc, welfare_aggregate_adjusted_pc=d_simulate_model(al, ah, kl, kh, T, t, P, N, model = 'pc', auction='discriminatory')
            
            #Append tt
            temp_El_lst_tt.append(El_tt)
            temp_Eh_lst_tt.append(Eh_tt)
            temp_E_lst_tt.append(E_tt)
            temp_CS_aggregate_adjusted_lst_tt.append(CS_aggregate_adjusted_tt)
            temp_pil_lst_tt.append(pil_tt)
            temp_pih_lst_tt.append(pih_tt)
            temp_pi_aggregate_lst_tt.append(pi_aggregate_tt)
            temp_welfare_aggregate_adjusted_lst_tt.append(welfare_aggregate_adjusted_tt)
            
            #Append pc
            temp_El_lst_pc.append(El_pc)
            temp_Eh_lst_pc.append(Eh_pc)
            temp_E_lst_pc.append(E_pc)
            temp_CS_aggregate_adjusted_lst_pc.append(CS_aggregate_adjusted_pc)
            temp_pil_lst_pc.append(pil_pc)
            temp_pih_lst_pc.append(pih_pc)
            temp_pi_aggregate_lst_pc.append(pi_aggregate_pc)
            temp_welfare_aggregate_adjusted_lst_pc.append(welfare_aggregate_adjusted_pc)
            
        #Append lst_tt
        El_lst_tt.append(temp_El_lst_tt)
        Eh_lst_tt.append(temp_Eh_lst_tt)
        E_lst_tt.append(temp_E_lst_tt)
        CS_aggregate_adjusted_lst_tt.append(temp_CS_aggregate_adjusted_lst_tt)
        pil_lst_tt.append(temp_pil_lst_tt)
        pih_lst_tt.append(temp_pih_lst_tt)
        pi_aggregate_lst_tt.append(temp_pi_aggregate_lst_tt)
        welfare_aggregate_adjusted_lst_tt.append(temp_welfare_aggregate_adjusted_lst_tt)
        
        #Append lst_pc
        El_lst_pc.append(temp_El_lst_pc)
        Eh_lst_pc.append(temp_Eh_lst_pc)
        E_lst_pc.append(temp_E_lst_pc)
        CS_aggregate_adjusted_lst_pc.append(temp_CS_aggregate_adjusted_lst_pc)
        pil_lst_pc.append(temp_pil_lst_pc)
        pih_lst_pc.append(temp_pih_lst_pc)
        pi_aggregate_lst_pc.append(temp_pi_aggregate_lst_pc)
        welfare_aggregate_adjusted_lst_pc.append(temp_welfare_aggregate_adjusted_lst_pc)
    
    #Array tt
    El_array_tt = np.array(El_lst_tt)
    Eh_array_tt = np.array(Eh_lst_tt)
    E_array_tt = np.array(E_lst_tt)
    CS_aggregate_adjusted_array_tt = np.array(CS_aggregate_adjusted_lst_tt)
    pil_array_tt = np.array(pil_lst_tt)
    pih_array_tt = np.array(pih_lst_tt)
    pi_aggregate_array_tt = np.array(pi_aggregate_lst_tt)
    welfare_aggregate_adjusted_array_tt = np.array(welfare_aggregate_adjusted_lst_tt)
    
    #Array pc
    El_array_pc = np.array(El_lst_pc)
    Eh_array_pc = np.array(Eh_lst_pc)
    E_array_pc = np.array(E_lst_pc)
    CS_aggregate_adjusted_array_pc = np.array(CS_aggregate_adjusted_lst_pc)
    pil_array_pc = np.array(pil_lst_pc)
    pih_array_pc = np.array(pih_lst_pc)
    pi_aggregate_array_pc = np.array(pi_aggregate_lst_pc)
    welfare_aggregate_adjusted_array_pc = np.array(welfare_aggregate_adjusted_lst_pc)
    
    #Array diff
    El_diff = El_array_pc - El_array_tt
    Eh__diff = Eh_array_pc - Eh_array_tt
    E_diff = E_array_tt -E_array_pc
    #CS. Prior belief: CS_tt>CS_pc
    CS_aggregate_adjusted_diff = CS_aggregate_adjusted_array_tt - CS_aggregate_adjusted_array_pc
    pil_diff = pil_array_pc - pil_array_tt
    pih_diif = pih_array_pc - pih_array_tt
    #pi. Prior belief: pi_tt>pi_pc
    pi_aggregate_diff = pi_aggregate_array_tt - pi_aggregate_array_pc
    #welfare. Prior belief: welfare_tt>welfare_pc
    welfare_aggregate_adjusted_diff = welfare_aggregate_adjusted_array_tt - welfare_aggregate_adjusted_array_pc
    
    #Heat color E, CS_aggregate_adjusted, profits, welfare_adjusted
    import matplotlib.pyplot as plt
    vmin_E =  E_diff.min()
    vmax_E =  E_diff.max()
    fig, ax = plt.subplots(ncols = 4, figsize = (20, 9))
    c0 = ax[0].pcolormesh(al_lst, ah_lst, E_diff, cmap = 'viridis', vmin = vmin_E, vmax = vmax_E)
    ax[0].set_position([0.05+(0.85/4)*0, 0.15, 0.15, 0.7])
    ax[0].set(xticks=[1, 5, 10, 15, 19], xticklabels=['1', '5', '10', '15', '19'],
              yticks=[41, 50, 60, 70, 80, 90, 99], yticklabels=['41', '50', '60', '70', '80', '90', '99'])
    ax[0].set_ylabel('$\\theta_h$', fontsize=18)
    ax[0].set_xlabel('$\\theta_l$', fontsize=18)
    ax[0].set_title('price (tt-pc)', fontsize=20)
    cbar_ax = fig.add_axes([0.05+(0.15*1)+0.01, 0.15, 0.01, 0.7])
    fig.colorbar(c0, cax=cbar_ax)
    #CS_aggregate_adjusted
    vmin_CS =  CS_aggregate_adjusted_diff.min()
    vmax_CS =  CS_aggregate_adjusted_diff.max()
    c1 = ax[1].pcolormesh(al_lst, ah_lst, CS_aggregate_adjusted_diff, cmap = 'viridis', vmin = vmin_CS, vmax = vmax_CS)
    ax[1].set_position([0.05+(0.85/4)*1, 0.15, 0.15, 0.7])
    ax[1].set(xticks=[1, 5, 10, 15, 19], xticklabels=['1', '5', '10', '15', '19'],
              yticks=[41, 50, 60, 70, 80, 90, 99], yticklabels=['41', '50', '60', '70', '80', '90', '99'])
    ax[1].set_ylabel('$\\theta_h$', fontsize=18)
    ax[1].set_xlabel('$\\theta_l$', fontsize=18)
    ax[1].set_title('CS adjusted (tt-pc)', fontsize=20)
    cbar_ax = fig.add_axes([0.05+(0.85/4)*1+(0.15)+0.01, 0.15, 0.01, 0.7])
    fig.colorbar(c1, cax=cbar_ax)
    #pi
    vmin_pi =  pi_aggregate_diff.min()
    vmax_pi =  pi_aggregate_diff.max()
    c2 = ax[2].pcolormesh(al_lst, ah_lst, pi_aggregate_diff, cmap = 'viridis', vmin = vmin_pi, vmax = vmax_pi)
    ax[2].set_position([0.05+(0.85/4)*2, 0.15, 0.15, 0.7])
    ax[2].set(xticks=[1, 5, 10, 15, 19], xticklabels=['1', '5', '10', '15', '19'],
              yticks=[41, 50, 60, 70, 80, 90, 99], yticklabels=['41', '50', '60', '70', '80', '90', '99'])
    ax[2].set_ylabel('$\\theta_h$', fontsize=18)
    ax[2].set_xlabel('$\\theta_l$', fontsize=18)
    ax[2].set_title('profit (tt-pc)', fontsize=20)
    cbar_ax = fig.add_axes([0.05+(0.85/4)*2+(0.15)+0.01, 0.15, 0.01, 0.7])
    fig.colorbar(c2, cax=cbar_ax)
    #welfare_aggregate_adjusted
    vmin_w =  welfare_aggregate_adjusted_diff.min()
    vmax_w =  welfare_aggregate_adjusted_diff.max()
    c3 = ax[3].pcolormesh(al_lst, ah_lst, welfare_aggregate_adjusted_diff, cmap = 'viridis', vmin = vmin_w, vmax = vmax_w)
    ax[3].set_position([0.05+(0.85/4)*3, 0.15, 0.15, 0.7])
    ax[3].set(xticks=[1, 5, 10, 15, 19], xticklabels=['1', '5', '10', '15', '19'],
              yticks=[41, 50, 60, 70, 80, 90, 99], yticklabels=['41', '50', '60', '70', '80', '90', '99'])
    ax[3].set_ylabel('$\\theta_h$', fontsize=18)
    ax[3].set_xlabel('$\\theta_l$', fontsize=18)
    ax[3].set_title('welfare adjusted (tt-pc)', fontsize=20)
    cbar_ax = fig.add_axes([0.05+(0.85/4)*3+(0.15)+0.01, 0.15, 0.01, 0.7])
    fig.colorbar(c3, cax=cbar_ax)
    plt.show()

    #############################
    ### Uniform price auction ###
    #############################    
    
    ##Call the functions
    #Determine the area
    area, area_num = determine_area(al, ah)
    #d_strategies_tt
    u_Fh_tt, u_Fl_tt, u_p_tt, u_b1_tt, u_b2_tt = u_strategies_tt(al, ah, kl, kh, T, t, P, N)   
    u_Eh_tt, u_El_tt, u_E_tt, u_CS_capita, u_CS_capita_adjusted, u_CS_aggregate, u_CS_aggregate_adjusted, u_pil, u_pih, u_pi_aggregate, u_welfare_aggregate, u_welfare_aggregate_adjusted=u_welfare_tt(u_Fh_tt, u_Fl_tt, u_p_tt, al, ah, T, t, kl, kh, P)
    #d_strategies_pc
    u_Fh_pc, u_Fl_pc, u_p_pc, u_b1_pc, u_b2_pc = u_strategies_pc(al, ah, kl, kh, T, t, P, N)   
    u_Eh_pc, u_El_pc, u_E_pc, u_CS_capita, u_CS_capita_adjusted, u_CS_aggregate, u_CS_aggregate_adjusted, u_pil, u_pih, u_pi_aggregate, u_welfare_aggregate, u_welfare_aggregate_adjusted=u_welfare_pc(u_Fh_pc, u_Fl_pc, u_p_pc, al, ah, T, t, kl, kh, P)
    #Welfare tt
    u_ah_lst_tt, u_Eh_lst_tt, u_El_lst_tt, u_E_lst_tt, u_CS_capita_lst_tt, u_CS_capita_adjusted_lst_tt, u_CS_aggregate_lst_tt, u_CS_aggregate_adjusteu_lst_tt, u_pil_lst_tt, u_pih_lst_tt, u_pi_aggregate_lst_tt, u_welfare_aggregate_lst_tt, u_welfare_aggregate_adjusted_lst_tt=u_plot_welfare_tt(al, kl, kh, T, t, P, N, N2)
    #Welfare pc
    u_ah_lst_pc, u_Eh_lst_pc, u_El_lst_pc, u_E_lst_pc, u_CS_capita_lst_pc, u_CS_capita_adjusted_lst_pc, u_CS_aggregate_lst_pc, u_CS_aggregate_adjusted_lst_pc, pil_lst_pc, pih_lst_pc, pi_aggregate_lst_pc, welfare_aggregate_lst_pc, welfare_aggregate_adjusted_lst_pc=u_plot_welfare_pc(al, kl, kh, T, t, P, N, N2)
    #Compare welfare
    u_ah_lst_tt, u_Eh_lst_tt, u_El_lst_tt, u_E_lst_tt, u_CS_capita_lst_tt, u_CS_capita_adjusteu_lst_tt, u_CS_aggregatu_E_lst_tt, u_CS_aggregate_adjusted_lst_tt, u_pil_lst_tt, u_pih_lst_tt, u_pi_aggregate_lst_tt, u_welfare_aggregate_lst_tt, u_welfare_aggregate_adjusted_lst_tt=u_plot_welfare_tt(al, kl, kh, T, t, P, N, N2)
    u_ah_lst_pc, u_Eh_lst_pc, u_El_lst_pc, u_E_lst_pc, u_CS_capita_lst_pc, u_CS_capita_adjusted_lst_pc, u_CS_aggregate_lst_pc, u_CS_aggregate_adjusted_lst_pc, u_pil_lst_pc, u_pih_lst_pc, u_pi_aggregate_lst_pc, u_welfare_aggregate_lst_pc, u_welfare_aggregate_adjusted_lst_pc=u_plot_welfare_pc(al, kl, kh, T, t, P, N, N2)

    ########################################
    ### Uniform price auction: tt vs. pc ###
    ########################################  
    ##Plot the functions
    import matplotlib.pyplot as plt
    
    #u_strategies_tt
    fig, ax = plt.subplots()
    ax.plot(u_p_tt, u_Fh_tt, label = 'u_Fh_tt',  color = colors["c"])
    ax.plot(u_p_tt, u_Fl_tt, label = 'Fl_tt', color = colors["p-g"])
    ax.plot([u_Eh_tt,u_Eh_tt], [0,1], label = 'u_Eh_tt',  color = colors["c"])
    ax.plot([u_El_tt,u_El_tt], [0,1], label = 'u_El_tt', color = colors["p-g"])
    ax.plot([u_E_tt,u_E_tt], [0,1], label = 'E_tt', color = colors["o-y-c"])
    
    #u_strategies_pc
    fig, ax = plt.subplots()
    ax.plot(u_p_pc, u_Fh_pc, label = 'u_Fh_pc',  color = colors["c"], alpha=1)
    ax.plot(u_p_pc, u_Fl_pc, label = 'Fl_pc', color = colors["p-g"], alpha=1)
    ax.plot([u_Eh_pc,u_Eh_pc], [0,1], label = 'u_Eh_pc',  color = colors["c"], alpha=1)
    ax.plot([u_El_pc,u_El_pc], [0,1], label = 'u_El_pc', color = colors["p-g"], alpha=1)
    ax.plot([u_E_pc,u_E_pc], [0,1], label = 'E_pc', color = colors["o-y-c"], alpha=1)
    
    #u_strategies comparison
    fig, ax = plt.subplots()
    ax.plot(u_p_tt, u_Fh_tt, label = 'u_Fh_tt',  color = colors["c"])
    ax.plot(u_p_tt, u_Fl_tt, label = 'u_Fl_tt', color = colors["p-g"])
    ax.plot([u_Eh_tt,u_Eh_tt], [0,1], label = 'u_Eh_tt',  color = colors["c"])
    ax.plot([u_El_tt,u_El_tt], [0,1], label = 'u_El_tt', color = colors["p-g"])
    ax.plot([u_E_tt,u_E_tt], [0,1], label = 'E_tt', color = colors["o-y-c"])
    ax.plot(u_p_pc, u_Fh_pc, label = 'u_Fh_pc',  color = colors["c"], alpha=0.2)
    ax.plot(u_p_pc, u_Fl_pc, label = 'u_Fl_pc', color = colors["p-g"], alpha=0.2)
    ax.plot([u_Eh_pc,u_Eh_pc], [0,1], label = 'u_Eh_pc',  color = colors["c"], alpha=0.2)
    ax.plot([u_El_pc,u_El_pc], [0,1], label = 'u_El_pc', color = colors["p-g"], alpha=0.2)
    ax.plot([u_E_pc,u_E_pc], [0,1], label = 'E_pc', color = colors["o-y-c"], alpha=0.2)
    
    #Welfare tt
    fig, ax = plt.subplots()
    ax.plot(u_ah_lst_tt, u_Eh_lst_tt, label = 'u_Eh_lst_tt', color = colors["c"], alpha=1)
    ax.plot(u_ah_lst_tt, u_El_lst_tt, label = 'u_El_lst_tt', color = colors["p-g"], alpha=1)
    ax.plot(u_ah_lst_tt, u_E_lst_tt, label = 'u_E_lst_tt', color = colors["o-y-c"], alpha=1)
    fig, ax = plt.subplots()
    ax.plot(u_ah_lst_tt, u_CS_aggregate_adjusted_lst_tt, label = 'u_CS_aggregate_adjusted_lst_tt', color = colors["b-s"], alpha=1)
    ax.plot(u_ah_lst_tt, u_CS_aggregate_lst_tt, label = 'u_CS_aggregate_lst_tt', color = colors["c"], alpha=1)
    fig, ax = plt.subplots()
    ax.plot(u_ah_lst_tt, u_pil_lst_tt, label = 'u_pil_lst_tt', color = colors["c"], alpha=1)
    ax.plot(u_ah_lst_tt, u_pih_lst_tt, label = 'u_pih_lst_tt', color = colors["p-g"], alpha=1)
    fig, ax = plt.subplots()
    ax.plot(u_ah_lst_tt, u_welfare_aggregate_adjusted_lst_tt, label = 'u_CS_aggregate_adjusted_lst_tt', color = colors["b-s"], alpha=1)
    ax.plot(u_ah_lst_tt, u_welfare_aggregate_lst_tt, label = 'u_CS_aggregate_lst_tt', color = colors["c"], alpha=1)
    
    
    #Welfare pc
    fig, ax = plt.subplots()
    ax.plot(u_ah_lst_pc, u_Eh_lst_pc, label = 'u_Eh_lst_pc', color = colors["c"], alpha=0.2)
    ax.plot(u_ah_lst_pc, u_El_lst_pc, label = 'u_El_lst_pc', color = colors["p-g"], alpha=0.2)
    ax.plot(u_ah_lst_pc, u_E_lst_pc, label = 'u_E_lst_pc', color = colors["o-y-c"], alpha=0.2)
    fig, ax = plt.subplots()
    ax.plot(u_ah_lst_pc, u_CS_aggregate_adjusted_lst_pc, label = 'u_CS_aggregate_adjusted_lst_pc', color = colors["b-s"], alpha=0.2)
    ax.plot(u_ah_lst_pc, u_CS_aggregate_lst_pc, label = 'u_CS_aggregate_lst_pc', color = colors["c"], alpha=0.2)
    fig, ax = plt.subplots()
    ax.plot(u_ah_lst_pc, u_pil_lst_pc, label = 'u_pil_lst_pc', color = colors["c"], alpha=0.2)
    ax.plot(u_ah_lst_pc, u_pih_lst_pc, label = 'u_pih_lst_pc', color = colors["p-g"], alpha=0.2)
    fig, ax = plt.subplots()
    ax.plot(u_ah_lst_pc, welfare_aggregate_adjusted_lst_pc, label = 'u_CS_aggregate_adjusted_lst_pc', color = colors["b-s"], alpha=0.2)
    ax.plot(u_ah_lst_pc, u_welfare_aggregate_lst_pc, label = 'u_CS_aggregate_lst_pc', color = colors["c"], alpha=0.2)
    
    #Compare u_welfare
    fig, ax = plt.subplots()
    ax.plot(u_ah_lst_tt, u_Eh_lst_tt, label = 'u_Eh_lst_tt', color = colors["c"], alpha=1)
    ax.plot(u_ah_lst_tt, u_El_lst_tt, label = 'u_El_lst_tt', color = colors["p-g"], alpha=1)
    ax.plot(u_ah_lst_tt, u_E_lst_tt, label = 'u_E_lst_tt', color = colors["o-y-c"], alpha=1) 
    ax.plot(u_ah_lst_pc, u_Eh_lst_pc, label = 'u_Eh_lst_pc', color = colors["c"], alpha=0.2)
    ax.plot(u_ah_lst_pc, u_El_lst_pc, label = 'u_El_lst_pc', color = colors["p-g"], alpha=0.2)
    ax.plot(u_ah_lst_pc, u_E_lst_pc, label = 'u_E_lst_pc', color = colors["o-y-c"], alpha=0.2)
    fig, ax = plt.subplots()
    ax.plot(u_ah_lst_tt, u_CS_aggregate_adjusted_lst_tt, label = 'u_CS_aggregate_adjusted_lst_tt', color = colors["b-s"], alpha=1)
    ax.plot(u_ah_lst_tt, u_CS_aggregate_lst_tt, label = 'u_CS_aggregate_lst_tt', color = colors["c"], alpha=1)
    ax.plot(u_ah_lst_pc, u_CS_aggregate_adjusted_lst_pc, label = 'u_CS_aggregate_adjusted_lst_pc', color = colors["b-s"], alpha=0.2)
    ax.plot(u_ah_lst_pc, u_CS_aggregate_lst_pc, label = 'u_CS_aggregate_lst_pc', color = colors["c"], alpha=0.2)
    fig, ax = plt.subplots()
    ax.plot(u_ah_lst_tt, u_pil_lst_tt, label = 'u_pil_lst_tt', color = colors["c"], alpha=1)
    ax.plot(u_ah_lst_tt, u_pih_lst_tt, label = 'u_pih_lst_tt', color = colors["p-g"], alpha=1)
    ax.plot(u_ah_lst_pc, u_pil_lst_pc, label = 'u_pil_lst_pc', color = colors["c"], alpha=0.2)
    ax.plot(u_ah_lst_pc, u_pih_lst_pc, label = 'u_pih_lst_pc', color = colors["p-g"], alpha=0.2)
    fig, ax = plt.subplots()
    ax.plot(u_ah_lst_tt, u_welfare_aggregate_adjusted_lst_tt, label = 'u_CS_aggregate_adjusted_lst_tt', color = colors["b-s"], alpha=1)
    ax.plot(u_ah_lst_tt, u_welfare_aggregate_lst_tt, label = 'u_CS_aggregate_lst_tt', color = colors["c"], alpha=1)
    ax.plot(u_ah_lst_pc, u_welfare_aggregate_adjusted_lst_pc, label = 'u_CS_aggregate_adjusted_lst_pc', color = colors["b-s"], alpha=0.2)
    ax.plot(u_ah_lst_pc, u_welfare_aggregate_lst_pc, label = 'u_CS_aggregate_lst_pc', color = colors["c"], alpha=0.2)


    #Heatcolor map
    N2 = 100
    u_ah_lst = np.linspace(99, 41, N2)
    u_al_lst = np.linspace(1, 19, N2)
    
    #Initialize tt
    u_El_lst_tt = []
    u_Eh_lst_tt = []
    u_E_lst_tt = []
    u_CS_aggregate_adjusted_lst_tt = []
    u_pil_lst_tt = []
    u_pih_lst_tt = []
    u_pi_aggregate_lst_tt = []
    u_welfare_aggregate_adjusted_lst_tt = []
    
    #Initialize pc
    u_El_lst_pc = []
    u_Eh_lst_pc = []
    u_E_lst_pc = []
    u_CS_aggregate_adjusted_lst_pc = []
    u_pil_lst_pc = []
    u_pih_lst_pc = []
    u_pi_aggregate_lst_pc = []
    u_welfare_aggregate_adjusted_lst_pc = []

    for ah in u_ah_lst:
            
        #temp_lst_tt = []
        u_temp_El_lst_tt = []
        u_temp_Eh_lst_tt = []
        u_temp_E_lst_tt = []
        u_temp_CS_aggregate_adjusted_lst_tt = []
        u_temp_pil_lst_tt = []
        u_temp_pih_lst_tt = []
        u_temp_pi_aggregate_lst_tt = []
        u_temp_welfare_aggregate_adjusted_lst_tt = []
        
        #u_temp_lst_pc = []
        u_temp_El_lst_pc = []
        u_temp_Eh_lst_pc = []
        u_temp_E_lst_pc = []
        u_temp_CS_aggregate_adjusted_lst_pc = []
        u_temp_pil_lst_pc = []
        u_temp_pih_lst_pc = []
        u_temp_pi_aggregate_lst_pc = []
        u_temp_welfare_aggregate_adjusted_lst_pc = []
      
        for al in u_al_lst:
            u_Eh_tt, u_El_tt, u_E_tt, u_CS_capita_tt, u_CS_capita_adjusted_tt, u_CS_aggregate_tt, u_CS_aggregate_adjusted_tt, u_pil_tt, u_pih_tt, u_pi_aggregate_tt, u_welfare_aggregate_tt, u_welfare_aggregate_adjusted_tt=d_simulate_model(al, ah, kl, kh, T, t, P, N, model = 'tt', auction='uniform')
            u_Eh_pc, u_El_pc, u_E_pc, u_CS_capita_pc, u_CS_capita_adjusted_pc, u_CS_aggregate_pc, u_CS_aggregate_adjusted_pc, u_pil_pc, u_pih_pc, u_pi_aggregate_pc, u_welfare_aggregate_pc, u_welfare_aggregate_adjusted_pc=d_simulate_model(al, ah, kl, kh, T, t, P, N, model = 'pc', auction='uniform')
            
            #Append tt
            u_temp_El_lst_tt.append(u_El_tt)
            u_temp_Eh_lst_tt.append(u_Eh_tt)
            u_temp_E_lst_tt.append(u_E_tt)
            u_temp_CS_aggregate_adjusted_lst_tt.append(u_CS_aggregate_adjusted_tt)
            u_temp_pil_lst_tt.append(u_pil_tt)
            u_temp_pih_lst_tt.append(u_pih_tt)
            u_temp_pi_aggregate_lst_tt.append(u_pi_aggregate_tt)
            u_temp_welfare_aggregate_adjusted_lst_tt.append(u_welfare_aggregate_adjusted_tt)
            
            #Append pc
            u_temp_El_lst_pc.append(u_El_pc)
            u_temp_Eh_lst_pc.append(u_Eh_pc)
            u_temp_E_lst_pc.append(u_E_pc)
            u_temp_CS_aggregate_adjusted_lst_pc.append(u_CS_aggregate_adjusted_pc)
            u_temp_pil_lst_pc.append(u_pil_pc)
            u_temp_pih_lst_pc.append(u_pih_pc)
            u_temp_pi_aggregate_lst_pc.append(u_pi_aggregate_pc)
            u_temp_welfare_aggregate_adjusted_lst_pc.append(u_welfare_aggregate_adjusted_pc)
            
        #Append lst_tt
        u_El_lst_tt.append(u_temp_El_lst_tt)
        u_Eh_lst_tt.append(u_temp_Eh_lst_tt)
        u_E_lst_tt.append(u_temp_E_lst_tt)
        u_CS_aggregate_adjusted_lst_tt.append(u_temp_CS_aggregate_adjusted_lst_tt)
        u_pil_lst_tt.append(u_temp_pil_lst_tt)
        u_pih_lst_tt.append(u_temp_pih_lst_tt)
        u_pi_aggregate_lst_tt.append(u_temp_pi_aggregate_lst_tt)
        u_welfare_aggregate_adjusted_lst_tt.append(u_temp_welfare_aggregate_adjusted_lst_tt)
        
        #Append lst_pc
        u_El_lst_pc.append(u_temp_El_lst_pc)
        u_Eh_lst_pc.append(u_temp_Eh_lst_pc)
        u_E_lst_pc.append(u_temp_E_lst_pc)
        u_CS_aggregate_adjusted_lst_pc.append(u_temp_CS_aggregate_adjusted_lst_pc)
        u_pil_lst_pc.append(u_temp_pil_lst_pc)
        u_pih_lst_pc.append(u_temp_pih_lst_pc)
        u_pi_aggregate_lst_pc.append(u_temp_pi_aggregate_lst_pc)
        u_welfare_aggregate_adjusted_lst_pc.append(u_temp_welfare_aggregate_adjusted_lst_pc)
   
    #Array tt
    u_El_array_tt = np.array(u_El_lst_tt)
    u_Eh_array_tt = np.array(u_Eh_lst_tt)
    u_E_array_tt = np.array(u_E_lst_tt)
    u_CS_aggregate_adjusted_array_tt = np.array(u_CS_aggregate_adjusted_lst_tt)
    u_pil_array_tt = np.array(u_pil_lst_tt)
    u_pih_array_tt = np.array(u_pih_lst_tt)
    u_pi_aggregate_array_tt = np.array(u_pi_aggregate_lst_tt)
    u_welfare_aggregate_adjusted_array_tt = np.array(u_welfare_aggregate_adjusted_lst_tt)
 
    #Array pc
    u_El_array_pc = np.array(u_El_lst_pc)
    u_Eh_array_pc = np.array(u_Eh_lst_pc)
    u_E_array_pc = np.array(u_E_lst_pc)
    u_CS_aggregate_adjusted_array_pc = np.array(u_CS_aggregate_adjusted_lst_pc)
    u_pil_array_pc = np.array(u_pil_lst_pc)
    u_pih_array_pc = np.array(u_pih_lst_pc)
    u_pi_aggregate_array_pc = np.array(u_pi_aggregate_lst_pc)
    u_welfare_aggregate_adjusted_array_pc = np.array(u_welfare_aggregate_adjusted_lst_pc)
  
    #Array diff
    u_El_diff = u_El_array_pc - u_El_array_tt
    u_Eh__diff = u_Eh_array_pc - u_Eh_array_tt
    u_E_diff = u_E_array_tt -u_E_array_pc
    #CS. Prior belief: CS_tt>CS_pc
    u_CS_aggregate_adjusted_diff = u_CS_aggregate_adjusted_array_tt - u_CS_aggregate_adjusted_array_pc
    u_pil_diff = u_pil_array_pc - u_pil_array_tt
    u_pih_diif = u_pih_array_pc - u_pih_array_tt
    #pi. Prior belief: pi_tt>pi_pc
    u_pi_aggregate_diff = u_pi_aggregate_array_tt - u_pi_aggregate_array_pc
    #welfare. Prior belief: welfare_tt>welfare_pc
    u_welfare_aggregate_adjusted_diff = u_welfare_aggregate_adjusted_array_tt - u_welfare_aggregate_adjusted_array_pc

    #Heat color E, CS_aggregate_adjusted,    
    u_vmin_E =  u_E_diff.min()
    u_vmax_E =  u_E_diff.max()
    fig, ax = plt.subplots(ncols = 4, figsize = (20, 9))
    u_c0 = ax[0].pcolormesh(u_al_lst, u_ah_lst, u_E_diff, cmap = 'viridis', vmin = u_vmin_E, vmax = u_vmax_E)
    ax[0].set_position([0.05+(0.85/4)*0, 0.15, 0.15, 0.7])
    ax[0].set(xticks=[1, 5, 10, 15, 19], xticklabels=['1', '5', '10', '15', '19'],
              yticks=[41, 50, 60, 70, 80, 90, 99], yticklabels=['41', '50', '60', '70', '80', '90', '99'])
    ax[0].set_ylabel('$\\theta_h$', fontsize=18)
    ax[0].set_xlabel('$\\theta_l$', fontsize=18)
    ax[0].set_title('price (tt-pc)', fontsize=20)
    cbar_ax = fig.add_axes([0.05+(0.15*1)+0.01, 0.15, 0.01, 0.7])
    fig.colorbar(u_c0, cax=cbar_ax)
    #CS_aggregate_adjusted
    u_vmin_CS =  u_CS_aggregate_adjusted_diff.min()
    u_vmax_CS =  u_CS_aggregate_adjusted_diff.max()
    u_c1 = ax[1].pcolormesh(u_al_lst, u_ah_lst, u_CS_aggregate_adjusted_diff, cmap = 'viridis', vmin = u_vmin_CS, vmax = u_vmax_CS)
    ax[1].set_position([0.05+(0.85/4)*1, 0.15, 0.15, 0.7])
    ax[1].set(xticks=[1, 5, 10, 15, 19], xticklabels=['1', '5', '10', '15', '19'],
              yticks=[41, 50, 60, 70, 80, 90, 99], yticklabels=['41', '50', '60', '70', '80', '90', '99'])
    ax[1].set_ylabel('$\\theta_h$', fontsize=18)
    ax[1].set_xlabel('$\\theta_l$', fontsize=18)
    ax[1].set_title('CS adjusted (tt-pc)', fontsize=20)
    cbar_ax = fig.add_axes([0.05+(0.85/4)*1+(0.15)+0.01, 0.15, 0.01, 0.7])
    fig.colorbar(u_c1, cax=cbar_ax)
    #pi
    u_vmin_pi =  u_pi_aggregate_diff.min()
    u_vmax_pi =  u_pi_aggregate_diff.max()
    u_c2 = ax[2].pcolormesh(u_al_lst, u_ah_lst, u_pi_aggregate_diff, cmap = 'viridis', vmin = u_vmin_pi, vmax = u_vmax_pi)
    ax[2].set_position([0.05+(0.85/4)*2, 0.15, 0.15, 0.7])
    ax[2].set(xticks=[1, 5, 10, 15, 19], xticklabels=['1', '5', '10', '15', '19'],
              yticks=[41, 50, 60, 70, 80, 90, 99], yticklabels=['41', '50', '60', '70', '80', '90', '99'])
    ax[2].set_ylabel('$\\theta_h$', fontsize=18)
    ax[2].set_xlabel('$\\theta_l$', fontsize=18)
    ax[2].set_title('profit (tt-pc)', fontsize=20)
    cbar_ax = fig.add_axes([0.05+(0.85/4)*2+(0.15)+0.01, 0.15, 0.01, 0.7])
    fig.colorbar(u_c2, cax=cbar_ax)
    #welfare_aggregate_adjusted
    u_vmin_w =  u_welfare_aggregate_adjusted_diff.min()
    u_vmax_w =  u_welfare_aggregate_adjusted_diff.max()
    u_c3 = ax[3].pcolormesh(u_al_lst, u_ah_lst, u_welfare_aggregate_adjusted_diff, cmap = 'viridis', vmin = u_vmin_w, vmax = u_vmax_w)
    ax[3].set_position([0.05+(0.85/4)*3, 0.15, 0.15, 0.7])
    ax[3].set(xticks=[1, 5, 10, 15, 19], xticklabels=['1', '5', '10', '15', '19'],
              yticks=[41, 50, 60, 70, 80, 90, 99], yticklabels=['41', '50', '60', '70', '80', '90', '99'])
    ax[3].set_ylabel('$\\theta_h$', fontsize=18)
    ax[3].set_xlabel('$\\theta_l$', fontsize=18)
    ax[3].set_title('welfare adjusted (tt-pc)', fontsize=20)
    cbar_ax = fig.add_axes([0.05+(0.85/4)*3+(0.15)+0.01, 0.15, 0.01, 0.7])
    fig.colorbar(u_c3, cax=cbar_ax)
    plt.show()
    
    ####################################################
    ### Dsicriminatory vs uniform price auction (tt) ###
    ####################################################
    
    #Array diff discriminatory tt - uniform tt
    du_El_diff = u_El_array_tt - El_array_tt
    du_Eh__diff = u_Eh_array_tt - Eh_array_tt
    du_E_diff = u_E_array_tt - E_array_tt
    #CS. Prior belief: CS_tt>CS_pc
    du_CS_aggregate_adjusted_diff = u_CS_aggregate_adjusted_array_tt - CS_aggregate_adjusted_array_tt
    du_pil_diff = u_pil_array_tt - pil_array_tt
    du_pih_diff = u_pih_array_tt - u_pih_array_tt
    #pi. Prior belief: pi_tt>pi_pc
    du_pi_aggregate_diff = u_pi_aggregate_array_tt - pi_aggregate_array_tt
    #welfare. Prior belief: welfare_tt>welfare_pc
    du_welfare_aggregate_adjusted_diff = u_welfare_aggregate_adjusted_array_tt - welfare_aggregate_adjusted_array_tt

    
    #Heat color E, CS_aggregate_adjusted, profits, welfare_adjusted
    import matplotlib.pyplot as plt
    du_vmin_E =  du_E_diff.min()
    du_vmax_E =  du_E_diff.max()
    fig, ax = plt.subplots(ncols = 4, figsize = (20, 9))
    du_c0 = ax[0].pcolormesh(al_lst, ah_lst, du_E_diff, cmap = 'viridis', vmin = du_vmin_E, vmax = du_vmax_E)
    ax[0].set_position([0.05+(0.85/4)*0, 0.15, 0.15, 0.7])
    ax[0].set(xticks=[1, 5, 10, 15, 19], xticklabels=['1', '5', '10', '15', '19'],
              yticks=[41, 50, 60, 70, 80, 90, 99], yticklabels=['41', '50', '60', '70', '80', '90', '99'])
    ax[0].set_ylabel('$\\theta_h$', fontsize=18)
    ax[0].set_xlabel('$\\theta_l$', fontsize=18)
    ax[0].set_title('price (u-d)(tt)', fontsize=20)
    cbar_ax = fig.add_axes([0.05+(0.15*1)+0.01, 0.15, 0.01, 0.7])
    fig.colorbar(du_c0, cax=cbar_ax)
    #CS_aggregate_adjusted
    du_vmin_CS =  du_CS_aggregate_adjusted_diff.min()
    du_vmax_CS =  du_CS_aggregate_adjusted_diff.max()
    du_c1 = ax[1].pcolormesh(al_lst, ah_lst, du_CS_aggregate_adjusted_diff, cmap = 'viridis', vmin = du_vmin_CS, vmax = du_vmax_CS)
    ax[1].set_position([0.05+(0.85/4)*1, 0.15, 0.15, 0.7])
    ax[1].set(xticks=[1, 5, 10, 15, 19], xticklabels=['1', '5', '10', '15', '19'],
              yticks=[41, 50, 60, 70, 80, 90, 99], yticklabels=['41', '50', '60', '70', '80', '90', '99'])
    ax[1].set_ylabel('$\\theta_h$', fontsize=18)
    ax[1].set_xlabel('$\\theta_l$', fontsize=18)
    ax[1].set_title('CS adjusted (u-d)(tt)', fontsize=20)
    cbar_ax = fig.add_axes([0.05+(0.85/4)*1+(0.15)+0.01, 0.15, 0.01, 0.7])
    fig.colorbar(du_c1, cax=cbar_ax)
    #pi
    du_vmin_pi =  du_pi_aggregate_diff.min()
    du_vmax_pi =  du_pi_aggregate_diff.max()
    du_c2 = ax[2].pcolormesh(al_lst, ah_lst, du_pi_aggregate_diff, cmap = 'viridis', vmin = du_vmin_pi, vmax = du_vmax_pi)
    ax[2].set_position([0.05+(0.85/4)*2, 0.15, 0.15, 0.7])
    ax[2].set(xticks=[1, 5, 10, 15, 19], xticklabels=['1', '5', '10', '15', '19'],
              yticks=[41, 50, 60, 70, 80, 90, 99], yticklabels=['41', '50', '60', '70', '80', '90', '99'])
    ax[2].set_ylabel('$\\theta_h$', fontsize=18)
    ax[2].set_xlabel('$\\theta_l$', fontsize=18)
    ax[2].set_title('profit (u-d)(tt)', fontsize=20)
    cbar_ax = fig.add_axes([0.05+(0.85/4)*2+(0.15)+0.01, 0.15, 0.01, 0.7])
    fig.colorbar(du_c2, cax=cbar_ax)
    #welfare_aggregate_adjusted
    du_vmin_w =  du_welfare_aggregate_adjusted_diff.min()
    du_vmax_w =  du_welfare_aggregate_adjusted_diff.max()
    du_c3 = ax[3].pcolormesh(al_lst, ah_lst, du_welfare_aggregate_adjusted_diff, cmap = 'viridis', vmin = du_vmin_w, vmax = du_vmax_w)
    ax[3].set_position([0.05+(0.85/4)*3, 0.15, 0.15, 0.7])
    ax[3].set(xticks=[1, 5, 10, 15, 19], xticklabels=['1', '5', '10', '15', '19'],
              yticks=[41, 50, 60, 70, 80, 90, 99], yticklabels=['41', '50', '60', '70', '80', '90', '99'])
    ax[3].set_ylabel('$\\theta_h$', fontsize=18)
    ax[3].set_xlabel('$\\theta_l$', fontsize=18)
    ax[3].set_title('welfare adjusted (u-d)(tt)', fontsize=20)
    cbar_ax = fig.add_axes([0.05+(0.85/4)*3+(0.15)+0.01, 0.15, 0.01, 0.7])
    fig.colorbar(du_c3, cax=cbar_ax)
    plt.show()
    
    ####################################################
    ### Dsicriminatory vs uniform price auction (pc) ###
    ####################################################
    
    #Array diff discriminatory tt - uniform tt
    du_El_diff_pc = u_El_array_pc - El_array_pc
    du_Eh__diff_pc = u_Eh_array_pc - Eh_array_pc
    du_E_diff_pc = u_E_array_pc - E_array_pc
    #CS. Prior belief: CS_tt>CS_pc
    du_CS_aggregate_adjusted_diff_pc = u_CS_aggregate_adjusted_array_pc - CS_aggregate_adjusted_array_pc
    du_pil_diff_pc = u_pil_array_pc - pil_array_pc
    du_pih_diff_pc = u_pih_array_pc - u_pih_array_pc
    #pi. Prior belief: pi_tt>pi_pc
    du_pi_aggregate_diff_pc = u_pi_aggregate_array_pc - pi_aggregate_array_pc
    #welfare. Prior belief: welfare_tt>welfare_pc
    du_welfare_aggregate_adjusted_diff_pc = u_welfare_aggregate_adjusted_array_pc - welfare_aggregate_adjusted_array_pc

    
    #Heat color E, CS_aggregate_adjusted, profits, welfare_adjusted
    import matplotlib.pyplot as plt
    du_vmin_E_pc =  du_E_diff_pc.min()
    du_vmax_E_pc =  du_E_diff_pc.max()
    fig, ax = plt.subplots(ncols = 4, figsize = (20, 9))
    du_c0_pc = ax[0].pcolormesh(al_lst, ah_lst, du_E_diff_pc, cmap = 'viridis', vmin = du_vmin_E_pc, vmax = du_vmax_E_pc)
    ax[0].set_position([0.05+(0.85/4)*0, 0.15, 0.15, 0.7])
    ax[0].set(xticks=[1, 5, 10, 15, 19], xticklabels=['1', '5', '10', '15', '19'],
              yticks=[41, 50, 60, 70, 80, 90, 99], yticklabels=['41', '50', '60', '70', '80', '90', '99'])
    ax[0].set_ylabel('$\\theta_h$', fontsize=18)
    ax[0].set_xlabel('$\\theta_l$', fontsize=18)
    ax[0].set_title('price (u-d)(pc)', fontsize=20)
    cbar_ax = fig.add_axes([0.05+(0.15*1)+0.01, 0.15, 0.01, 0.7])
    fig.colorbar(du_c0_pc, cax=cbar_ax)
    #CS_aggregate_adjusted
    du_vmin_CS_pc =  du_CS_aggregate_adjusted_diff_pc.min()
    du_vmax_CS_pc =  du_CS_aggregate_adjusted_diff_pc.max()
    du_c1_pc = ax[1].pcolormesh(al_lst, ah_lst, du_CS_aggregate_adjusted_diff_pc, cmap = 'viridis', vmin = du_vmin_CS_pc, vmax = du_vmax_CS_pc)
    ax[1].set_position([0.05+(0.85/4)*1, 0.15, 0.15, 0.7])
    ax[1].set(xticks=[1, 5, 10, 15, 19], xticklabels=['1', '5', '10', '15', '19'],
              yticks=[41, 50, 60, 70, 80, 90, 99], yticklabels=['41', '50', '60', '70', '80', '90', '99'])
    ax[1].set_ylabel('$\\theta_h$', fontsize=18)
    ax[1].set_xlabel('$\\theta_l$', fontsize=18)
    ax[1].set_title('CS adjusted (u-d)(pc)', fontsize=20)
    cbar_ax = fig.add_axes([0.05+(0.85/4)*1+(0.15)+0.01, 0.15, 0.01, 0.7])
    fig.colorbar(du_c1_pc, cax=cbar_ax)
    #pi
    du_vmin_pi_pc =  du_pi_aggregate_diff_pc.min()
    du_vmax_pi_pc =  du_pi_aggregate_diff_pc.max()
    du_c2_pc = ax[2].pcolormesh(al_lst, ah_lst, du_pi_aggregate_diff_pc, cmap = 'viridis', vmin = du_vmin_pi_pc, vmax = du_vmax_pi_pc)
    ax[2].set_position([0.05+(0.85/4)*2, 0.15, 0.15, 0.7])
    ax[2].set(xticks=[1, 5, 10, 15, 19], xticklabels=['1', '5', '10', '15', '19'],
              yticks=[41, 50, 60, 70, 80, 90, 99], yticklabels=['41', '50', '60', '70', '80', '90', '99'])
    ax[2].set_ylabel('$\\theta_h$', fontsize=18)
    ax[2].set_xlabel('$\\theta_l$', fontsize=18)
    ax[2].set_title('profit (u-d)(pc)', fontsize=20)
    cbar_ax = fig.add_axes([0.05+(0.85/4)*2+(0.15)+0.01, 0.15, 0.01, 0.7])
    fig.colorbar(du_c2_pc, cax=cbar_ax)
    #welfare_aggregate_adjusted
    du_vmin_w_pc =  du_welfare_aggregate_adjusted_diff_pc.min()
    du_vmax_w_pc =  du_welfare_aggregate_adjusted_diff_pc.max()
    du_c3_pc = ax[3].pcolormesh(al_lst, ah_lst, du_welfare_aggregate_adjusted_diff_pc, cmap = 'viridis', vmin = du_vmin_w_pc, vmax = du_vmax_w_pc)
    ax[3].set_position([0.05+(0.85/4)*3, 0.15, 0.15, 0.7])
    ax[3].set(xticks=[1, 5, 10, 15, 19], xticklabels=['1', '5', '10', '15', '19'],
              yticks=[41, 50, 60, 70, 80, 90, 99], yticklabels=['41', '50', '60', '70', '80', '90', '99'])
    ax[3].set_ylabel('$\\theta_h$', fontsize=18)
    ax[3].set_xlabel('$\\theta_l$', fontsize=18)
    ax[3].set_title('welfare adjusted (u-d)(pc)', fontsize=20)
    cbar_ax = fig.add_axes([0.05+(0.85/4)*3+(0.15)+0.01, 0.15, 0.01, 0.7])
    fig.colorbar(du_c3_pc, cax=cbar_ax)
    plt.show()


