from lingua import LanguageDetectorBuilder
from apify import Actor

async def main():
    async with Actor:
        input_data = await Actor.get_input()
        raw_text = input_data.get("text", "")

        texts = [line.strip() for line in raw_text.splitlines() if line.strip()]
        results = []

        detector = LanguageDetectorBuilder.from_all_languages().build()

        for text in texts:
            try:
                confidence_values = detector.compute_language_confidence_values(text)

                if not confidence_values:
                    raise ValueError("Unable to detect language with confidence")

                best_lang, best_prob = confidence_values[0]

                results.append({
                    "text": text,
                    "language": best_lang.iso_code_639_1.name.lower(),
                    "confidence": round(best_prob, 6)
                })

            except Exception as e:
                results.append({
                    "text": text,
                    "error": str(e)
                })

        await Actor.push_data(results)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
