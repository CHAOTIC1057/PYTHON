import streamlit as st

# Set page configuration
st.set_page_config(page_title="Netflix Demo", layout="wide")

# Create a header
st.title("🎬 Netflix - Movie Streaming")

# Add some introductory text
st.markdown("""
Welcome to the Netflix demo site! Explore the trending movies and shows from your favorite genres. Enjoy!
""")

# Sample data for movies
movies = [
    {
        "title": "The Witcher",
        "description": "The Witcher, a saga of a mutated monster hunter, is set in a world of magic and medieval fantasy.",
        "image": "https://upload.wikimedia.org/wikipedia/en/0/08/The_Witcher_season_1.jpg"
    },
    {
        "title": "Stranger Things",
        "description": "A group of young friends in a small town uncover a secret government project while searching for their missing friend.",
        "image": "https://upload.wikimedia.org/wikipedia/en/3/38/Stranger_Things_season_4.jpg"
    },
    {
        "title": "Money Heist",
        "description": "A criminal mastermind plans a heist on the Royal Mint of Spain and assembles a team of eight robbers with unique skills.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Money_Heist_-_La_Casa_de_Papel.jpg/800px-Money_Heist_-_La_Casa_de_Papel.jpg"
    },
    {
        "title": "Squid Game",
        "description": "Hundreds of contestants with financial struggles participate in a deadly competition based on children's games for a tempting cash prize.",
        "image": "https://upload.wikimedia.org/wikipedia/en/3/37/Squid_Game_poster.jpg"
    }
]

# Display movie information in a grid layout
st.write("### Trending Movies")
col1, col2, col3, col4 = st.columns(4)

# Movie 1
with col1:
    st.image(movies[0]["image"], caption=movies[0]["title"], use_column_width=True)
    st.write(movies[0]["description"])

# Movie 2
with col2:
    st.image(movies[1]["image"], caption=movies[1]["title"], use_column_width=True)
    st.write(movies[1]["description"])

# Movie 3
with col3:
    st.image(movies[2]["image"], caption=movies[2]["title"], use_column_width=True)
    st.write(movies[2]["description"])

# Movie 4
with col4:
    st.image(movies[3]["image"], caption=movies[3]["title"], use_column_width=True)
    st.write(movies[3]["description"])

# Footer with a call to action
st.markdown("""
---
Explore more movies and shows on **Netflix**. Sign up now to start your free trial.
""")
