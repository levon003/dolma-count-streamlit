#!/bin/bash
gunzip -c data/raw/wiki-en-simple/*.json.gz \
| ggrep -Po '"text":.*?[^\\]",' - \
| cut -c 9- \
| sed 's/",$//' \
| sed 's/\\n/\n/g' \
| sed 's/\\"/"/g' \
| tr -d '[[:punct:]]' \
| tr ' ' '\n' \
| python src/dolma_count/count_utils.py > data/derived/wiki_word_counts.csv
