import streamlit as st

st.set_page_config(page_title="Muhammad Noman Growth Mindset Project", page_icon="🌟")
st.title("Muhammad Noman Growth Mindset AI Project")

st.header("💞 Welcome to Your Growth Journey")

# Quote section
st.header("💚 Today's Growth Mindset Quote")
st.write("“Success is not final, failure is not fatal: It is the courage to continue that counts.” - Winston Churchill")

# Challenge input
st.header("♡ What's Your Challenge Today?")
user_input = st.text_input("Describe your challenge today", "e.g. I'm struggling to stay focused on my work")

# Condition
if user_input:
    st.success(f"You're facing: {user_input}. Keep pushing forward toward your goal!")
else:
    st.warning("🤔 What's your challenge today?")

# Reflection section
st.header("🌟 Reflect on Your Learning")
reflection = st.text_area("Write your reflection here", "e.g. What did you learn today? What challenges did you face? How can you overcome them?")

if reflection:
    st.success(f"🌟 Great Insight! Your reflection: {reflection} 🌟")
else:
    st.info("🤔 Reflecting on past experiences helps you grow! Share your difficulties.")

# Achievements section
st.header("🏆 Celebrate Your Achievements!")
achievement = st.text_input("Share something you've achieved today", "e.g. I completed my project ahead of schedule")

if achievement:   
    st.success(f"🎉 Congratulations! You've achieved: {achievement} 🎉")
else:
    st.info("🤔 Big or small, every achievement counts! Share one now! ❤️")

# Footer
st.write("----")
st.write("👭 Keep believing in yourself. Growth is a journey, not a destination. Keep pushing forward and you'll achieve great things! 💖")
st.write("🌟 Created with love by Muhammad Noman 🌟")

st.write("👭 keep believing in yourself.Growth is a journey, not a destination. Keep pushing forward and you'll achieve great things!💖")
  st.write("🌟Created with love by Muhammad Noman🌟")
  
     
