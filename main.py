from langdetect import detect, detect_langs
from apify import Actor

async def main():
    async with Actor:
        input_data = await Actor.get_input()
        texts = input_data.get("texts", [])
        results = []

        for text in texts:
            try:
                best_guess = detect(text)
                all_guesses = detect_langs(text)
                results.append({
                    "text": text,
                    "language": best_guess,
                    "alternatives": [
                        {"lang": str(alt.lang), "prob": alt.prob}
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
