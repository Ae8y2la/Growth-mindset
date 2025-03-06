import streamlit as st
import random
from datetime import datetime, timedelta

# Sample data
affirmations = [
    "I am capable of learning and growing every day.",
    "Challenges help me grow stronger and smarter.",
    "Mistakes are opportunities to learn.",
    "I embrace effort and persistence to achieve my goals.",
    "I am constantly improving and getting better."
]

reflection_questions = [
    "What did I learn today?",
    "What challenges did I face, and how did I overcome them?",
    "What can I improve tomorrow?",
    "What am I grateful for today?",
    "How did I step out of my comfort zone today?"
]

# Initialize session state for progress tracking
if "goals" not in st.session_state:
    st.session_state.goals = []
if "reflections" not in st.session_state:
    st.session_state.reflections = []
if "affirmations" not in st.session_state:
    st.session_state.affirmations = []
if "streak" not in st.session_state:
    st.session_state.streak = 0
if "last_activity" not in st.session_state:
    st.session_state.last_activity = None

# Function to update streak
def update_streak():
    today = datetime.today().date()
    if st.session_state.last_activity:
        last_activity = st.session_state.last_activity.date()
        if today == last_activity + timedelta(days=1):
            st.session_state.streak += 1
        elif today > last_activity + timedelta(days=1):
            st.session_state.streak = 1  # Reset streak if missed a day
    else:
        st.session_state.streak = 1
    st.session_state.last_activity = datetime.today()

# Function to display falling stars effect
def show_stars():
    stars_js = """
    <script>
    function createStar() {
        const star = document.createElement('div');
        star.className = 'star';
        star.style.left = Math.random() * 100 + 'vw';
        star.style.animationDuration = Math.random() * 2 + 1 + 's';
        star.style.opacity = Math.random();
        document.body.appendChild(star);
    }
    setInterval(createStar, 100);
    </script>
    <style>
    .star {
        width: 2px;
        height: 2px;
        background-color: white;
        border-radius: 50%;
        position: fixed;
        top: -10px;
        animation: fall linear infinite;
        box-shadow: 0 0 5px white, 0 0 10px white;
    }
    @keyframes fall {
        0% { transform: translateY(0); }
        100% { transform: translateY(100vh); }
    }
    </style>
    """
    st.components.v1.html(stars_js, height=0)

# Function to display balloon effect
def show_balloons():
    balloon_js = """
    <script>
    function createBalloon() {
        const balloon = document.createElement('div');
        balloon.className = 'balloon';
        balloon.style.left = Math.random() * 100 + 'vw';
        balloon.style.animationDuration = Math.random() * 5 + 3 + 's';
        document.body.appendChild(balloon);
    }
    setInterval(createBalloon, 300);
    </script>
    <style>
    .balloon {
        width: 50px;
        height: 70px;
        background-color: #FF6F61;
        border-radius: 50%;
        position: fixed;
        bottom: -100px;
        animation: floatUp 5s linear infinite;
    }
    @keyframes floatUp {
        0% { transform: translateY(0); }
        100% { transform: translateY(-100vh); }
    }
    </style>
    """
    st.components.v1.html(balloon_js, height=0)

# Custom CSS
custom_css = """
<style>
/* Set background color for the entire app */
body, .stApp {
    background-color: #001F3F !important;
    color: #F6CBB6 !important;
}

/* Step 1: Style h1 headers */
h1 {
    color: #E9FFDB !important;
}

/* Step 2: Style h2 headers */
h2 {
    color: #EAE0C8 !important;
}

/* Step 3: Style h3 headers */
h3 {
    color: #EAE0C8  !important;
}

/* Step 4: Style h4 headers */
h4 {
    color: #EAE0C8  !important;
}

/* Step 5: Style h5 headers */
h5 {
    color: #EAE0C8  !important;
}

/* Step 6: Style h6 headers */
h6 {
    color: #EAE0C8  !important;
}

/* Step 7: Style headers inside Streamlit components */
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6,
.stText h1, .stText h2, .stText h3, .stText h4, .stText h5, .stText h6,
.stSidebar h1, .stSidebar h2, .stSidebar h3, .stSidebar h4, .stSidebar h5, .stSidebar h6 {
    color: #EAE0C8  !important;
}

/* Style buttons */
.stButton > button {
    background-color: #001F3F !important;
    color: #FFD700 !important;
    border: 1px solid #FFD700 !important;
    border-radius: 5px !important;
    padding: 10px 20px !important;
    font-weight: bold !important;
}

/* Hover effect for buttons */
.stButton > button:hover {
    background-color: #003366 !important;
    color: #FFD700 !important;
    border: 1px solid #FFD700 !important;
}

/* Style text input and text area */
.stTextInput > div > input, .stTextArea > div > textarea {
    background-color: #001F3F !important;
    color: #FFD700 !important;
    border: 1px solid #FFD700 !important;
    border-radius: 5px !important;
}

/* Style sidebar */
.css-1d391kg, .stSidebar {
    background-color: #001F3F !important;
    color: #FFD700 !important;
}

/* Style radio buttons (menu) */
.stRadio > div {
    background-color: #001F3F !important;
    color: #FFD700 !important;
    border-radius: 5px !important;
    padding: 10px !important;
    margin: 5px 0 !important;
}

/* Hover effect for radio buttons */
.stRadio > div:hover {
    background-color: #003366 !important;
}

/* Selected radio button */
.stRadio > div[data-baseweb="radio"] > div:first-child {
    background-color: #003366 !important;
    border-color: #FFD700 !important;
}

/* Label for selected radio button */
.stRadio > div[data-baseweb="radio"] > div:first-child > div {
    color: #FFD700 !important;
}

/* Custom style for image text */
.image-text {
    font-size: 18px;
    font-weight: bold;
    color: #FFD700;
    margin-top: 10px;
}
</style>
"""

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Streamlit app
st.title("🌱 Growth Mindset Challenge 🌱")
st.sidebar.header("Menu")
menu = st.sidebar.radio("Choose an activity:", ["Home", "Daily Affirmation", "Set Goals", "Reflect", "View Progress"])

