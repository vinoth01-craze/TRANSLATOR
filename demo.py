import streamlit as st
from translate import Translator
from gtts import gTTS
import os

def main():
    st.title("Simple Translator App")
    st.markdown(
        """
        <style>

        h1 {
            width: 400px;
            padding: 0%;
            top: 5%;
            left: 40%;
            font-size: 60px;
            color: light=white;
            font-family: Garamond, serif;
            white-space: nowrap; /* Ensures text stays on a single line */
            -webkit-animation: glow 1s ease-in-out infinite alternate;
            -moz-animation: glow 1s ease-in-out infinite alternate;
            animation: glow 1s ease-in-out infinite alternate;
            margin-bottom: 100px;
            background-clip: padding-box;
            box-shadow: 0 0 50px white;
        }
        h2{
            color:lightblue;
            font-family: Copperplate, Papyrus, fantasy;
        }
        h3{
            color:yellow;
          font-family: Copperplate, Papyrus, fantasy;
        }
        P {
            color: black;
            font-family: Copperplate, Papyrus, fantasy;
        }
        .stButton>button {
            background-color: white; /* Background color of the button */
        }
        .stButton>button:hover {
            cursor: pointer;
        }
        .stApp {
            background-image: url("https://static.vecteezy.com/system/resources/thumbnails/039/650/006/small_2x/modern-abstract-technology-background-design-illustration-vector.jpg");
            background-size: cover;
            object-fit:center;
        }

        /* Custom CSS for table text color */
        table.dataframe td {
            color: #666;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # Input type selection
    input_type = st.radio("Select Input Type", ("Text",))

    if input_type == "Text":
        # Input text
        input_text = st.text_area("Enter Text to Translate", "")

        # Language selection
        src_lang = st.selectbox("Select Source Language", ("en", "es", "fr", "de", "ja", "ko", "ta", "hi", "ml"))
        dest_lang = st.selectbox("Select Destination Language", ("en", "es", "fr", "de", "ja", "ko", "ta", "hi", "ml"))

        # Translate button
        if st.button("Translate"):
            translator = Translator(to_lang=dest_lang, from_lang=src_lang)
            translation = translator.translate(input_text)
            if translation:
                st.success(f"Translated Text: {translation}")

                # Generate audio
                tts = gTTS(text=translation, lang=dest_lang)
                audio_file = "translated_audio.mp3"
                tts.save(audio_file)
                st.audio(audio_file, format='audio/mp3', start_time=0)

                # Delete audio file after playing
                os.remove(audio_file)
            else:
                st.error("Translation failed. Please try again.")

if __name__ == "__main__":
    main()
