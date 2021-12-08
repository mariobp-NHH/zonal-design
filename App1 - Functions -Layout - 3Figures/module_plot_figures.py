# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 10:51:20 2021

@author: s14761
"""
import plotly.graph_objects as go
colors= {
    "c": "rgb(38, 70, 83)", #"charcoal"
    "p-g": "rgb(42, 157, 143)", #"persian-green"
    "o-y-c": "rgb(233, 196, 106)", #"orange-yellow-crayola"
    "s-b": "rgb(244, 162, 97)", #"sandy-brown"
    "b-s": "rgb(231, 111, 81)" #"burnt-sienna"
    }


def fig_area_function(al, ah):
    fig_area = go.Figure()
    fig_area.update_layout(title={
                    'text': "Equilibrium areas",
                    'y':0.9,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                    xaxis_title='demand low-node (al)',
                    yaxis_title='demand high-node (ah)')
    fig_area.update_yaxes(range=[40, 100])  
    fig_area.update_xaxes(range=[0, 20])
    fig_area.update_yaxes(tickvals=[41.1, 45.1, 50.1, 55.1, 59.1, 65, 70, 75, 80, 85, 90, 95, 99])
    fig_area.update_xaxes(tickangle=0, tickvals=[1, 5, 10, 15, 19, 60, 100])
    fig_area.update_yaxes(showgrid=False)
    fig_area.update_xaxes(showgrid=False)
        
    fig_area.add_trace(go.Scatter(
    x=[0, 20], y=[40, 40],
    showlegend=False,
    fill=None,
    mode='lines',
    line=dict(width=0.5, color=colors["c"]),))
    fig_area.add_trace(go.Scatter(
    x=[0, 20], y=[60, 40],
    showlegend=False,
    fill='tonexty',
    mode='lines',
    line=dict(width=0.5, color=colors["c"]),))
    fig_area.add_trace(go.Scatter(
    x=[0, 20], y=[100, 100],
    showlegend=False,
    fill='tonexty',
    mode='lines',
    line=dict(width=0.5, color=colors["p-g"]),))
    
    fig_area.add_trace(go.Scatter(x=[0, al], y=[ah, ah], mode= 'lines', showlegend=False,
                    line=dict(width=1, color='rgb(0, 0, 0)', dash='dash')))
    fig_area.add_trace(go.Scatter(x=[al, al], y=[0, ah], mode= 'lines', showlegend=False,
                    line=dict(width=1, color='rgb(0, 0, 0)', dash='dash')))
    fig_area.add_scatter(x=[al],y=[ah], mode="markers", showlegend=False,
                marker=dict(size=10, color=colors["s-b"]))
    
    return fig_area

def fig_strategies(Fh_tt, Fl_tt, p_tt, Fh_pc, Fl_pc, p_pc, Eh_tt, El_tt, E_tt, Eh_pc, El_pc, E_pc):
    #Fig 1: Discriminatory, ex-ante (strategies)
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=p_tt, y=Fh_tt,
                        mode='lines',
                        name='Fh (tt)',
                        line = dict(color=colors["c"], width=1.5)))
    fig1.add_trace(go.Scatter(x=p_tt, y=Fl_tt,
                        mode='lines',
                        name='Fl (tt)',
                        line = dict(color=colors["p-g"], width=1.5)))
    fig1.add_trace(go.Scatter(x=[Eh_tt,Eh_tt], y=[0,1],
                        mode='lines',
                        name='Eh (tt)',
                        line = dict(color=colors["o-y-c"], width=1.5)))
    fig1.add_trace(go.Scatter(x=[El_tt,El_tt], y=[0,1],
                        mode='lines',
                        name='El (tt)',
                        line = dict(color=colors["s-b"], width=1.5)))
    fig1.add_trace(go.Scatter(x=[E_tt,E_tt], y=[0,1],
                        mode='lines',
                        name='E (tt)',
                        line = dict(color=colors["b-s"], width=1.5)))
    fig1.update_layout(title={
                    'text': "Discriminatory, tt (strategies)",
                    'y':0.9,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                    xaxis_title='Price',
                    yaxis_title='CDF')
    fig1.update_yaxes(range=[0, 1.1])  
    fig1.update_xaxes(range=[0, 7.1]) 
    fig1.update_xaxes(tickangle=0, tickvals=[0, 1, 2, 3, 4, 5, 6, 7])
    
    #Fig 2: Discriminatory, ex-ante \ ex-post (strategies)
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=p_tt, y=Fh_tt,
                        mode='lines',
                        name='Fh (tt)',
                        opacity=.2,
                        line = dict(color=colors["c"], width=1.5)))
    fig2.add_trace(go.Scatter(x=p_tt, y=Fl_tt,
                        mode='lines',
                        name='Fl (tt)',
                        opacity=.2,
                        line = dict(color=colors["p-g"], width=1.5)))
    fig2.add_trace(go.Scatter(x=[Eh_tt,Eh_tt], y=[0,1],
                        mode='lines',
                        name='Eh (tt)',
                        opacity=.2,
                        line = dict(color=colors["o-y-c"], width=1.5)))
    fig2.add_trace(go.Scatter(x=[El_tt,El_tt], y=[0,1],
                        mode='lines',
                        name='El (tt)',
                        opacity=.2,
                        line = dict(color=colors["s-b"], width=1.5)))
    fig2.add_trace(go.Scatter(x=[E_tt,E_tt], y=[0,1],
                        mode='lines',
                        opacity=.2,
                        name='E (tt)',
                        line = dict(color=colors["b-s"], width=1.5)))
    fig2.add_trace(go.Scatter(x=p_pc, y=Fh_pc,
                        mode='lines',
                        name='Fh (pc)',
                        line = dict(color=colors["c"], width=1.5)))
    fig2.add_trace(go.Scatter(x=p_pc, y=Fl_pc,
                        mode='lines',
                        name='Fl (pc)',
                        line = dict(color=colors["p-g"], width=1.5)))
    fig2.add_trace(go.Scatter(x=[Eh_pc,Eh_pc], y=[0,1],
                        mode='lines',
                        name='Eh (pc)',
                        line = dict(color=colors["o-y-c"], width=1.5)))
    fig2.add_trace(go.Scatter(x=[El_pc,El_pc], y=[0,1],
                        mode='lines',
                        name='El (pc)',
                        line = dict(color=colors["s-b"], width=1.5)))
    fig2.add_trace(go.Scatter(x=[E_pc,E_pc], y=[0,1],
                        mode='lines',
                        name='E (pc)',
                        line = dict(color=colors["b-s"], width=1.5)))
    fig2.update_layout(title={
                    'text': "Discriminatory, tt \ pc (strategies)",
                    'y':0.9,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                    xaxis_title='Price',
                    yaxis_title='CDF')
    fig2.update_yaxes(range=[0, 1.1])  
    fig2.update_xaxes(range=[0, 7.1]) 
    fig2.update_xaxes(tickangle=0, tickvals=[0, 1, 2, 3, 4, 5, 6, 7])
    
    #Fig 3: Discriminatory, ex-post (strategies)
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=p_pc, y=Fh_pc,
                        mode='lines',
                        name='Fh (pc)',
                        line = dict(color=colors["c"], width=1.5)))
    fig3.add_trace(go.Scatter(x=p_pc, y=Fl_pc,
                        mode='lines',
                        name='Fl (pc)',
                        line = dict(color=colors["p-g"], width=1.5)))
    fig3.add_trace(go.Scatter(x=[Eh_pc,Eh_pc], y=[0,1],
                        mode='lines',
                        name='Eh (pc)',
                        line = dict(color=colors["o-y-c"], width=1.5)))
    fig3.add_trace(go.Scatter(x=[El_pc,El_pc], y=[0,1],
                        mode='lines',
                        name='El (pc)',
                        line = dict(color=colors["s-b"], width=1.5)))
    fig3.add_trace(go.Scatter(x=[E_pc,E_pc], y=[0,1],
                        mode='lines',
                        name='E (pc)',
                        line = dict(color=colors["b-s"], width=1.5)))
    fig3.update_layout(title={
                    'text': "Discriminatory, pc (strategies)",
                    'y':0.9,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                    xaxis_title='Price',
                    yaxis_title='CDF')
    fig3.update_yaxes(range=[0, 1.1])  
    fig3.update_xaxes(range=[0, 7.1]) 
    fig3.update_xaxes(tickangle=0, tickvals=[0, 1, 2, 3, 4, 5, 6, 7])
    
    return fig1, fig2, fig3
 

def fig_prices(ah, ah_lst_tt, Eh_lst_tt, El_lst_tt, E_lst_tt, ah_lst_pc, Eh_lst_pc, El_lst_pc, E_lst_pc):
        #Fig 1: Discriminatory, ex-ante (prices)
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=ah_lst_tt, y=Eh_lst_tt,
                            mode='lines',
                            name='Eh (tt)',
                            line = dict(color=colors["c"], width=1.5)))
        fig1.add_trace(go.Scatter(x=ah_lst_tt, y=El_lst_tt,
                            mode='lines',
                            name='El (tt)',
                            line = dict(color=colors["p-g"], width=1.5)))
        fig1.add_trace(go.Scatter(x=ah_lst_tt, y=E_lst_tt,
                            mode='lines',
                            name='E (tt)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig1.add_trace(go.Scatter(x=[ah,ah], y=[0,7],
                            mode='lines',
                            name='ah',
                            line = dict(color=colors["s-b"], width=1.5)))
        fig1.update_layout(title={
                        'text': "Discriminatory, tt (prices)",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='Price')
        fig1.update_yaxes(range=[0, 7])  
        fig1.update_xaxes(range=[40, 101]) 
        fig1.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
        
        #Fig 2: Discriminatory, ex-ante \ ex-post (prices)
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=ah_lst_tt, y=Eh_lst_tt,
                            mode='lines',
                            name='Eh (tt)',
                            opacity=.2,
                            line = dict(color=colors["c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_tt, y=El_lst_tt,
                            mode='lines',
                            name='El (tt)',
                            opacity=.2,
                            line = dict(color=colors["p-g"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_tt, y=E_lst_tt,
                            mode='lines',
                            opacity=.2,
                            name='E (tt)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_pc, y=Eh_lst_pc,
                            mode='lines',
                            name='Eh (pc)',
                            line = dict(color=colors["c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_pc, y=El_lst_pc,
                            mode='lines',
                            name='El (pc)',
                            line = dict(color=colors["p-g"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_pc, y=E_lst_pc,
                            mode='lines',
                            name='E (pc)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=[ah,ah], y=[0,7],
                            mode='lines',
                            name='ah',
                            opacity=1,
                            line = dict(color=colors["s-b"], width=1.5)))
        fig2.update_layout(title={
                        'text': "Discriminatory, tt \ pc (prices)",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='Price')
        fig2.update_yaxes(range=[0, 7])  
        fig2.update_xaxes(range=[40, 101]) 
        fig2.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
        
        #Fig 3: : Discriminatory, ex-post (prices)
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=ah_lst_pc, y=Eh_lst_pc,
                            mode='lines',
                            name='Eh (pc)',
                            line = dict(color=colors["c"], width=1.5)))
        fig3.add_trace(go.Scatter(x=ah_lst_pc, y=El_lst_pc,
                            mode='lines',
                            name='El (pc)',
                            line = dict(color=colors["p-g"], width=1.5)))
        fig3.add_trace(go.Scatter(x=ah_lst_pc, y=E_lst_pc,
                            mode='lines',
                            name='E (pc)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig3.add_trace(go.Scatter(x=[ah,ah], y=[0,7],
                            mode='lines',
                            name='ah',
                            line = dict(color=colors["s-b"], width=1.5)))
        fig3.update_layout(title={
                        'text': "Discriminatory, pc (prices)",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='Price')
        fig3.update_yaxes(range=[0, 7])  
        fig3.update_xaxes(range=[40, 101]) 
        fig3.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
        
        return fig1, fig2, fig3
     
def fig_cs_capita(ah, ah_lst_tt, CS_capita_lst_tt, CS_capita_adjusted_lst_tt, ah_lst_pc, CS_capita_lst_pc, CS_capita_adjusted_lst_pc):
        #Fig 1: Discriminatory, ex-ante (CS capita)
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=ah_lst_tt, y=CS_capita_lst_tt,
                            mode='lines',
                            name='CS (tt)',
                            line = dict(color=colors["c"], width=1.5)))
        fig1.add_trace(go.Scatter(x=[ah,ah], y=[0,7],
                            mode='lines',
                            name='ah',
                            line = dict(color=colors["s-b"], width=1.5)))
        fig1.update_layout(title={
                        'text': "Discriminatory, tt (CS capita)",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='CS (capita)')
        fig1.update_yaxes(range=[0, 7])  
        fig1.update_xaxes(range=[40, 101]) 
        fig1.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
        
        #Fig 2: Discriminatory, ex-ante \ ex-post (CS capita)
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=ah_lst_tt, y=CS_capita_lst_tt,
                            mode='lines',
                            opacity=.2,
                            name='CS (tt)',
                            line = dict(color=colors["c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_pc, y=CS_capita_lst_pc,
                            mode='lines',
                            opacity=1,
                            name='CS (pc)',
                            line = dict(color=colors["c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_tt, y=CS_capita_adjusted_lst_tt,
                            mode='lines',
                            opacity=0.2,
                            name='CS ad (tt)',
                            line = dict(color=colors["b-s"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_pc, y=CS_capita_adjusted_lst_pc,
                            mode='lines',
                            opacity=1,
                            name='CS ad (tt)',
                            line = dict(color=colors["b-s"], width=1.5)))
        fig2.add_trace(go.Scatter(x=[ah,ah], y=[0,7],
                            mode='lines',
                            name='ah',
                            opacity=1,
                            line = dict(color=colors["s-b"], width=1.5)))
        fig2.update_layout(title={
                        'text': "Discriminatory, tt \ pc (CS capita)",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='CS (capita)')
        fig2.update_yaxes(range=[0, 7])  
        fig2.update_xaxes(range=[40, 101]) 
        fig2.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
        
        #Fig 3: : Discriminatory, ex-post (CS capita)
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=ah_lst_pc, y=CS_capita_lst_pc,
                            mode='lines',
                            opacity=1,
                            name='CS (pc)',
                            line = dict(color=colors["c"], width=1.5)))
        fig3.add_trace(go.Scatter(x=ah_lst_pc, y=CS_capita_adjusted_lst_pc,
                            mode='lines',
                            opacity=1,
                            name='CS ad (pc)',
                            line = dict(color=colors["b-s"], width=1.5)))
        fig3.add_trace(go.Scatter(x=[ah,ah], y=[0,7],
                            mode='lines',
                            name='ah',
                            line = dict(color=colors["s-b"], width=1.5)))
        fig3.update_layout(title={
                        'text': "Discriminatory, pc (CS capita)",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='CS (capita)')
        fig3.update_yaxes(range=[0, 7])  
        fig3.update_xaxes(range=[40, 101]) 
        fig3.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
        
        return fig1, fig2, fig3

def fig_profits(ah, ah_lst_tt, pil_lst_tt, pih_lst_tt, pi_aggregate_lst_tt, ah_lst_pc, pil_lst_pc, pih_lst_pc, pi_aggregate_lst_pc):
    #Fig 1: Discriminatory, ex-ante (profits)
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=ah_lst_tt, y=pil_lst_tt,
                            mode='lines',
                            name='pil (tt)',
                            line = dict(color=colors["p-g"], width=1.5)))
        fig1.add_trace(go.Scatter(x=ah_lst_tt, y=pih_lst_tt,
                            mode='lines',
                            name='pih (tt)',
                            line = dict(color=colors["c"], width=1.5)))
        fig1.add_trace(go.Scatter(x=ah_lst_tt, y=pi_aggregate_lst_tt,
                            mode='lines',
                            name='pi (tt)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig1.add_trace(go.Scatter(x=[ah,ah], y=[0,500],
                            mode='lines',
                            name='ah',
                            line = dict(color=colors["s-b"], width=1.5)))
        fig1.update_layout(title={
                        'text': "Discriminatory, tt (profits)",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='Profit')
        fig1.update_yaxes(range=[0, 500])  
        fig1.update_xaxes(range=[40, 101]) 
        fig1.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
        
        #Fig 2: Discriminatory, ex-ante \ ex-post (profits)
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=ah_lst_tt, y=pil_lst_tt,
                            mode='lines',
                            opacity=0.2,
                            name='pil (tt)',
                            line = dict(color=colors["p-g"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_tt, y=pih_lst_tt,
                            mode='lines',
                            opacity=0.2,
                            name='pih (tt)',
                            line = dict(color=colors["c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_tt, y=pi_aggregate_lst_tt,
                            mode='lines',
                            opacity=0.2,
                            name='pi (tt)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_pc, y=pil_lst_pc,
                            mode='lines',
                            name='pil (pc)',
                            line = dict(color=colors["p-g"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_pc, y=pih_lst_pc,
                            mode='lines',
                            name='pih (pc)',
                            line = dict(color=colors["c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_pc, y=pi_aggregate_lst_pc,
                            mode='lines',
                            name='pi (pc)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=[ah,ah], y=[0,500],
                            mode='lines',
                            name='ah',
                            opacity=1,
                            line = dict(color=colors["s-b"], width=1.5)))
        fig2.update_layout(title={
                        'text': "Discriminatory, tt \ pc (profits)",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='Profit')
        fig2.update_yaxes(range=[0, 500])  
        fig2.update_xaxes(range=[40, 101]) 
        fig2.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
        
        #Fig 3: : Discriminatory, ex-post (profits)
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=ah_lst_pc, y=pil_lst_pc,
                            mode='lines',
                            name='pil (pc)',
                            line = dict(color=colors["p-g"], width=1.5)))
        fig3.add_trace(go.Scatter(x=ah_lst_pc, y=pih_lst_pc,
                            mode='lines',
                            name='pih (pc)',
                            line = dict(color=colors["c"], width=1.5)))
        fig3.add_trace(go.Scatter(x=ah_lst_pc, y=pi_aggregate_lst_pc,
                            mode='lines',
                            name='pi (pc)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig3.add_trace(go.Scatter(x=[ah,ah], y=[0,500],
                            mode='lines',
                            name='ah',
                            line = dict(color=colors["s-b"], width=1.5)))
        fig3.update_layout(title={
                        'text': "Discriminatory, pc (profits)",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='Profit')
        fig3.update_yaxes(range=[0, 500])  
        fig3.update_xaxes(range=[40, 101]) 
        fig3.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
        
        return fig1, fig2, fig3
    
def fig_welfare(ah, ah_lst_tt, CS_aggregate_lst_tt, CS_aggregate_adjusted_lst_tt, pi_aggregate_lst_tt, welfare_aggregate_lst_tt, welfare_aggregate_adjusted_lst_tt, ah_lst_pc, CS_aggregate_lst_pc, CS_aggregate_adjusted_lst_pc, pi_aggregate_lst_pc, welfare_aggregate_lst_pc, welfare_aggregate_adjusted_lst_pc):
        #Fig 1: Discriminatory, ex-ante (welfare)
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=ah_lst_tt, y=CS_aggregate_lst_tt,
                            mode='lines',
                            name='CS (tt)',
                            line = dict(color=colors["c"], width=1.5)))
        fig1.add_trace(go.Scatter(x=ah_lst_tt, y=pi_aggregate_lst_tt,
                            mode='lines',
                            name='pi (tt)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig1.add_trace(go.Scatter(x=ah_lst_tt, y=welfare_aggregate_lst_tt,
                            mode='lines',
                            name='W (tt)',
                            line = dict(color=colors["s-b"], width=1.5)))
        fig1.add_trace(go.Scatter(x=[ah,ah], y=[0,800],
                            mode='lines',
                            name='ah',
                            opacity=1,
                            line = dict(color=colors["s-b"], width=1.5, dash='dash')))
        fig1.update_layout(title={
                        'text': "Discriminatory, tt (welfare)",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='Welfate')
        fig1.update_yaxes(range=[0, 800])  
        fig1.update_xaxes(range=[40, 101]) 
        fig1.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
        
        #Fig 2: Discriminatory, ex-ante \ ex-post (welfare)
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=ah_lst_tt, y=CS_aggregate_lst_tt,
                            mode='lines',
                            opacity=0.2,
                            name='CS (tt)',
                            line = dict(color=colors["c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_tt, y=pi_aggregate_lst_tt,
                            mode='lines',
                            opacity=0.2,
                            name='pi (tt)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_tt, y=welfare_aggregate_lst_tt,
                            mode='lines',
                            opacity=0.2,
                            name='W (tt)',
                            line = dict(color=colors["s-b"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_pc, y=CS_aggregate_lst_pc,
                            mode='lines',
                            opacity=1,
                            name='CS (pc)',
                            line = dict(color=colors["c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_pc, y=CS_aggregate_adjusted_lst_pc,
                            mode='lines',
                            opacity=1,
                            name='CS ad (pc)',
                            line = dict(color=colors["p-g"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_pc, y=pi_aggregate_lst_pc,
                            mode='lines',
                            opacity=1,
                            name='pi (pc)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_pc, y=welfare_aggregate_lst_pc,
                            mode='lines',
                            opacity=1,
                            name='W (pc)',
                            line = dict(color=colors["s-b"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_pc, y=welfare_aggregate_adjusted_lst_pc,
                            mode='lines',
                            opacity=1,
                            name='W ad (pc)',
                            line = dict(color=colors["b-s"], width=1.5)))
        fig2.add_trace(go.Scatter(x=[ah,ah], y=[0,800],
                            mode='lines',
                            opacity=1,
                            name='ah',
                            line = dict(color=colors["s-b"], width=1.5, dash='dash')))
        fig2.update_layout(title={
                        'text': "Discriminatory, tt / pc (welfare)",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='Welfate')
        fig2.update_yaxes(range=[0, 800])  
        fig2.update_xaxes(range=[40, 101]) 
        fig2.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
        
        #Fig 3: Discriminatory, ex-post (strategies)
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=ah_lst_pc, y=CS_aggregate_lst_pc,
                            mode='lines',
                            opacity=1,
                            name='CS (pc)',
                            line = dict(color=colors["c"], width=1.5)))
        fig3.add_trace(go.Scatter(x=ah_lst_pc, y=CS_aggregate_adjusted_lst_pc,
                            mode='lines',
                            opacity=1,
                            name='CS ad (pc)',
                            line = dict(color=colors["p-g"], width=1.5)))
        fig3.add_trace(go.Scatter(x=ah_lst_pc, y=pi_aggregate_lst_pc,
                            mode='lines',
                            opacity=1,
                            name='pi (pc)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig3.add_trace(go.Scatter(x=ah_lst_pc, y=welfare_aggregate_lst_pc,
                            mode='lines',
                            opacity=1,
                            name='W (pc)',
                            line = dict(color=colors["s-b"], width=1.5)))
        fig3.add_trace(go.Scatter(x=ah_lst_pc, y=welfare_aggregate_adjusted_lst_pc,
                            mode='lines',
                            opacity=1,
                            name='W ad (pc)',
                            line = dict(color=colors["b-s"], width=1.5)))
        fig3.add_trace(go.Scatter(x=[ah,ah], y=[0,800],
                            mode='lines',
                            opacity=1,
                            name='ah',
                            line = dict(color=colors["s-b"], width=1.5, dash='dash')))
        fig3.update_layout(title={
                        'text': "Discriminatory, pc (welfare)",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='Welfate')
        fig3.update_yaxes(range=[0, 800])  
        fig3.update_xaxes(range=[40, 101]) 
        fig3.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
       
        return fig1, fig2, fig3
    
