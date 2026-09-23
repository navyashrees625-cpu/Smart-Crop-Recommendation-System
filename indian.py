import streamlit as st
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Indian Smart Farmer Pro", layout="wide")

# ---------------- CUSTOM STYLING ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
}

.main {
    background: linear-gradient(to right, #e6f9f0, #f0fff4);
}

.title-style {
    font-size: 40px;
    font-weight: 700;
    color: #0a5c36;
}

.subtitle-style {
    font-size: 18px;
    color: #444;
}

.crop-card {
    background: white;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    transition: 0.3s;
}

.crop-card:hover {
    transform: scale(1.03);
}

.badge {
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="title-style">🌾 Smart Crop Recommendation System 🌱 </div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-style">Scientific crop suggestions with full agronomic details</div>',
            unsafe_allow_html=True)
st.markdown("---")

# ---------------- CROP DATABASE ----------------
CROP_DATABASE = {
    "Rice": {"category": "Cereal", "days": (105, 150), "temp": "20-35°C", "water": "1200-1600 mm",
             "spacing": "20x15 cm", "soil": ["Alluvial", "Clay"]},
    "Wheat": {"category": "Cereal", "days": (100, 140), "temp": "15-25°C", "water": "400-800 mm", "spacing": "22x10 cm",
              "soil": ["Alluvial", "Black"]},
    "Maize": {"category": "Cereal", "days": (90, 110), "temp": "18-27°C", "water": "500-800 mm", "spacing": "60x25 cm",
              "soil": ["Alluvial", "Red", "Black"]},
    "Tomato": {"category": "Vegetable", "days": (60, 80), "temp": "18-30°C", "water": "600-800 mm",
               "spacing": "60x45 cm", "soil": ["Alluvial", "Red", "Black"]},
    "Potato": {"category": "Vegetable", "days": (75, 120), "temp": "15-25°C", "water": "500-700 mm",
               "spacing": "60x20 cm", "soil": ["Alluvial", "Sandy"]},
    "Onion": {"category": "Vegetable", "days": (100, 120), "temp": "20-30°C", "water": "350-550 mm",
              "spacing": "15x10 cm", "soil": ["Alluvial", "Black"]},
    "Banana": {"category": "Fruit", "days": (300, 365), "temp": "25-35°C", "water": "1000-2500 mm",
               "spacing": "1.8x1.8 m", "soil": ["Alluvial", "Black"]},
    "Mango": {"category": "Fruit", "days": (1500, 1825), "temp": "24-30°C", "water": "750-2500 mm",
              "spacing": "10x10 m", "soil": ["Alluvial", "Laterite"]},
    "Sugarcane": {"category": "Cash Crop", "days": (300, 365), "temp": "20-35°C", "water": "1500-2500 mm",
                  "spacing": "90x30 cm", "soil": ["Alluvial", "Black"]},
    "Cotton": {"category": "Fiber", "days": (160, 180), "temp": "21-30°C", "water": "500-1200 mm",
               "spacing": "75x30 cm", "soil": ["Black"]},
    "Brinjal": {"category": "Vegetable", "days": (120, 150), "temp": "21-30°C", "water": "500-750 mm",
                "spacing": "60x60 cm", "soil": ["Sandy", "Clay"]},
    "Chilli": {"category": "Spice", "days": (120, 150), "temp": "20-25°C", "water": "500-800 mm",
               "spacing": "60x45 cm", "soil": ["Sandy", "Clay"]},
    "Marigold": {"category": "Flower", "days": (70, 90), "temp": "18-25°C", "water": "400-500 mm",
                 "spacing": "45x45 cm", "soil": ["Sandy"]},
    "Rose": {"category": "Flower", "days": (60, 90), "temp": "15-28°C", "water": "700-1000 mm",
             "spacing": "120x120 cm", "soil": ["Sandy"]},
    "Jasmine": {"category": "Flower", "days": (150, 180), "temp": "20-30°C", "water": "600-800 mm",
                "spacing": "150x150 cm", "soil": ["Sandy", "Red"]},
    "Tuberose": {"category": "Flower", "days": (90, 120), "temp": "20-30°C", "water": "600-800 mm",
                 "spacing": "30x20 cm", "soil": ["Sandy"]},
    "Cauliflower": {"category": "Vegetable", "days": (90, 120), "temp": "15-25°C", "water": "500-700 mm",
                    "spacing": "60x45 cm", "soil": ["Sandy", "Clay"]},
    "Okra": {"category": "Vegetable", "days": (90, 100), "temp": "22-35°C", "water": "400-600 mm",
             "spacing": "45x30 cm", "soil": ["Sandy", "Clay"]}

}


CROP_IMAGES = {
    "Rice": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvJlWgt2pYOKkyJyC87ybiAV56fmylG05JZA&s",
    "Wheat": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7REXsyj60ncyBD6klVrILC8Og9VK9srvdyA&s",
    "Maize": "https://thumbs.dreamstime.com/b/different-corn-plantation-524311.jpg",
    "Tomato": "https://media.istockphoto.com/id/1132371208/photo/three-ripe-tomatoes-on-green-branch.jpg?s=612x612&w=0&k=20&c=qVjDb5Tk3-UccV-E9gqvoz97PTsP1QmBftw27qA9kEo=",
    "Potato": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUXyov4nMm_Xjv8L49Jzl5L779yAYQdFshBw&s",
    "Onion": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuvt5tbxSlVBZyF4y6h04wFuDoxu-qw26y9Q&s",
    "Banana": "https://eos.com/wp-content/uploads/2024/05/banana-growing-plantation.png.webp",
    "Mango": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSacMGp8hV0TiPm9WfV0cCuGqzHvJdmZRk39w&s",
    "Sugarcane": "https://www.mahagro.com/cdn/shop/articles/iStock_000063947343_Medium_4e1c882b-faf0-4487-b45b-c2b557d32442.jpg?v=1541408129",
    "Cotton": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDhnhqJIj85bgubo4cJR9FeewK6k5WEGyVJg&s",
    "Brinjal": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_Z_fN1UbmaThgxUeq_evjGQ59yuKqf1NvVw&s",
    "Chilli": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVDwtzdLlfasJWHhF5DKDTCiYRbj44mDraKA&s",
    "Marigold": "https://images.ctfassets.net/bq61jovlhx8i/6y4VgNA9VFDhv7YigTmiQa/d1aaf4b00ff811d03395961dee9c9bc7/MAR-A_AMX00076_Blog.jpg",
    "Rose": "https://almondsbury.co.uk/cdn/shop/collections/roses.png?v=1740656315&width=1296",
    "Jasmine": "https://gilmour.com/wp-content/uploads/2019/05/Jasmine-Care.jpg",
    "Tuberose": "https://beejwala.com/cdn/shop/files/tuberosemixbulb.png?v=1741783591",
    "Cauliflower": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvyLiEATVXMqCpihlrLBfTa7KPt5HGa2lTMw&s",
    "Okra" :  "https://samsgardenstore.com/cdn/shop/files/Favorite-Okra-Varieties.jpg?v=1734083792&width=1445"
}

# ---------------- USER INPUT ----------------
st.subheader("🧪 Enter Soil & Climate Details")

col1, col2, col3 = st.columns(3)

with col1:
    nitrogen = st.number_input("Nitrogen (N)", 0, 150, 50)
    phosphorus = st.number_input("Phosphorus (P)", 0, 150, 40)
    potassium = st.number_input("Potassium (K)", 0, 150, 40)

with col2:
    soil_type = st.selectbox("Soil Type", ["Alluvial", "Black", "Red", "Laterite", "Sandy", "Clay"])
    rainfall = st.number_input("Annual Rainfall (mm)", 0, 3000, 1000)

with col3:
    soil_depth = st.selectbox("Soil Depth", ["Shallow", "Medium", "Deep"])
    ph = st.slider("Soil pH", 0.0, 14.0, 6.5)


# ---------------- RECOMMENDATION LOGIC ----------------
def get_recommendations():
    results = []
    for crop, data in CROP_DATABASE.items():
        if soil_type in data["soil"]:
            if rainfall >= 400:
                results.append(crop)
    return results


# ---------------- ANALYSIS ----------------
if st.button("🚀 Analyze & Generate Report"):

    st.success("Analysis Complete ✅")

    recommendations = get_recommendations()

    if recommendations:
        st.subheader("🌱 Recommended Crops")

        cols = st.columns(3)

        for i, crop in enumerate(recommendations):
            with cols[i % 3]:
                data = CROP_DATABASE[crop]
                img = CROP_IMAGES.get(crop)

                # Create a container for the card effect
                with st.container(border=True):
                    st.image(img, use_container_width=True, caption=crop)

                    # Category Badge using Markdown
                    st.markdown(
                        f'<span class="badge" style="background-color:#2e8b57; color:white; padding:2px 8px; border-radius:10px;">{data["category"]}</span>',
                        unsafe_allow_html=True)

                    st.markdown(f"### {crop}")

                    with st.expander("View Details"):
                        st.write(f"⏳ **Duration:** {data['days'][0]}-{data['days'][1]} days")
                        st.write(f"🌡 **Temp:** {data['temp']}")
                        st.write(f"💧 **Water:** {data['water']}")
                        st.write(f"📏 **Spacing:** {data['spacing']}")

        # ---------------- REPORT ----------------
        st.markdown("---")
        st.subheader("📄 Farm Analysis Report")
        st.info(f"""
        📅 Date: {datetime.now().strftime('%d %B %Y')}

        🌱 Soil Type: {soil_type}  
        🌧 Rainfall: {rainfall} mm  
        🧪 NPK Levels: {nitrogen}-{phosphorus}-{potassium}  
        ⚖ pH Level: {ph}  

        ✅ Total Recommended Crops: {len(recommendations)}
        """)

    else:
        st.error("No suitable crops found. Try adjusting inputs.")

