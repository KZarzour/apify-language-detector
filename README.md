# Language Detector Actor

This actor detects the language of each line of text using machine learning techniques. It allows users to input multiple lines of text, with each line representing a separate text sample. The actor will return the detected language for each line, along with confidence scores and alternative language guesses.

## Features

- **Language Detection**: Automatically detects the language of each line of text.
- **Confidence Scores**: Provides the likelihood of the language detection for each guess.
- **Alternative Guesses**: In case the first guess isn't 100% accurate, it returns additional language options with probabilities.
- **Multi-line Support**: Accepts multiple text lines as input (one per line), with each line being processed individually.

## Input

- **Text**: Paste or enter multiple lines of text (one text sample per line). Each line will be processed separately to detect the language.

### Example Input

```
Hello, how are you?
Bonjour, comment ça va?
これは日本語です。
```

## Output

The actor will return the detected language for each line of text, along with alternative language guesses and their confidence scores.

### Example Output

```json
[
  {
    "text": "Hello, how are you?",
    "language": "en",
    "alternatives": [
      { "lang": "en", "probability": 0.99999 },
      { "lang": "fr", "probability": 0.00001 }
    ]
  },
  {
    "text": "Bonjour, comment ça va?",
    "language": "fr",
    "alternatives": [
      { "lang": "fr", "probability": 0.99997 },
      { "lang": "en", "probability": 0.00003 }
    ]
  },
  {
    "text": "これは日本語です。",
    "language": "ja",
    "alternatives": [
      { "lang": "ja", "probability": 0.99999 },
      { "lang": "zh", "probability": 0.00001 }
    ]
  }
]
```

## How It Works

1. **Input Processing**: Users input multiple lines of text (one line per text sample). Each line is parsed and passed to the language detection model.
2. **Language Detection**: The actor uses a **machine learning model** (Naive Bayes classifier) to detect the language based on n-gram patterns found in the input.
3. **Output**: For each line of text, the actor returns the detected language, along with the confidence score and alternative guesses.

## Deployment

This actor is deployed on Apify and can be used via the **Apify Console**. Once deployed, users can provide text as input and retrieve language detection results through the UI.

## Usage

1. Go to the Apify Console.
2. Run the actor with your text input.
3. Download the results or view them in the Apify UI.

## Limitations

- The actor is best suited for shorter texts, such as sentences or short paragraphs.
- Accuracy can vary with very short or ambiguous text inputs.
