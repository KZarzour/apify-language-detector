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
                confidence_map = detector.compute_language_confidence_values(text)
                top_language = max(confidence_map, key=confidence_map.get)
                confidence = round(confidence_map[top_language], 6)

                results.append({
                    "text": text,
                    "language": top_language.iso_code_639_1.name.lower(),
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
