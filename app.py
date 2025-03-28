import streamlit as st
import random
from datetime import datetime

# Simulated trend database
trend_database = {
    "fashion": ["#FashionVibes", "#StyleGoals", "#TrendyLook", "#ChicFuture", "#GlamTech", "chic", "glam", "vogue", "trend", "style"],
    "tech": ["#TechLife", "#GadgetTrend", "#InnovateNow", "#CyberFuture", "#SmartEra", "smart", "future", "gadget", "techie", "innovation"],
    "food": ["#FoodLovers", "#TastyBites", "#YummyTrend", "#FlavorRush", "#FoodTech", "delicious", "flavor", "yummy", "taste", "bite"],
    "fitness": ["#FitLife", "#WorkoutVibes", "#HealthTrend", "#PowerCore", "#FitFuture", "strong", "active", "fit", "health", "energy"],
    "travel": ["#TravelGoals", "#Wanderlust", "#ExploreNow", "#SpaceJourney", "#GlobeTech", "adventure", "journey", "explore", "travel", "wander"]
}
default_trends = ["#Trending", "#ViralNow", "#ExploreMore", "#NextGen", "#FutureNow", "new", "hot", "top", "viral", "trend"]

class InstaTrendOptimizer:
    def __init__(self, niche, product_name, description=None):
        self.niche = niche.lower()
        self.product_name = product_name.lower()
        self.description = description.lower() if description else None
        self.current_date = datetime.now().strftime("%Y-%m-%d")
        self.trends = self.fetch_simulated_trends()

    def fetch_simulated_trends(self):
        return trend_database.get(self.niche, default_trends)

    def generate_caption(self):
        if self.description:
            trend_word = random.choice(self.trends).replace("#", "")
            mood = random.choice(["So futuristic!", "Mind-blowing!", "Next-level stuff!", "Out of this world!"])
            base = f"Step into the future with this {self.product_name}! {self.description.capitalize()} like never before. " \
                   f"This is more than just a {self.niche} moment—it’s a cosmic experience waiting to happen. " \
                   f"Embrace the {trend_word} energy and let your vibe resonate across the galaxy. {mood} " \
                   f"Ready to launch this into your feed today, {self.current_date}—are you in?"
        else:
            trend_word = random.choice(self.trends).replace("#", "")
            mood = random.choice(["Epic vibes!", "Totally unreal!", "Future-ready!", "Cosmic win!"])
            base = f"Teleport your {self.niche} game with this {self.product_name}! It’s not just a product, it’s a portal " \
                   f"to a new dimension of awesomeness. Feel the {trend_word} surge through you as you unlock its power. " \
                   f"Perfect for fans who live ahead of the curve—this is your ticket to the stars. {mood} " \
                   f"Beam it up to your Instagram on {self.current_date} and watch it soar!"
        return base

    def generate_hashtags(self):
        niche_tags = [f"#{self.niche}", f"#{self.niche}Lovers", f"#{self.niche}Future", f"#{self.niche}2025"]
        product_tags = [f"#{self.product_name}", f"#{self.product_name}Addict", f"#{self.product_name}Vibes"]
        if self.description:
            desc_words = self.description.split()
            desc_tags = [f"#{word}" for word in desc_words if len(word) > 3][:3]
            return niche_tags + product_tags + desc_tags + self.trends[:4]
        return niche_tags + product_tags + self.trends[:6]

    def generate_seo_keywords(self):
        base_keywords = [self.product_name, self.niche, "future", "trend"]
        trend_keywords = [word.replace("#", "").lower() for word in self.trends[:3]]
        if self.description:
            desc_keywords = [word for word in self.description.split() if len(word) > 3][:3]
            return base_keywords + desc_keywords + trend_keywords + ["2025", "best", "viral"]
        return base_keywords + trend_keywords + ["2025", "best", "viral"]

    def simulate_algorithm_insight(self):
        engagement_score = random.randint(40, 90)
        reach_potential = engagement_score * (len(self.trends) + (2 if self.description else 1))
        recommendation = "Launch now for stellar reach!" if reach_potential > 150 else "Add a futuristic CTA for max orbit!"
        return {
            "engagement_score": engagement_score,
            "reach_potential": reach_potential,
            "recommendation": recommendation
        }

    def optimize(self):
        return {
            "caption": self.generate_caption(),
            "hashtags": self.generate_hashtags(),
            "seo_keywords": self.generate_seo_keywords(),
            "algorithm_insight": self.simulate_algorithm_insight()
        }

