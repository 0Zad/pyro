import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from modelS.calc_press_cyl import model_s


st.write("""
    # Premiere app web
    Hello *world!*
""")

r = 0.01*st.number_input("Entrer le rayon (en cm) de l'hemicylindre", min_value=5, max_value=60, step=5, value=20)
d = 0.01*st.number_input("Entrer la distance (en cm) charge - obstacle", min_value=10, max_value=300, step=10, value=60)


alph = st.slider('Cursor test', min_value=0, max_value=180, value=18)


if st.button("Afficher tous les angles"):
    l_ct, l_angle = [], []
    result = model_s(r,d,alph)

    for angle in np.linspace(result[0], 180,):
        angle_res = model_s(r, d, angle)
        l_ct.append(angle_res[1])
        l_angle.append(angle)

    
    # fig, ax = plt.subplots()
    # ax.plot(l_angle, l_ct)
    # ax.set_xlabel('Input Values')
    # ax.set_ylabel('Result')
    # ax.set_title('Result vs. Input Values')
    # st.pyplot(fig)

    fig =go.Figure()
    fig.add_trace(go.Scatter(x=l_angle, y=l_ct, mode='markers+lines', marker=dict(color='blue', size=10)))
    fig.add_trace(go.Scatter(x=[alph, alph, alph, 0], y=[0,result[1], result[1], result[1]], mode='lines', marker=dict(color='red', size=10)))
    fig.update_layout(title='Model S', xaxis_title='Angle', yaxis_title='Coefficient de transmission',)
    
    # Display the plot on the Streamlit app page
    st.plotly_chart(fig)



# Button to perform the calculation
if st.button('Calcule du coefficient de transmission'):
    result = model_s(r,d,alph)
    ct = result[1]
    if ct != 0:
        st.success(f"Le coefficient de transmission pour l'angle {alph} est {ct:0.2f}")
    else :
        st.success(f"l'angle {alph}° est plus petit que l'angle limite {result[0]:0.1f}° : le point est en visu direct de l'explosif")
