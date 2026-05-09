# NLP with Streamlit

Aplikacja webowa stworzona w Streamlit, wykorzystująca modele z platformy Hugging Face do przetwarzania języka naturalnego.

Aplikacja umożliwia:

- analizę wydźwięku emocjonalnego tekstu w języku angielskim,
- tłumaczenie tekstu z języka angielskiego na język niemiecki,
- obsługę komunikatów ładowania, sukcesu, ostrzeżeń oraz błędów.

## Technologie

Projekt został wykonany z użyciem:

- Python,
- Streamlit,
- Hugging Face Transformers,
- PyTorch,
- modelu `Helsinki-NLP/opus-mt-en-de` do tłumaczenia EN → DE,
- modelu `sentiment-analysis` do analizy wydźwięku tekstu.

## Funkcje aplikacji

### 1. Analiza wydźwięku emocjonalnego tekstu

Użytkownik wpisuje tekst w języku angielskim, a aplikacja określa, czy jego wydźwięk jest pozytywny czy negatywny. Wynik prezentowany jest razem z poziomem pewności modelu.

### 2. Tłumaczenie tekstu EN → DE

Użytkownik wpisuje tekst w języku angielskim, a aplikacja tłumaczy go na język niemiecki przy użyciu modelu Hugging Face.

## Uruchomienie online
[streamlit.app](https://s29267.streamlit.app/)

## Instalacja i uruchomienie lokalne

1. Sklonuj repozytorium:
```bash
git clone https://github.com/XSzymon11/nlp-with-streamlit.git
```

2. Przejdź do folderu projektu:
```bash
cd nlp-with-streamlit
```

3. Zainstaluj wymagane biblioteki:
``` bash
pip install -r requirements.txt
```

4. Uruchom aplikację Streamlit:
```bash
streamlit run streamlit_app.py
```

Po uruchomieniu aplikacja powinna otworzyć się w przeglądarce. Jeśli nie otworzy się automatycznie, skopiuj adres z terminala, najczęściej:
```http://localhost:8501```

