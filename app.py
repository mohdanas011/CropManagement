import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load encoder, scaler, and model_gbc
encoder = pickle.load(open(r"C:\Users\mohda\OneDrive\Desktop\model\encoder.pkl",'rb'))
scaler = pickle.load(open(r"C:\Users\mohda\OneDrive\Desktop\model\scaler.pkl",'rb'))
model_gbc = pickle.load(open(r"C:\Users\mohda\OneDrive\Desktop\model\model_gbc.pkl", 'rb'))

# Prediction function
def predict_crop(N, P, K, temperature, humidity, ph, rainfall):
    input_df = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
                            columns=['N','P','K','temperature','humidity','ph','rainfall'])
    input_scaled = scaler.transform(input_df)
    prediction = model_gbc.predict(input_scaled)
    prediction = encoder.inverse_transform(prediction)
    return prediction[0]

# ---------- Streamlit UI ----------
st.set_page_config(page_title="🌱 Crop Recommendation", page_icon="🌾", layout="wide")

# Custom CSS for bright theme
st.markdown("""
    <style>
    .main {background-color: #ffffff;}
    h1 {
        text-align: center;
        background: linear-gradient(to right, #4CAF50, #8BC34A);
        color: white;
        padding: 15px;
        border-radius: 10px;
    }
    .stButton>button {
        background: linear-gradient(to right, #43cea2, #185a9d);
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(to right, #185a9d, #43cea2);
        color: white;
        transform: scale(1.05);
    }
    .stNumberInput label {
        font-weight: bold;
        color: #2e7d32;
    }
    .card {
        padding: 15px;
        margin: 10px;
        border-radius: 12px;
        text-align: center;
        color: #333;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
    .icon-links a {
        margin: 0 5px;
        font-size: 20px;
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar - About App
st.sidebar.header("ℹ️ About App")
st.sidebar.markdown("""
This **Smart Crop Recommendation System** helps farmers and gardeners choose the **best crop** 
based on soil nutrients, environmental conditions, and rainfall.  

**How to use:**  
1. Enter soil parameters (N, P, K, pH).  
2. Enter environmental conditions (temperature, humidity, rainfall).  
3. Click the **Recommend Crop** button to see the best crop for your field.  

**Benefits:**  
- Save time choosing crops  
- Improve yield  
- Plan agriculture efficiently
""")

# Title
st.markdown("<h1>🌾 Smart Crop Recommendation System 🌞</h1>", unsafe_allow_html=True)
st.markdown("### Enter the **soil & environmental values** below:")

# Layout
col1, col2 = st.columns(2)
with col1:
    st.subheader("🌱 Soil Properties")
    N = st.number_input("Nitrogen (N)", min_value=0.0, max_value=150.0, step=1.0)
    P = st.number_input("Phosphorus (P)", min_value=0.0, max_value=100.0, step=1.0)
    K = st.number_input("Potassium (K)", min_value=0.0, max_value=100.0, step=1.0)
    ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.5, step=0.1)
with col2:
    st.subheader("🌤 Environmental Conditions")
    temperature = st.number_input("Temperature (°C)", min_value=10.0, max_value=100.0, step=0.5)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, step=0.5)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, step=1.0)

# Predict Button
st.markdown("---")
if st.button("🌱 Recommend Crop"):
    crop = predict_crop(N, P, K, temperature, humidity, ph, rainfall)

    # Emoji / Image mapping
    crop_emojis = {
        "rice": "🌾", "wheat": "🌿", "maize": "🌽", "chickpea": "🥜",
        "kidneybeans": "🫘", "pigeonpeas": "🌱", "mothbeans": "🌱",
        "mungbean": "🌱", "blackgram": "🌱", "lentil": "🥣",
        "pomegranate": "🍎", "banana": "🍌", "mango": "🥭",
        "grapes": "🍇", "watermelon": "🍉", "muskmelon": "🍈",
        "apple": "🍏", "orange": "🍊", "papaya": "🍍",
        "coconut": "🥥", "cotton": "🧵", "jute": "🪢", "coffee": "☕"
    }

    crop_info = {
        "rice": "Rice grows well in warm, wet conditions with fertile, well-drained soil.",
        "wheat": "Wheat prefers temperate climates and well-drained loamy soil.",
        "maize": "Maize requires moderate rainfall and well-drained fertile soil.",
        "chickpea": "Chickpea grows in semi-arid conditions with neutral to slightly alkaline soil.",
        "lentil": "Lentils grow best in cool climates with well-drained soil.",
        "banana": "Bananas thrive in tropical regions with high humidity and rich soil.",
        "mango": "Mango trees require tropical/subtropical climates with deep fertile soil.",
        "grapes": "Grapes prefer warm, dry climates and well-drained sandy soil.",
        "watermelon": "Watermelon grows well in warm, sunny areas with sandy loam soil.",
    }

    emoji = crop_emojis.get(crop.lower(), "🌱")
    info_text = crop_info.get(crop.lower(), "This crop grows best with proper care and suitable soil/environmental conditions.")

    st.success(f"✅ Recommended Crop: **{crop.capitalize()} {emoji}**")
    st.info(f"🌿 **About {crop.capitalize()}:** {info_text}")

# ---------- Team Section ----------
st.markdown("---")
st.markdown("<h2 style='text-align:center;'>👨‍👩‍👦 Meet Our Team members</h2>", unsafe_allow_html=True)

team_members = [
    {"role": "Lead Developer", "name": "Mohd Anas", "email": "mohdanas212655@gmail.com", "linkedin": "linkedin.com/in/mohd-anas-5b1a69293", "phone": "+91 7310016307"},
    {"role": "Lead AI Engineer", "name": "Shivam Mishra", "email": "shivam@example.com", "linkedin": "https://linkedin.com/in/shivam", "phone": "+91 8826326475"},
    {"role": "DevOps Engineer", "name": "Umesh", "email": "umesh@example.com", "linkedin": "https://linkedin.com/in/umesh", "phone": "+91 7011675647"},
    {"role": "Data Scientist", "name": "Paras", "email": "paras@example.com", "linkedin": "https://linkedin.com/in/paras", "phone": "+91 8816834263"},
    {"role": "Product Manager", "name": "Niyati", "email": "niyati@example.com", "linkedin": "https://linkedin.com/in/niyati", "phone": "+917827481421 "},
    {"role": "Frontend Developer", "name": "Tarun Kumar", "email": "tarun@example.com", "linkedin": "https://linkedin.com/in/tarun", "phone": "+91 9050343640"},
]

cols = st.columns(3)
for idx, member in enumerate(team_members):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class='card' style='background: linear-gradient(135deg, #FFD3B6, #FFAAA5);'>
            <h4>{member['role']}</h4>
            <p><strong>{member['name']}</strong></p>
            <div class='icon-links'>
                <a href='mailto:{member['email']}' target='_blank'>📧</a>
                <a href='{member['linkedin']}' target='_blank'>💼</a>
                <a href='tel:{member['phone']}' target='_blank'>📞</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
