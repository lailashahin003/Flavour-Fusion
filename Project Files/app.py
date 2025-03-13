import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import random

# Load API Key from api_key.env
load_dotenv("api_key.env")

# Get API Key securely
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("Missing Google API Key! Add it to api_key.env.")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

# Function to generate recipe
def generate_recipe(topic, word_count):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Write a {word_count}-word blog on {topic} with a detailed recipe.")
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# List of programmer jokes
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs! 🐞",
    "Why was the JavaScript developer sad? Because he didn’t ‘null’ his feelings.",
    "Why do Python developers prefer snakes? Because they love indentation!",
    "What is a programmer’s favorite hangout place? The Foo Bar!",
    "How do you comfort a JavaScript bug? You console it. 😂",
    "Why did the developer go broke? Because he used up all his cache!",
    "Why was the computer cold? It left its Windows open!"
]

# UI Design
st.title("Flavour Fusion: AI-Driven Recipe Blogging 🍽️")

topic = st.text_input("Enter Recipe Topic", "Vegan Chocolate Cake")
word_count = st.slider("Select Word Count", 500, 2000, 1200)

if st.button("Generate Recipe"):
    with st.spinner("Generating..."):
        recipe = generate_recipe(topic, word_count)
        joke = random.choice(jokes)  # Select a random joke
        st.success("Recipe Generated!")
        st.write(recipe)
        st.info(f"Joke: {joke}")
