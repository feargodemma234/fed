import streamlit as st
import urllib.parse

st.set_page_config(page_title="QuantumKicks", layout="centered", page_icon="📦")

st.markdown("""
<style>
    .logo { font-size: 22px; font-weight: 800; color: #10B981; padding: 16px 20px; }
    .hero-box { background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%); padding: 50px 24px; border-radius: 0 0 40px 40px; text-align: center; color: white; margin: 0 0 30px 0; }
    .hero-box h1 { font-size: 32px; font-weight: 800; margin: 0 0 12px 0; }
    .hero-box p { font-size: 15px; color: #E0E7FF; margin: 0; }
    .send-btn { background: #EF4444; color: white; padding: 16px 0; border-radius: 12px; font-size: 18px; font-weight: 700; width: 100%; text-align: center; display: block; text-decoration: none; margin-top: 10px; border: none; }
    .send-btn-disabled { background: #444; color: #888; padding: 16px 0; border-radius: 12px; font-size: 18px; font-weight: 700; width: 100%; text-align: center; display: block; margin-top: 10px; border: none; }
</style>
""", unsafe_allow_html=True)

# HEADER
col1, col2 = st.columns([3,2])
with col1: st.markdown('<div class="logo">🛒 QuantumKicks</div>', unsafe_allow_html=True)
with col2:
    c1, c2 = st.columns(2)
    with c1: st.button("Sign In")
    with c2: st.button("Login")

# PURPLE BOX
st.markdown("""<div class="hero-box"><h1>Cravings Delivered.<br>Why Wait?</h1><p>From food to essentials — get anything delivered to you in minutes. Request now and get it.</p></div>""", unsafe_allow_html=True)

st.markdown("### 📦 Place Your Request")

# FORM
item = st.text_input("What do you want?", placeholder="e.g Pizza, Groceries, Phone Charger")
name = st.text_input("Your Full Name", placeholder="John Doe")
phone = st.text_input("Your Phone Number", placeholder="0803 123 4567")
address = st.text_area("Delivery Address", placeholder="123 Street, Port Harcourt", height=100)

# CHANGED EMAIL HERE
TO_EMAIL = "quantumindustries258@gmail.com"

subject = f"New Delivery Request - {item if item else 'New Request'}"
body = f"""Hi QuantumKicks Team,

I would like to place a request:

Item: {item}
Name: {name}
Phone: {phone}
Delivery Address: {address}

Thank you!"""
mailto_link = f"mailto:{TO_EMAIL}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"

if all([item.strip(), name.strip(), phone.strip(), address.strip()]):
    st.markdown(f'<a href="{mailto_link}" target="_blank"><button class="send-btn">📦 Send Request</button></a>', unsafe_allow_html=True)
else:
    st.markdown('<button class="send-btn-disabled" disabled>📦 Fill all fields</button>', unsafe_allow_html=True)