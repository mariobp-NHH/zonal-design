# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 21:07:31 2021

@author: s14761
"""


import numpy as np
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import module_discriminatory_v1 as dis
import module_plot_figures as pf

colors= {
    "c": "rgb(38, 70, 83)", #"charcoal"
    "p-g": "rgb(42, 157, 143)", #"persian-green"
    "o-y-c": "rgb(233, 196, 106)", #"orange-yellow-crayola"
    "s-b": "rgb(244, 162, 97)", #"sandy-brown"
    "b-s": "rgb(231, 111, 81)" #"burnt-sienna"
    }

app = dash.Dash(__name__)

app.layout = html.Div([
    
    html.Div([
        html.H2("Redispatch - Zonal Market App"),
        #html.Img(src="/assets/stock-icon.png")
        ],className = "banner"),
    
    html.Div([
        html.Div([
            
            html.Label('Demand low-node (al)'),
            dcc.Slider(id="al",
                min=1,
                max=19,
                step=None,
                marks={
                    1: '1',
                    5: '5',
                    10: '10',
                    15: '15',
                    19: '19',
                },
                value=5,
            ),
            
            
            html.Label('Demand high-node (ah)'),
            dcc.Slider(id="ah",
                min=41,
                max=99,
                step=None,
                marks={
                    41.1: '41.1',
                    45.1: '45.1',
                    50.1: '50.1',
                    55.1: '55.1',
                    59.1: '59.1',
                    65: '65',
                    70: '70',
                    75: '75',
                    80: '80',
                    85: '85',
                    90: '90',
                    95: '95',
                    99: '99',
                },
                value=41,
            ),
            
            html.Label('Tariff (t)'),
            dcc.Slider(id="t",
                min=0,
                max=2,
                step=None,
                marks={
                    0: '0',
                    0.25: '0.25',
                    0.5: '0.5',
                    0.75: '0.75',
                    1: '1',
                    1.25: '1.25',
                    1.5: '1.5',
                    1.75: '1.75',
                    2: '2',
                },
                value=0,
            ),
            
            html.Label('Plot'),
            dcc.RadioItems(id='plot',
                options=[
                    {'label': 'Strategies', 'value': 'strategies'},
                    {'label': 'Prices', 'value': 'prices'},
                    {'label': 'Consumer Surplus (per capita)', 'value': 'cs_capita'},
                    {'label': 'Profits', 'value': 'profits'},
                    {'label': 'Welfare (aggregate)', 'value': 'aggregate'}
                ],
                value='strategies',
                labelStyle={'display': 'inline-block'},
                className = "char-btn"
            ),
            
            
        ],className = "box_menu"),
        
        html.Div([   
            
            dcc.Graph(
                id="fig_area",
                figure = {}
            ),            
            
        ]),
        
    ],className = "wrapper"),    
    
    html.Div([
        html.Div([
           dcc.Graph(
                id="fig1",
                figure = {
                    "layout": {
                        "title": "Discriminatory, ex-ante (strategies)"                        
                    }                
                }
            ),
        ],className="four columns"),
        
        html.Div([
            dcc.Graph(
                id="fig2",
                figure = {
                    "layout": {
                        "title": "Discriminatory, ex-ante \ ex-post (strategies)"                        
                    }                
                }
            ),
        ],className="four columns"),
        
        html.Div([ 
            dcc.Graph(
                id="fig3",
                figure = {
                    "layout": {
                        "title": "Discriminatory, ex-post (strategies)"                        
                    }                
                }
            ),
        ],className="four columns"),
    ],className="row"),
        
   ])

def parameters(a, b, c, d):
    al = a
    ah = b
    plot = c
    t = d
    kl = 60
    kh = 60
    T = 40
    P = 7
    N = 100
    N2 = 400 #Points to work out the expected price for a given al
    return al, ah, plot, kl, kh, T, t, P, N, N2

def graph_in(al, ah, plot,
            Fh_tt, Fl_tt, p_tt,
            Fh_pc, Fl_pc, p_pc,
            Eh_tt, El_tt, E_tt,
            Eh_pc, El_pc, E_pc,
            ah_lst_tt, Eh_lst_tt, El_lst_tt, E_lst_tt, CS_capita_lst_tt, CS_capita_adjusted_lst_tt, CS_aggregate_lst_tt, CS_aggregate_adjusted_lst_tt, pil_lst_tt, pih_lst_tt, pi_aggregate_lst_tt, welfare_aggregate_lst_tt, welfare_aggregate_adjusted_lst_tt,
            ah_lst_pc, Eh_lst_pc, El_lst_pc, E_lst_pc, CS_capita_lst_pc, CS_capita_adjusted_lst_pc, CS_aggregate_lst_pc, CS_aggregate_adjusted_lst_pc, pil_lst_pc, pih_lst_pc, pi_aggregate_lst_pc, welfare_aggregate_lst_pc, welfare_aggregate_adjusted_lst_pc):
    #Fig area:
    fig_area = pf.fig_area_function(al, ah)
    

       
    if plot == 'strategies':
        fig1, fig2, fig3 = pf.fig_strategies(Fh_tt, Fl_tt, p_tt, Fh_pc, Fl_pc, p_pc, Eh_tt, El_tt, E_tt, Eh_pc, El_pc, E_pc)
    elif plot == 'prices':
        fig1, fig2, fig3 = pf.fig_prices(ah, ah_lst_tt, Eh_lst_tt, El_lst_tt, E_lst_tt, ah_lst_pc, Eh_lst_pc, El_lst_pc, E_lst_pc)
    elif plot == 'cs_capita':
        fig1, fig2, fig3 = pf.fig_cs_capita(ah, ah_lst_tt, CS_capita_lst_tt, CS_capita_adjusted_lst_tt, ah_lst_pc, CS_capita_lst_pc, CS_capita_adjusted_lst_pc)
    elif plot == 'profits':
        fig1, fig2, fig3 = pf.fig_profits(ah, ah_lst_tt, pil_lst_tt, pih_lst_tt, pi_aggregate_lst_tt, ah_lst_pc, pil_lst_pc, pih_lst_pc, pi_aggregate_lst_pc)
    else:
        fig1, fig2, fig3 = pf.fig_welfare(ah, ah_lst_tt, CS_aggregate_lst_tt, CS_aggregate_adjusted_lst_tt, pi_aggregate_lst_tt, welfare_aggregate_lst_tt, welfare_aggregate_adjusted_lst_tt, ah_lst_pc, CS_aggregate_lst_pc, CS_aggregate_adjusted_lst_pc, pi_aggregate_lst_pc, welfare_aggregate_lst_pc, welfare_aggregate_adjusted_lst_pc)  

    return fig_area, fig1, fig2, fig3


@app.callback(
    [
    Output('fig_area', 'figure'),
    Output("fig1", "figure"),   
    Output("fig2", "figure"),
    Output("fig3", "figure")   
    ],
    [ 
     Input('al', 'value'),
     Input('ah', 'value'),
     Input('plot', 'value'),
     Input('t', 'value')
      ]
    )


def update_graph(a_input, b_input, c_input, d_input):
    #Get parameters
    al, ah, plot, kl, kh, T, t, P, N, N2 = parameters(a_input, b_input, c_input, d_input)
    ##Call the functions
    #Determine the area
    area, area_num = dis.determine_area(al, ah)
    #d_strategies_tt
    Fh_tt, Fl_tt, p_tt, b1_tt, b2_tt = dis.d_strategies_tt(al, ah, kl, kh, T, t, P, N)   
    Eh_tt, El_tt, E_tt, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted=dis.d_welfare_tt(Fh_tt, Fl_tt, p_tt, al, ah, T, t, kl, kh, P)
    #d_strategies_pc
    Fh_pc, Fl_pc, p_pc, b1_pc, b2_pc = dis.d_strategies_pc(al, ah, kl, kh, T, t, P, N)   
    Eh_pc, El_pc, E_pc, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted=dis.d_welfare_pc(Fh_pc, Fl_pc, p_pc, al, ah, T, t, kl, kh, P)
    #Welfare tt
    ah_lst_tt, Eh_lst_tt, El_lst_tt, E_lst_tt, CS_capita_lst_tt, CS_capita_adjusted_lst_tt, CS_aggregate_lst_tt, CS_aggregate_adjusted_lst_tt, pil_lst_tt, pih_lst_tt, pi_aggregate_lst_tt, welfare_aggregate_lst_tt, welfare_aggregate_adjusted_lst_tt=dis.d_plot_welfare_tt(al, kl, kh, T, t, P, N, N2)
    #Welfare pc
    ah_lst_pc, Eh_lst_pc, El_lst_pc, E_lst_pc, CS_capita_lst_pc, CS_capita_adjusted_lst_pc, CS_aggregate_lst_pc, CS_aggregate_adjusted_lst_pc, pil_lst_pc, pih_lst_pc, pi_aggregate_lst_pc, welfare_aggregate_lst_pc, welfare_aggregate_adjusted_lst_pc=dis.d_plot_welfare_pc(al, kl, kh, T, t, P, N, N2)
    ##Update the graphs
    fig_area, fig1, fig2, fig3 = graph_in(al, ah, plot,
                                 Fh_tt, Fl_tt, p_tt,
                                 Fh_pc, Fl_pc, p_pc,
                                 Eh_tt, El_tt, E_tt,
                                 Eh_pc, El_pc, E_pc,
                                 ah_lst_tt, Eh_lst_tt, El_lst_tt, E_lst_tt, CS_capita_lst_tt, CS_capita_adjusted_lst_tt, CS_aggregate_lst_tt, CS_aggregate_adjusted_lst_tt, pil_lst_tt, pih_lst_tt, pi_aggregate_lst_tt, welfare_aggregate_lst_tt, welfare_aggregate_adjusted_lst_tt,
                                 ah_lst_pc, Eh_lst_pc, El_lst_pc, E_lst_pc, CS_capita_lst_pc, CS_capita_adjusted_lst_pc, CS_aggregate_lst_pc, CS_aggregate_adjusted_lst_pc, pil_lst_pc, pih_lst_pc, pi_aggregate_lst_pc, welfare_aggregate_lst_pc, welfare_aggregate_adjusted_lst_pc)
    return fig_area,  fig1, fig2, fig3
    

if __name__=="__main__":
    app.run_server(debug=True)