if menu == "Home":
    st.write("### Welcome to the Growth Mindset Challenge! 🌟")
    st.write("This app is your personal guide to developing a **growth mindset**—the belief that you can improve and grow through effort, learning, and persistence.")
    st.write("Here's what you can do:")
    st.write("- 🌟 **Daily Affirmation**: Start your day with a positive mindset.")
    st.write("- 🎯 **Set Goals**: Define your weekly learning goals and track your progress.")
    st.write("- 📝 **Reflect**: Take a moment to reflect on your day and learn from your experiences.")
    st.write("- 📊 **View Progress**: See how far you've come with your affirmations, goals, and reflections.")
    st.write("Let's get started! Use the sidebar to navigate.")

elif menu == "Daily Affirmation":
    st.header("🌟 Daily Affirmation 🌟")
    st.write("Start your day with a positive thought to set the tone for growth and learning.")
    if st.button("Get Today's Affirmation"):
        affirmation = random.choice(affirmations)
        st.session_state.affirmations.append((datetime.today().strftime("%Y-%m-%d"), affirmation))
        update_streak()
        st.success(f"**{affirmation}**")
        show_stars()  # Show falling stars effect
    if st.session_state.affirmations:
        st.write("### Your Recent Affirmations:")
        for date, aff in st.session_state.affirmations[-5:]:  # Show last 5 affirmations
            st.write(f"📅 **{date}**: {aff}")

elif menu == "Set Goals":
    st.header("🎯 Set Your Weekly Goals 🎯")
    st.write("What do you want to achieve this week? Set **SMART goals** (Specific, Measurable, Achievable, Relevant, Time-bound) to stay focused and motivated.")
    goal = st.text_input("Enter a new goal:")
    if st.button("Add Goal"):
        if goal:
            st.session_state.goals.append((datetime.today().strftime("%Y-%m-%d"), goal))
            update_streak()
            st.success("Goal added! 🚀")
            show_balloons()  # Show balloon effect
        else:
            st.warning("Please enter a goal.")
    if st.session_state.goals:
        st.write("### Your Goals:")
        for date, goal in st.session_state.goals:
            st.write(f"📅 **{date}**: {goal}")

elif menu == "Reflect":
    st.header("📝 Reflection Time 📝")
    st.write("Take a moment to reflect on your day. What did you learn? What challenges did you overcome? Reflection helps you grow and improve.")
    question = random.choice(reflection_questions)
    st.write(f"**{question}**")
    reflection = st.text_area("Your response:")
    if st.button("Save Reflection"):
        if reflection:
            st.session_state.reflections.append((datetime.today().strftime("%Y-%m-%d"), reflection))
            update_streak()
            st.success("Reflection saved! 🌟")
            show_stars()  # Show falling stars effect
        else:
            st.warning("Please write your reflection.")
    if st.session_state.reflections:
        st.write("### Your Recent Reflections:")
        for date, ref in st.session_state.reflections[-5:]:  # Show last 5 reflections
            st.write(f"📅 **{date}**: {ref}")

elif menu == "View Progress":
    st.header("📊 Your Progress 📊")
    st.write(f"🔥 **Current Streak:** {st.session_state.streak} days")
    if st.session_state.streak >= 3:
        st.write("🎉 You're on a roll! Keep it up!")
    if st.session_state.streak >= 7:
        st.write("🏆 Wow! You're a Growth Mindset Champion!")
    
    if st.session_state.affirmations:
        st.write("### Affirmations:")
        for date, aff in st.session_state.affirmations:
            st.write(f"📅 **{date}**: {aff}")
    
    if st.session_state.goals:
        st.write("### Goals:")
        for date, goal in st.session_state.goals:
            st.write(f"📅 **{date}**: {goal}")
    
    if st.session_state.reflections:
        st.write("### Reflections:")
        for date, ref in st.session_state.reflections:
            st.write(f"📅 **{date}**: {ref}")

# Fun interactivity
st.sidebar.write("---")
st.sidebar.header("Fun Stats")
st.sidebar.write(f"🔥 **Current Streak:** {st.session_state.streak} days")
if st.session_state.streak >= 3:
    st.sidebar.write("🎉 You're on a roll! Keep it up!")
if st.session_state.streak >= 7:
    st.sidebar.write("🏆 Wow! You're a Growth Mindset Champion!")