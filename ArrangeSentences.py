import re

# Read the file content
with open('ShortStory.txt', 'r') as file:
    content = file.read()

# Step 1: Remove any newlines and unnecessary spaces that may cause incorrect splits
content = content.replace('\n', ' ').strip()

# Step 2: Split the content into sentences carefully, but without splitting attributed parts like asked Jerrodd
# This will ensure we keep quoted text with the attribution part
sentences = re.split(r'(?<!["\'])\s*(?=[.!?])', content)

# Step 3: Remove hyphen separators (------------------------------------------------) from the sentences list
sentences = [sentence for sentence in sentences if sentence != '------------------------------------------------']

# Function to clean sentences by removing leading/trailing punctuation and spaces
def clean_sentence(sentence):
    # Remove punctuation marks at the start and end of the sentence
    return re.sub(r'^[^\w]+|[^\w]+$', '', sentence).strip()

# Clean all sentences by removing punctuation and spaces at the beginning and end
sentences = [clean_sentence(sentence) for sentence in sentences]

# Function to handle sentences with quotation marks and continuation after quotes
def handle_quoted_sentences(sentences):
    quoted_sentences = []
    for i, sentence in enumerate(sentences):
        # Check if current sentence starts with lowercase and is a continuation of the previous sentence
        if i > 0:
            # Check if the current sentence starts with a lowercase letter and if the previous sentence ends with a quote
            if sentence[0].islower() and sentences[i-1].endswith('"'):
                # Combine the current sentence with the previous one
                sentences[i-1] = sentences[i-1][:-1] + ' ' + sentence.strip()  # Remove the ending quote from the previous sentence and merge
                continue
        # Otherwise, add the sentence as it is
        quoted_sentences.append(sentences[i])
    return quoted_sentences

# Handle sentences inside quotation marks and continuations after a quote
sentences = handle_quoted_sentences(sentences)

# Step 4: Sort the sentences alphabetically
sorted_sentences = sorted(sentences, key=lambda s: re.sub(r"^[^a-zA-Z0-9]+", "", s).lower())

# Step 5: Write the sorted sentences to a new file
with open('Sorted_Story.txt', 'w') as file:
    file.write('\n'.join(sorted_sentences))

print("The sentences have been sorted and written to 'Sorted_Story.txt'.")
