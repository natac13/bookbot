
book_path = 'books/'
book_name = 'frankenstein.txt'

def main():
  content = getBookText()
  # print(content)

  word_count = count_words(content)
  char_count = count_each_char(content)

  print_report(word_count, char_count)


def getBookText():
  with open(book_path + book_name, 'r') as f:
      return f.read()
  
def count_words(content):
  return len(content.split())

def count_each_char(content):
  char_count = {}
  for char in content:
    normalized_char = char.lower()
    if normalized_char in char_count:
      char_count[normalized_char] += 1
    else:
      char_count[normalized_char] = 1
  return char_count

def print_report(word_count: int, char_counts: dict):
  print(f"--- Begin report of books/{book_name} ---")
  print(f"{word_count} words found in the document")
  print()

  char_counts = dict(sorted(char_counts.items(), key=lambda x: x[1], reverse=True))
  for char, count in char_counts.items():
    if char.isalpha():
      print(f"The '{char}' character was found {count} times")


  print(f"--- End report ---")

if __name__ == '__main__':
  main()

# --- Begin report of books/frankenstein.txt ---
# 77986 words found in the document

# The 'e' character was found 46043 times
# The 't' character was found 30365 times
# The 'a' character was found 26743 times
# The 'o' character was found 25225 times
# The 'i' character was found 24613 times
# The 'n' character was found 24367 times
# The 's' character was found 21155 times
# The 'r' character was found 20818 times
# The 'h' character was found 19725 times
# The 'd' character was found 16863 times
# The 'l' character was found 12739 times
# The 'm' character was found 10604 times
# The 'u' character was found 10407 times
# The 'c' character was found 9243 times
# The 'f' character was found 8731 times
# The 'y' character was found 7914 times
# The 'w' character was found 7638 times
# The 'p' character was found 6121 times
# The 'g' character was found 5974 times
# The 'b' character was found 5026 times
# The 'v' character was found 3833 times
# The 'k' character was found 1755 times
# The 'x' character was found 677 times
# The 'j' character was found 504 times
# The 'q' character was found 324 times
# The 'z' character was found 243 times
# --- End report ---
