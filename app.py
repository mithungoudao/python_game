import streamlit as st
import json
import os
import random
import math

PROGRESS_FILE = "progress.json"

# --- Load URLs ---
def load_urls(file_path="urls.txt"):
    with open(file_path, "r") as f:
        urls = [line.strip() for line in f if line.strip()]
    return urls

# --- Load progress ---
def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {"index": 0, "xp": 0}

# --- Save progress ---
def save_progress(progress):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f)

quotes = [
    "🔥 Keep going, you’re crushing it!",
    "💡 Every click makes you smarter!",
    "🐍 You’re one step closer to mastering Python!",
    "🚀 Boom! Another lesson down!",
    "🏆 Great job! Your XP is leveling up!"
]

def main():
    st.set_page_config(page_title="Python Learning Game", page_icon="🐍")

    st.title("🐍 Python Learning Tracker (Persistent Gamified Edition)")

    urls = load_urls("urls.txt")
    total = len(urls)

    # Load saved progress
    progress_data = load_progress()
    current_index = progress_data["index"]
    xp = progress_data["xp"]
    completed = current_index
    progress = completed / total
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
            progress_data["index"] += 1
            progress_data["xp"] += 10
            save_progress(progress_data)
            st.success(random.choice(quotes))
            st.rerun()

    else:
        st.success("🎉 Congratulations! You’ve completed ALL lessons!")
        st.balloons()
        st.progress(1.0, text="100% completed")
        st.info(f"Final Score → ⭐ XP: {xp} | 🆙 Level: {level}")
        st.snow()

if __name__ == "__main__":
    main()