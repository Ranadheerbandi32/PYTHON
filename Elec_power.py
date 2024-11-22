import streamlit as st
import math
def Resonance(R, L, C):
    F_R = 1 / (2 * math.pi * math.sqrt(L * C))  # Resonance Frequency
    BW = R / (2 * math.pi * L)  # Bandwidth
    Q = F_R / BW  # Quality Factor
    F_L = F_R - BW / 2  # Lower Cutoff Frequency
    F_U = F_R + BW / 2  # Upper Cutoff Frequency
    return F_R, BW, Q, F_L, F_U
    

st.title("02341A0259-PS3")
st.markdown("calculate resonance frequency(FR),band width(BW),quality factor(Q),upper cutoff frequency(FU),and lower cutoo frequency(FL,based on R,L,and C values for series resonance circuit)")


col1, col2 = st.columns(2)
with col1:
        with st.container(border=True):
            R = st.number_input("Resistance (R) in ohms", value=100.0, step=1.0)
            L = st.number_input("Inductance (L) in henries", value=0.1, step=0.01)
            C = st.number_input("Capacitance (C) in farads", value=1e-6, step=1e-7, format="%.7f")
            compute=st.button("Compute")
            

with col2:
        with st.container(border=True):
            if compute:
                    F_R, BW, Q, F_L, F_U = Resonance(R, L, C)

                    st.write(f"Resonance Frequency (F_R): {F_R:.2f} Hz")
                    st.write(f"Bandwidth (BW): {BW:.2f} Hz")
                    st.write(f"Quality Factor (Q): {Q:.2f}")
                    st.write(f"Lower Cutoff Frequency (F_L): {F_L:.2f} Hz")
                    st.write(f"Upper Cutoff Frequency (F_U): {F_U:.2f} Hz")