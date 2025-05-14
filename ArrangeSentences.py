import re

# Read file
with open('ShortStory.txt', 'r') as f:
    content = f.read()

# collapse all whitespace (including newlines) into single spaces
content = re.sub(r'\s+', ' ', content).strip()

# remove any divider lines of hyphens
content = re.sub(r'-{2,}', ' ', content)

# Use findall to grab each sentence up to an end-of-sentence boundary,
# including any trailing quotes, but only if the next chunk really is
# a new sentence (whitespace + optional quote + uppercase) or end of text.
pattern = r'''
    .*?                  # minimally match up to…
    [\.!?]               # a sentence-ending ., ! or ?
    (?:["'])*            # —plus any trailing quotes—
    (?=                  # but only if what follows is…
       \s+["']?[A-Z]     #   whitespace + optional opening quote + uppercase
     | $                 # or end of text
    )
'''
sentences = re.findall(pattern, content, flags=re.X)

# Clean each sentence (trim stray punctuation/spaces but preserve quotes)
def clean_sentence(s):
    return re.sub(r'^[^\w"’‘]+|[^\w"’‘]+$', '', s).strip()

sentences = [clean_sentence(s) for s in sentences if s.strip()]

# Sort alphabetically (ignoring any leading non-alphanumerics for ordering)
sorted_sents = sorted(
    sentences,
    key=lambda s: re.sub(r'^[^A-Za-z0-9]+', '', s).lower()
)

# 5) Get sorted file with a sentence on each line
with open('SortedStory.txt', 'w') as f:
    f.write('\n'.join(sorted_sents))
