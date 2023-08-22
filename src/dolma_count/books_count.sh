#!/bin/bash
gunzip -c data/raw/gutenberg-books/*.json.gz \
| cut -c 79- \
| sed 's/","version":"v."}$//' \
| sed 's/\\n/\n/g' \
| sed 's/\\"/"/g' \
| tr -d '[[:punct:]]' \
| tr ' ' '\n' \
| python src/dolma_count/count_utils.py > data/derived/books_word_counts.csv


#| ggrep -Po '"text":.*?[^\\]",' - \
#| cut -c 9- \
#| sed 's/",$//' \
