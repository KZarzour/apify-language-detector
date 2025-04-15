from lingua import Language, LanguageDetectorBuilder
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
                confidences = detector.compute_language_confidence_values(text)

                if not confidences:
                    raise ValueError("Unable to detect language with confidence")

                best_language, confidence = max(confidences.items(), key=lambda x: x[1])

                results.append({
                    "text": text,
                    "language": best_language.iso_code_639_1.name.lower(),
                    "confidence": round(confidence, 6)
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
