
import streamlit as st
import pyttsx3

st.title("AI Language Trainer – Michael's Meeting")
st.write("🎙️ Speak your sentence and get instant feedback.")

st.subheader("Michael:")
michael_line = "Can you briefly walk me through your proposal idea?"
st.write(michael_line)

# TTS
if st.button("▶ Hear Michael"):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(michael_line)
    engine.runAndWait()

st.subheader("🎤 Your Turn")
audio_input = st.text_input("Type what you said (for now, we'll simulate voice input):")

if audio_input:
    st.write("✅ Your sentence:")
    st.success(audio_input)

    # تقييم بسيط (مطابقة)
    if "proposal" in audio_input.lower() and "idea" in audio_input.lower():
        st.info("Your pronunciation and vocabulary are on point!")
    else:
        st.warning("Try to include keywords like 'proposal' and 'idea'.")

st.markdown("---")
st.write("📘 Vocabulary:")
st.code("proposal, idea, briefly, walk me through, concept")
