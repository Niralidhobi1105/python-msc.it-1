import string

# Step 1: Get a paragraph from the user (This was missing)
paragraph = input("Enter a paragraph: ")

# Remove punctuation from the paragraph
for p in string.punctuation:
    paragraph = paragraph.replace(p, "")

# Split the paragraph into a list of words
words_list = paragraph.lower().split()

# Step 3: Calculate total number of words
total_words = len(words_list)

# Step 4: Calculate number of unique words (using set)
unique_words = set(words_list)
total_unique = len(unique_words)

# Step 5: Find the shortest and longest word(s)
if words_list:
    shortest_length = min(len(word) for word in words_list)
    shortest_words = [word for word in unique_words if len(word) == shortest_length]
    
    # Added logic to find the longest word(s)
    longest_length = max(len(word) for word in words_list)
    longest_words = [word for word in unique_words if len(word) == longest_length]
else:
    shortest_words = []
    longest_words = []

# Step 6: Find words appearing only once
word_counts = {}
for word in words_list:
    word_counts[word] = word_counts.get(word, 0) + 1

once_appearing = [word for word, count in word_counts.items() if count == 1]

# Step 7: Display words in alphabetical order
alphabetical_words = sorted(unique_words)

# --- DISPLAY RESULTS ---
print("\n--- ANALYSIS RESULTS ---")
print(f"Total number of words: {total_words}")
print(f"Number of unique words: {total_unique}")
print(f"Longest word(s): {longest_words}")  # Now this variable exists!
print(f"Shortest word(s): {shortest_words}")
print(f"Words appearing only once: {once_appearing}")
print(f"All unique words in alphabetical order: {alphabetical_words}")

# Step 8: Allow the user to search for a word and find its positions
search_word = input("\nEnter a word to search for its positions: ").lower().strip()

positions = []
for index, word in enumerate(words_list):
    if word == search_word:
        # We use index + 1 so human counting starts at 1 instead of 0
        positions.append(index + 1)

if positions:
    print(f"The word '{search_word}' was found at position(s): {positions}")
else:
    print(f"The word '{search_word}' is not present in the paragraph.")
