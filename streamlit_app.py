import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM


st.set_page_config(
    page_title="NLP with Streamlit",
    page_icon="🙄",
    layout="centered"
)


@st.cache_resource(show_spinner=False)
def load_sentiment_model():
    return pipeline("sentiment-analysis")


@st.cache_resource(show_spinner=False)
def load_translation_model():
    model_name = "Helsinki-NLP/opus-mt-en-de"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    return tokenizer, model


st.title('Tłumaczenie EN -> DE i Analiza Wydźwięku Emocjonalnego Tekstu w języku angielskim')

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    st.image(
        "https://huggingface.co/front/assets/huggingface_logo-noborder.svg",
        width=120,
    )

st.header('Przetwarzanie języka naturalnego')

st.info(
    """
    Ta część aplikacji wykorzystuje modele z platformy Hugging Face.
    
    Możesz wybrać jedną z dwóch opcji:
    
    1. Analizę wydźwięku emocjonalnego tekstu w języku angielskim.
    2. Tłumaczenie tekstu z języka angielskiego na język niemiecki.
    """
)

option = st.selectbox(
    "Opcje",
    [
        "Wydźwięk emocjonalny tekstu (eng)",
        "Tłumaczenie tekstu z angielskiego na niemiecki",
    ],
)


if option == "Wydźwięk emocjonalny tekstu (eng)":
    with st.form("sentiment_form"):
        text = st.text_area(label="Wpisz tekst w języku angielskim")
        submit = st.form_submit_button("Analizuj tekst")

    if submit:
        if not text.strip():
            st.warning("Najpierw wpisz tekst do analizy.")
        else:
            try:
                with st.spinner("Model analizuje wydźwięk tekstu..."):
                    classifier = load_sentiment_model()
                    answer = classifier(text)

                st.success("Analiza zakończona sukcesem.")

                label = answer[0]["label"]
                score = answer[0]["score"]

                if label == "POSITIVE":
                    label_pl = "Pozytywny"
                    emoji = "😇"
                else:
                    label_pl = "Negatywny"
                    emoji = "😈"

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        label="Wydźwięk tekstu",
                        value=f"{emoji} {label_pl}"
                    )

                with col2:
                    st.metric(
                        label="Pewność modelu",
                        value=f"{score:.2%}"
                    )

            except Exception as e:
                st.error("Wystąpił błąd podczas analizy tekstu.")
                st.write(e)


elif option == "Tłumaczenie tekstu z angielskiego na niemiecki":
    with st.form("translation_form"):
        text = st.text_area(label="Wpisz tekst w języku angielskim do przetłumaczenia")
        submit = st.form_submit_button("Przetłumacz tekst")

    if submit:
        if not text.strip():
            st.warning("Najpierw wpisz tekst do tłumaczenia.")
        else:
            try:
                with st.spinner("Trwa tłumaczenie tekstu z języka angielskiego na niemiecki..."):
                    tokenizer, model = load_translation_model()

                    inputs = tokenizer(
                        text,
                        return_tensors="pt",
                        padding=True,
                        truncation=True
                    )

                    translated = model.generate(**inputs, max_length=512)

                    translated_text = tokenizer.decode(
                        translated[0],
                        skip_special_tokens=True
                    )

                st.success("Tłumaczenie zakończone sukcesem.")

                st.markdown("### Tłumaczenie na język niemiecki")

                st.text_area(
                    label="Wynik tłumaczenia",
                    value=translated_text,
                    height=200,
                    disabled=True
                )

            except Exception as e:
                st.error("Wystąpił błąd podczas tłumaczenia tekstu.")
                st.write(e)

st.divider()

st.write("Autor: Szymon Prządak")
st.write("Numer indeksu: S29267")