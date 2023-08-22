#!/bin/bash
# generate counts on a random 500,000 texts
gunzip -c data/raw/peS2o/s2_v3-*.json.gz \
| shuf -n 500000 \
| ggrep -Po '"text":.*?[^\\]",' - \
| cut -c 9- \
| sed 's/",$//' \
| sed 's/\\n/\n/g' \
| sed 's/\\"/"/g' \
| tr -d '[[:punct:]]' \
| tr ' ' '\n' \
| python src/dolma_count/count_utils.py > data/derived/s2_word_counts.csv
