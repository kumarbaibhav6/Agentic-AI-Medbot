import wikipedia

def fetch_wikipedia_summary(query: str) -> str:
    try:
        summary = wikipedia.summary(query, sentences=5)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple topics found: {e.options[:3]}"
    except wikipedia.exceptions.PageError:
        return "No information found on Wikipedia."
