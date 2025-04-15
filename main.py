from lingua_language_detector import LanguageDetectorBuilder
from apify import Actor

async def main():
    # Initialize the language detector from Lingua
    detector = LanguageDetectorBuilder.from_languages().build()

    async with Actor:
        input_data = await Actor.get_input()
        raw_text = input_data.get("text", "")

        # Split into lines and clean
        texts = [line.strip() for line in raw_text.splitlines() if line.strip()]
        results = []

        for text in texts:
            try:
                # Detect the language using Lingua
                lang = detector.detect_language_of(text)
                
                if lang:
                    # Get the language code and name
                    language = lang.name
                    # Get confidence score (Lingua gives a score between 0 and 1)
                    confidence = lang.probability
                    results.append({
                        "text": text,
                        "language": language,
                        "confidence": round(confidence, 6)
                    })
                else:
                    results.append({
                        "text": text,
                        "error": "Could not detect language"
                    })

            except Exception as e:
                results.append({
                    "text": text,
                    "error": str(e)
                })

        # Push results to Apify's dataset and set value
        await Actor.push_data(results)
        await Actor.set_value("OUTPUT", results)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
