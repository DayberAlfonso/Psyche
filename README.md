# Psyche

A small **Dash** web app that performs **sentiment analysis** on user-entered text using **TextBlob** and displays the result in a simple UI.

## What’s implemented so far

- **Sentiment analysis** via `TextBlob(text).sentiment.polarity`
  - Polarity \(> 0\) → Positive
  - Polarity \(< 0\) → Negative
  - Polarity \(= 0\) → Neutral
- **Dash UI**
  - Text area input + “Analyze Sentiment” button
  - Result panel updated via Dash callback
  - Basic styling using `dash-bootstrap-components` (Bootstrap theme)

## Requirements

- **Python**: `>=3.14` (per `pyproject.toml`)
- **Dependencies**: managed via `pyproject.toml` / `uv.lock`

## Setup

### Option A: Using `uv` (recommended)

```bash
uv sync
```

### Option B: Using `pip`

If you’re not using `uv`, install dependencies from `pyproject.toml` manually (or export a requirements file).

## Run the app

From the project root:

```bash
python src/main.py
```

This starts the Dash dev server (with `debug=True`). The console output will show the local URL to open in your browser.

## Project structure

```text
src/
  main.py              # App entry point (runs Dash server)
  api/
    sentiment.py       # analyze_sentiment(text) using TextBlob
  ui/
    app.py             # Dash app factory + app instance
    layout.py          # create_layout() -> UI layout
    callbacks.py       # register_callbacks(app) -> interactivity
```

## Key modules

- **Sentiment function**: `src/api/sentiment.py`
  - `analyze_sentiment(text) -> "Positive" | "Negative" | "Neutral"`
- **Dash entry point**: `src/main.py`
  - Imports the created Dash `app` and runs `app.run(debug=True)`

## Notes / current limitations

- The model is **rule-based** (TextBlob polarity), not a trained classifier.
- Output is currently a **3-class label** (Positive/Negative/Neutral); no score is shown yet.
- No tests/CI are included yet.