from langdetect import detect, detect_langs
from apify import Actor

async def main():
    async with Actor:
        input_data = await Actor.get_input()
        raw_text = input_data.get("text", "")

        # Split input into lines and clean
        texts = [line.strip() for line in raw_text.splitlines() if line.strip()]
        results = []

        for text in texts:
            try:
                # Detect the language
                best_guess = detect(text)
                # Get all language guesses with probabilities
                all_guesses = detect_langs(text)
                results.append({
                    "text": text,
                    "language": best_guess,
                    "confidence": round(all_guesses[0].prob, 6) if all_guesses else None
                })
            except Exception as e:
                results.append({
                    "text": text,
                    "error": str(e)
                })

        await Actor.push_data(results)
        await Actor.set_value("OUTPUT", results)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
