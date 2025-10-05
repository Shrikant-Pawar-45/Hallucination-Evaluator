import re
import wikipediaapi

wiki = wikipediaapi.Wikipedia(
    user_agent="HallucinationEvaluator/1.0 (streamlit-app)",
    language="en"
)


def verify_factual(prompt: str, response: str) -> bool:
    """A simple verification by checking for keywords in the relevant Wikipedia summary.

    Returns True if the response shares a meaningful number of words with the most
    relevant Wikipedia page found for the prompt. This is a heuristic and should be
    treated as an approximate automated verifier only.
    """
    # A more robust regex to find potential subjects (nouns/proper nouns)
    words = re.findall(r"\b[A-Z][a-z]*\b(?:\s\b[A-Z][a-z]*\b)*|\b[a-zA-Z]{4,}\b", prompt)

    ignore_list = {"who", "what", "where", "when", "why", "how", "the", "is", "of", "in", "did", "was", "a", "an"}
    subjects = [w for w in words if w.lower() not in ignore_list]

    if not subjects:
        return False

    # Try subjects in order of appearance to find a valid Wikipedia page
    page = None
    for subject in subjects:
        p = wiki.page(subject)
        if p.exists():
            page = p
            break

    # Fallback: try simple lowercased single-word title from prompt
    if not page:
        tokens = re.findall(r"\b\w+\b", prompt)
        for t in tokens:
            p = wiki.page(t.lower())
            if p.exists():
                page = p
                break

    # Fallback: look for proper nouns in the response and try those as page titles
    if not page and response:
        proper_nouns = re.findall(r"\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b", response)
        for pn in proper_nouns:
            p = wiki.page(pn)
            if p.exists():
                page = p
                break

    if not page:
        return False

    summary = page.summary.lower()
    response_lower = response.lower()

    # Check if a significant portion of the response words are in the summary
    response_words = set(re.findall(r'\b\w+\b', response_lower))
    summary_words = set(re.findall(r'\b\w+\b', summary))
    common_words = response_words.intersection(summary_words)

    # Simple heuristic: if 2 or more common words exist, it's likely related.
    return len(common_words) >= 2
