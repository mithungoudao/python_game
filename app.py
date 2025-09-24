import streamlit as st
import random
import math

# --- Step 1: Load URLs from text file ---
def load_urls(file_path="urls.txt"):
    with open(file_path, "r") as f:
        urls = [line.strip() for line in f if line.strip()]
    return urls

# Motivational quotes
quotes = [
    "🔥 Keep going, you’re crushing it!",
    "💡 Every click makes you smarter!",
    "🐍 You’re one step closer to mastering Python!",
    "🚀 Boom! Another lesson down!",
    "🏆 Great job! Your XP is leveling up!"
]

def main():
    st.set_page_config(page_title="Python Learning Game", page_icon="🐍")

    st.title("🐍 Python Learning Tracker (Gamified Edition)")

    urls = load_urls("urls.txt")

    # --- Session state ---
    if "index" not in st.session_state:
        st.session_state.index = 0
    if "xp" not in st.session_state:
        st.session_state.xp = 0

    total = len(urls)
    current_index = st.session_state.index

    # --- Calculate Progress ---
    completed = current_index
    progress = completed / total
    xp = st.session_state.xp
    level = math.floor(xp / 50) + 1

    if current_index < total:
        st.subheader(f"📖 Lesson {current_index+1} of {total}")
        st.write(f"[👉 Open this lesson here]({urls[current_index]})")

        # Progress bar
        st.progress(progress, text=f"{int(progress*100)}% completed")

        # Show XP and Level
        st.info(f"⭐ XP: {xp} | 🆙 Level: {level}")

        # Done button
        if st.button("✅ Done"):
            st.session_state.index += 1
            st.session_state.xp += 10  # Add XP
            st.success(random.choice(quotes))
            st.experimental_rerun()

    else:
        st.success("🎉 Congratulations! You’ve completed ALL lessons!")
        st.balloons()
        st.progress(1.0, text="100% completed")
        st.info(f"Final Score → ⭐ XP: {xp} | 🆙 Level: {level}")

        if progress == 1:
            st.snow()  # Extra fun

if __name__ == "__main__":
    main()