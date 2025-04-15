from apify import Actor
from lingua import LanguageDetectorBuilder

async def main():
    async with Actor:
        input_data = await Actor.get_input()
        raw_text = input_data.get("text", "")

        texts = [line.strip() for line in raw_text.splitlines() if line.strip()]
        results = []

        detector = LanguageDetectorBuilder.from_all_languages().build()

        for text in texts:
            try:
                confidence_data = detector.compute_language_confidence_values(text)

                # Handle both possible types
                if isinstance(confidence_data, dict):
                    top_lang = max(confidence_data, key=confidence_data.get)
                    confidence = round(confidence_data[top_lang], 6)
                else:
                    top = max(confidence_data, key=lambda cv: cv.value)
                    top_lang = top.language
                    confidence = round(top.value, 6)

                results.append({
                    "text": text,
                    "language": top_lang.iso_code_639_1.name.lower(),
                    "confidence": confidence
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
