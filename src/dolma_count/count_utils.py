import sys
from collections import defaultdict

from tqdm import tqdm


def stream_count_words():
    word_counts = defaultdict(int)
    for line in tqdm(sys.stdin, desc="Counting words"):
        word_counts[line.strip()] += 1
    for word, count in word_counts.items():
        print(str(count) + ',"' + word + '"')


def main():
    stream_count_words()


if __name__ == "__main__":
    main()
