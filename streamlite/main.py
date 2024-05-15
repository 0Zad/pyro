import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from modelS.calc_press_cyl import model_s


st.write("""
    # Premiere app web
    Hello *world!*
""")

r = st.number_input("Entrer le rayon (en cm) de l'hemicylindre", min_value=5, max_value=60, step=5)
d = st.number_input("Entrer la distance charge - obstacle", min_value=10, max_value=300, step=10)

alph = st.slider('Cursor test', min_value=0, max_value=180, value=18)


if st.button("Afficher tous les angles"):
    l_ct, l_angle = [], []
    result = model_s(r,d,90)

    for angle in np.linspace(result[0], 180,):
        angle_res = model_s(r, d, angle)
        l_ct.append(angle_res[1])
        l_angle.append(angle)

    
    fig, ax = plt.subplots()
    ax.plot(l_angle, l_ct)
    ax.set_xlabel('Input Values')
    ax.set_ylabel('Result')
    ax.set_title('Result vs. Input Values')
    st.pyplot(fig)


# Button to perform the calculation
if st.button('Calcule du coefficient de transmission'):
    result = model_s(r,d,alph)
    ct = result[1]
    if ct != 0:
        st.success(f"Le coefficient de transmission pour l'angle {alph} est {ct:0.2f}")
    else :
        st.success(f"l'angle {alph}° est plus petit que l'angle limite {result[0]:0.1f}° : le point est en visu direct de l'explosif")
