from langdetect import detect, detect_langs
from apify import Actor

async def main():
    async with Actor:
        input_data = await Actor.get_input()
        raw_text = input_data.get("text", "")

        # Split into lines and clean
        texts = [line.strip() for line in raw_text.splitlines() if line.strip()]
        results = []

        for text in texts:
            try:
                best_guess = detect(text)
                all_guesses = detect_langs(text)
                results.append({
                    "text": text,
                    "language": best_guess,
                    "alternatives": [
                        {"lang": str(alt.lang), "probability": round(alt.prob, 6)}
                        for alt in all_guesses
                    ]
                })
            except Exception as e:
                results.append({
                    "text": text,
                    "error": str(e)
                })

        await Actor.set_value("OUTPUT", results)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
