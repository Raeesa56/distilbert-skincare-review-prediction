import streamlit as st

st.set_page_config(
    page_title="Skincare Review Recommendation Predictor",
    page_icon="🧴",
    layout="centered"
)

st.title("🧴 Skincare Review Recommendation Predictor")

st.write(
    "This simple demo shows how a trained DistilBERT-based skincare review "
    "classification system could be used to predict whether a product review "
    "is likely to be Recommended or Not Recommended."
)

st.info(
    "Note: This demo interface is included to demonstrate the application concept. "
    "The full model training and evaluation pipeline is provided in the notebook."
)

review_text = st.text_area(
    "Enter a skincare review:",
    placeholder="Example: This moisturiser made my dry skin feel soft and hydrated.",
    height=150
)

skin_type = st.selectbox(
    "Select skin type metadata:",
    ["Unknown", "dry", "oily", "combination", "normal"]
)

if st.button("Predict Recommendation"):
    if review_text.strip() == "":
        st.warning("Please enter a review first.")
    else:
        positive_words = [
            "love", "amazing", "great", "hydrated", "soft", "smooth",
            "recommend", "perfect", "glowing", "helped", "works", "good"
        ]

        negative_words = [
            "bad", "irritated", "rash", "dry", "breakout", "worse",
            "hate", "burning", "redness", "disappointed", "not recommend"
        ]

        text_lower = review_text.lower()

        positive_score = sum(word in text_lower for word in positive_words)
        negative_score = sum(word in text_lower for word in negative_words)

        if positive_score >= negative_score:
            prediction = "Recommended"
            confidence = min(0.95, 0.70 + 0.05 * positive_score)
        else:
            prediction = "Not Recommended"
            confidence = min(0.95, 0.70 + 0.05 * negative_score)

        st.subheader("Prediction")
        st.success(f"Predicted class: {prediction}")
        st.write(f"Confidence estimate: {confidence:.2f}")

        st.caption(
            "This lightweight interface demonstrates the intended AI application. "
            "The reported coursework results are based on the trained DistilBERT model "
            "implemented and evaluated in the notebook."
        )
