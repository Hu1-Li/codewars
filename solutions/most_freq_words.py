# coding=utf-8
def top_3_words(text: str):
    import re
    from collections import Counter

    pattern = r"[^a-zA-Z']+"
    words = re.split(pattern, text.lower())
    words = [word.strip() for word in words]
    words = [word for word in words if len(word) > 0 and any(c.isalpha() for c in word)]
    if not words:
        return []
    else:
        c = Counter(words)
        return [w for w, _ in c.most_common(min(len(c), 3))]
