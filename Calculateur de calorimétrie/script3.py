import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Calorimétrie Lab", page_icon="🧬", layout="centered")

# 2. 100% Reliable CSS Design (No external images)
st.markdown("""
    <style>
    /* Professional Mesh Gradient Background - Works Everywhere */
    .stApp {
        background-color: #0f172a;
        background-image: 
            radial-gradient(at 0% 0%, rgba(30, 58, 138, 0.5) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(14, 165, 233, 0.4) 0px, transparent 50%),
            radial-gradient(at 50% 0%, rgba(3, 105, 161, 0.3) 0px, transparent 50%);
        background-attachment: fixed;
    }

    /* Main Container Card */
    [data-testid="stVerticalBlock"] > div:has(div.stHeader) {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
    }

    /* Text & Labels */
    h1, h2, h3, label, p, .stMarkdown {
        color: #e2e8f0 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* The Pulse Animation for Results */
    @keyframes pulse-glow {
        0% { transform: scale(1); box-shadow: 0 0 5px rgba(0, 242, 254, 0.5); }
        50% { transform: scale(1.02); box-shadow: 0 0 20px rgba(0, 242, 254, 0.8); }
        100% { transform: scale(1); box-shadow: 0 0 5px rgba(0, 242, 254, 0.5); }
    }

    .result-display {
        background: rgba(0, 242, 254, 0.1);
        color: #00f2fe;
        border: 2px solid #00f2fe;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        margin-top: 25px;
        animation: pulse-glow 2s infinite ease-in-out;
    }

    /* Modern Button */
    .stButton>button {
        width: 100%;
        background: #0ea5e9 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        height: 45px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Application Logic
st.title("🧬 Calculateur Thermique")
st.write("Résolvez vos équations de calorimétrie instantanément.")

var = st.selectbox("Quelle variable recherchez-vous ?",
                  ["Énergie (Q)", "Masse (m)", "Capacité (c)", "Température (T)"])

st.divider()

with st.container():
    if "Énergie" in var:
        m = st.number_input("Masse (g)", min_value=0.0, format="%.2f")
        c = st.number_input("Capacité (J/g°C)", min_value=0.0, format="%.4f")
        dt = st.number_input("Variation de Température (°C)", format="%.2f")
        if st.button("CALCULER"):
            res = m * c * dt
            st.markdown(f'<div class="result-display">Q = {res:,.2f} Joules</div>', unsafe_allow_html=True)

    elif "Masse" in var:
        q = st.number_input("Énergie (J)", format="%.2f")
        c = st.number_input("Capacité (J/g°C)", min_value=0.01, format="%.4f")
        dt = st.number_input("Variation de Température (°C)", format="%.2f")
        if st.button("CALCULER"):
            if c * dt != 0:
                res = q / (c * dt)
                st.markdown(f'<div class="result-display">m = {res:,.2f} grammes</div>', unsafe_allow_html=True)
            else: st.error("Calcul impossible (division par zéro).")

    elif "Capacité" in var:
        q = st.number_input("Énergie (J)", format="%.2f")
        m = st.number_input("Masse (g)", min_value=0.01, format="%.2f")
        dt = st.number_input("Variation de Température (°C)", format="%.2f")
        if st.button("CALCULER"):
            if m * dt != 0:
                res = q / (m * dt)
                st.markdown(f'<div class="result-display">c = {res:,.4f} J/g°C</div>', unsafe_allow_html=True)
            else: st.error("Calcul impossible.")

    elif "Température" in var:
        mode = st.radio("Cible :", ["Variation (ΔT)", "Initiale (Ti)", "Finale (Tf)"], horizontal=True)
        q = st.number_input("Énergie (J)", format="%.2f")
        m = st.number_input("Masse (g)", min_value=0.01)
        c = st.number_input("Capacité (J/g°C)", min_value=0.01)

        if mode == "Variation (ΔT)":
            if st.button("CALCULER ΔT"):
                res = q / (m * c)
                st.markdown(f'<div class="result-display">ΔT = {res:,.2f} °C</div>', unsafe_allow_html=True)
        elif mode == "Initiale (Ti)":
            tf = st.number_input("Température Finale (°C)")
            if st.button("CALCULER Ti"):
                res = tf - (q / (m * c))
                st.markdown(f'<div class="result-display">Ti = {res:,.2f} °C</div>', unsafe_allow_html=True)
        elif mode == "Finale (Tf)":
            ti = st.number_input("Température Initiale (°C)")
            if st.button("CALCULER Tf"):
                res = (q / (m * c)) + ti
                st.markdown(f'<div class="result-display">Tf = {res:,.2f} °C</div>', unsafe_allow_html=True)