# Sci-Fi UI with Custom CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0d1b2a, #1b263b);
        color: #e0e1dd;
        font-family: 'Orbitron', sans-serif;
    }
    .stTextInput>label, .stSelectbox>label, .stTextArea>label {
        color: #00ffcc;
        font-size: 18px;
        font-weight: bold;
        text-shadow: 0 0 5px #00ffcc;
    }
    .stTextInput>div>input, .stTextArea>div>textarea {
        background-color: #1b263b;
        color: #00ffcc;
        border: 2px solid #415a77;
        border-radius: 10px;
        padding: 12px;
        box-shadow: 0 0 10px rgba(0, 255, 204, 0.3);
    }
    .stSelectbox>div>div {
        background-color: #1b263b;
        color: #00ffcc;
        border: 2px solid #415a77;
        border-radius: 10px;
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff0066, #ffcc00);
        color: #ffffff;
        border-radius: 12px;
        padding: 12px 25px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        box-shadow: 0 0 15px rgba(255, 0, 102, 0.5);
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #ff3399, #ffeb3b);
        box-shadow: 0 0 20px rgba(255, 51, 153, 0.7);
    }
    .stSuccess {
        background-color: #00cc99;
        border-radius: 10px;
        padding: 15px;
        color: #ffffff;
        text-shadow: 0 0 5px #00cc99;
    }
    .stSubheader {
        color: #ff0066;
        font-size: 22px;
        font-weight: bold;
        text-shadow: 0 0 10px #ff0066;
    }
    .output-box {
        background: rgba(27, 38, 59, 0.8);
        border: 2px solid #00ffcc;
        border-radius: 12px;
        padding: 20px;
        margin-top: 15px;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit UI
st.title("🚀 InstaVerse Optimizer 🚀")
st.write("Power up your Instagram with sci-fi precision!")

with st.form(key="optimizer_form"):
    st.markdown("### Enter Your Coordinates")
    username = st.text_input("Username", placeholder="e.g., cyberuser_x")
    id_type = st.selectbox("ID Type", ["Personal", "Business", "Creator"])
    niche = st.text_input("Niche", placeholder="e.g., fashion, tech, food")
    product_name = st.text_input("Product Name", placeholder="e.g., sneakers, quantumphone")
    description = st.text_area("Optional: Mission Brief (Post/Reel Description)", 
                              placeholder="e.g., unveiling my latest tech masterpiece", height=120)
    submit_button = st.form_submit_button(label="Engage Hyperdrive")

if submit_button:
    if niche and product_name:
        optimizer = InstaTrendOptimizer(niche, product_name, description if description else None)
        result = optimizer.optimize()
        st.success("🌌 Hyperdrive Engaged! Post Optimized!")
        
        st.subheader("Transmission (Caption)")
        st.markdown(f"<div class='output-box'>{result['caption']}</div>", unsafe_allow_html=True)
        
        st.subheader("Quantum Tags (Hashtags)")
        st.markdown(f"<div class='output-box'>{' '.join(result['hashtags'])}</div>", unsafe_allow_html=True)
        
        st.subheader("SEO Nebula (Keywords)")
        st.markdown(f"<div class='output-box'>{' '.join(result['seo_keywords'])}</div>", unsafe_allow_html=True)
        
        st.subheader("Algorithm Matrix")
        st.markdown(f"<div class='output-box'>"
                    f"Engagement Core: {result['algorithm_insight']['engagement_score']}<br>"
                    f"Reach Velocity: {result['algorithm_insight']['reach_potential']}<br>"
                    f"Command: {result['algorithm_insight']['recommendation']}"
                    f"</div>", unsafe_allow_html=True)
        
        st.write(f"Locked for {id_type} unit: @{username}", unsafe_allow_html=True)
    else:
        st.error("Core systems require Niche and Product Name input!")

st.markdown("<hr><p style='text-align: center; color: #ffcc00;'>Crafted in the Cosmos for Instagram Pioneers 🌠</p>", unsafe_allow_html=True)
