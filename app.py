import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

st.title("📝 Sentiment Analysis App")
st.markdown("Enter some text below, and I'll analyze its sentiment for you!")

user_input = st.text_area("Your Text:", placeholder="Type your text here...", height=150)

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze!")
    else:
        sentiment_scores = analyzer.polarity_scores(user_input)
        
        compound_score = sentiment_scores['compound']
        positive_score = sentiment_scores['pos']
        negative_score = sentiment_scores['neg']
        neutral_score = sentiment_scores['neu']

        if compound_score >= 0.05:
            sentiment = "Positive 😊👍✅"
            st.markdown(f"### Sentiment: **{sentiment}**")
        elif compound_score <= -0.05:
            sentiment = "Negative 😞👎❌"
            st.markdown(f"### Sentiment: **{sentiment}**")
        else:
            sentiment = "Neutral 😐🤷‍♂️"
            st.markdown(f"### Sentiment: **{sentiment}**")

        st.markdown("#### Detailed Scores:")
        st.write(f"- **Positive**: {positive_score:.2f}")
        st.write(f"- **Negative**: {negative_score:.2f}")
        st.write(f"- **Neutral**: {neutral_score:.2f}")

        st.markdown("""
        **What do these scores mean?**
        - **Compound Score**: Ranges from -1 (most negative) to 1 (most positive). A score ≥ 0.5 indicates positive sentiment, ≤ -0.5 indicates negative, and between -0.05 and 0.05 is neutral.
        - **Positive/Negative/Neutral Scores**: These show the proportion of the text that falls into each category (sum to 1).
        """)

st.markdown("---")
st.markdown("Made by Ravi Ashray")
