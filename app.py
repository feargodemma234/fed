import streamlit as st
import urllib.parse
import os

st.set_page_config(page_title="QuantumKicks", layout="centered", page_icon="📦")

# HIDE STREAMLIT HEADER + GREETING
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 1rem;}
    
    .logo { font-size: 22px; font-weight: 800; color: #10B981; padding: 10px 0 20px 0; text-align: center; }
    .hero-box { background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%); padding: 40px 24px; border-radius: 0 0 40px 40px; text-align: center; color: white; margin: 0 0 30px 0; }
    .hero-box h1 { font-size: 32px; font-weight: 800; margin: 0 0 12px 0; }
    .hero-box p { font-size: 15px; color: #E0E7FF; margin: 0; }
    .send-btn { background: #EF4444; color: white; padding: 16px 0; border-radius: 12px; font-size: 18px; font-weight: 700; width: 100%; text-align: center; display: block; text-decoration: none; margin-top: 20px; border: none; }
</style>
""", unsafe_allow_html=True)

# LOGO ONLY - NO GREETING
st.markdown('<div class="logo">🛒 QuantumKicks</div>', unsafe_allow_html=True)

# HERO BOX
st.markdown("""<div class="hero-box"><h1>Cravings Delivered.<br>Why Wait?</h1><p>From food to essentials — get anything delivered to you in minutes. Request now and get it.</p></div>""", unsafe_allow_html=True)

st.markdown("### 📦 Place Your Request")
item = st.text_input("What do you want?", placeholder="e.g Pizza, Groceries")
name = st.text_input("Your Full Name", placeholder="John Doe")
phone = st.text_input("Your Phone Number", placeholder="0803 123 4567")
address = st.text_area("Delivery Address", placeholder="123 Street, Port Harcourt", height=100)
budget = st.text_input("Your Budget", placeholder="e.g ₦5,000") # <-- NEW FIELD

# EMAIL FROM ENV VARIABLE
TO_EMAIL = os.getenv("TO_EMAIL", "quantumindustries258@gmail.com")

# FIX: If empty, use "Not provided" so Gmail never receives empty
item_val = item if item.strip() else "Not provided"
name_val = name if name.strip() else "Not provided"
phone_val = phone if phone.strip() else "Not provided"
address_val = address if address.strip() else "Not provided"
budget_val = budget if budget.strip() else "Not provided"

subject = f"New Delivery Request - {item_val}"
# Use | instead of \n because Android Gmail app handles it better
body = f"Item: {item_val} | Name: {name_val} | Phone: {phone_val} | Address: {address_val} | Budget: {budget_val}"

mailto_link = f"mailto:{TO_EMAIL}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"

# BUTTON IS ALWAYS ACTIVE
st.markdown(f'<a href="{mailto_link}" target="_blank"><button class="send-btn">📦 Send Request</button></a>', unsafe_allow_html=True)