# AI2 Dolma Most Frequent Words: a derivative dataset of the most common words

_Published August 21, 2023 by [Zachary Levonian](https://www-users.cse.umn.edu/~levon003/)_

In August 2023, AI2 released [Dolma](https://huggingface.co/datasets/allenai/dolma), an open corpus for training large language models.
Read their [blog post](https://blog.allenai.org/dolma-3-trillion-tokens-open-llm-corpus-9a0ff4b8da64) to learn more.

The texts in Dolma come from six data sources.
This Streamlit app shows the 500 most frequent words in the three smallest sources: [peS2o](https://github.com/allenai/peS2o), [Project Gutenberg](https://www.gutenberg.org/), and Wikipedia.

Dolma was released under an interesting license: the [AI2 ImpACT License for Medium Risk Artifacts](https://allenai.org/licenses/impact-mr).
This small dataset of word counts is a Data Derivative of Dolma:
it's "a new dataset that incorporates some or all of our data" (see the [license summary](https://allenai.org/impact-license)).

The ImpACT license includes use-based restrictions.
Briefly, you can't use this word list for a few purposes:
military weapons/surveillance,
law enforcement (including predictive or biometric identification systems),
disseminating information without a disclaimer the information is machine generated,
and "fully automated decision-making without a human in the loop".

AI2 call these "Flow Down Use-Based Restrictions":
"The Use-Based Restrictions should be included in an enforceable legal agreement for all downstream use and/or further distribution by your end users.
Our intent is for the Use-Based Restrictions to continue running downstream."
I'm not sure what that means for the license of this word count table, or which licenses are compatible with these flow-down restrictions.
(If you actually want to use these data for some reason, treat them as covered by the same AI2 ImpACT License for Medium Risk Artifacts and submit your contact info on [the HuggingFace dataset release](https://huggingface.co/datasets/allenai/dolma).)

### Derivative Impact Report

The ImpACT license also requires me to produce a Derivative Impact Report, which is an interesting concept based on [data cards](https://arxiv.org/abs/2204.01075).
I submitted this report to AI2 via a web form.

1. **Intended Use**: What is the intended use of the Derivative?

    A high-level overview for 3 of the 6 Dolma sources.

2. **Intended Users**: Who are the intended users of the Derivative?

    Any person interested in the most frequent words in peS2o, Project Gutenberg, or Wikipedia sources for Dolma.

3. **Funding**: What is the source of funding for the program, project, or initiative that developed the Derivative?

    No funding source.

4. **Dataset Sources & Modifications**: To develop the Data Derivative, what is the source of any data that was added to the original dataset and/or how was any data removed from the original dataset?

    Only data from the peS2o, Project Gutenberg, and Wikipedia sources was used.

5. **Dataset Size**: How many examples are included in the Data Derivative overall?

    1007 (top 500 most frequent words from each source)

### How did I count words?
I chose the fastest approach I could think of:
using `bash` for case-sensitive string counting after splitting on spaces and newlines.
Punctuation is removed (via `tr -d '[[:punct:]]'`).

I would not recommend this approach to segmentation or word identification.

You can compare the token counts reported in the Dolma data release to my word counts in the table below.
As expected, these word counts are lower as they exclude punctuation and many words are composed of multiple tokens.


|    | Source            |   GPT-NeoX Tokens (billions) | This word count (billions)   | Unique words (millions)   | % Hapaxes   |
|---:|:------------------|-----------------------------:|:-----------------------------|:--------------------------|:------------|
|  0 | peS2o             |                         57   | *                            | *                         | 23.2%       |
|  1 | Project Gutenberg |                          4.8 | 3.53                         | 14.3                      | 62.2%       |
|  2 | Wikipedia         |                          3.6 | 2.59                         | 12.9                      | 54.7%       |

*The word counts for the peS2o data are based on a random 500,000 documents (about 1% of the total, sampled using `shuf`'s reservoir sampling), so we can't compute full word counts or compare to the reported token counts.
(In the sample: 0.97 billion total words with 4.9 million unique words.)

## Most Frequent Words

See the markdown table below.

>
/notebook/
Name
Last Modified

Collate Word Counts
Selection deleted
from pathlib import Path

import pandas as pd
data_dir = Path("../data")
assert data_dir.exists()
dfs = []
for source, fname in zip(
    ["Wikipedia", "Project Gutenberg", "peS2o"],
    ["wiki_word_counts.csv", "books_word_counts.csv", "s2_word_counts.csv"],
):
    df = pd.read_csv(
        data_dir / "derived" / fname, header=None, names=["count", "word"], dtype={"count": int, "word": str}
    )
    df["source"] = source
    dfs.append(df)
len(dfs)

3

dfs[2].head(10)
	count 	word 	source
0 	13104 	Response 	peS2o
1 	36987140 	of 	peS2o
2 	89 	jujube 	peS2o
3 	18527 	fruits 	peS2o
4 	19039849 	to 	peS2o
5 	18057 	exogenous 	peS2o
6 	962 	oxalic 	peS2o
7 	249218 	acid 	peS2o
8 	686752 	treatment 	peS2o
9 	700098 	based 	peS2o
top_n = 1000
top_dfs = []
for df in dfs:
    df = df.sort_values(by="count", ascending=False)
    df = df[(df["word"] != "") & (df["word"].notna())]
    total_words = df["count"].sum()
    source = df["source"].iloc[0]
    print(f"{source} total words: {total_words}")
    print(f"{source} unique words: {len(df)}")
    print(f"{source} % hapaxes: {(df['count'] == 1).sum() / len(df):.1%}")
    df = df.head(1000000).copy()
    df = df.reset_index(drop=True)
    df["rank"] = df.index + 1
    df["pct"] = df["count"] / total_words
    top_word_count = df["count"].iloc[0]
    df["zipf"] = df["count"] / top_word_count
    top_dfs.append(df)
len(top_dfs)

Wikipedia total words: 2569550145
Wikipedia unique words: 12931993
Wikipedia % hapaxes: 54.7%
Project Gutenberg total words: 3174282374
Project Gutenberg unique words: 14325897
Project Gutenberg % hapaxes: 62.2%
peS2o total words: 971899439
peS2o unique words: 4915017
peS2o % hapaxes: 23.2%

3

metadata_df = pd.DataFrame(
    {
        "Source": ["peS2o", "Project Gutenberg", "Wikipedia"],
        "GPT-NeoX Tokens (billions)": ["57", "4.8", "3.6"],
        "This word count (billions)": ["-", "3.53", "2.59"],
        "Unique words (millions)": ["-", "14.3", "12.9"],
        "% Hapaxes": ["23.2%", "62.2%", "54.7%"],
    }
)
metadata_df
	Source 	GPT-NeoX Tokens (billions) 	This word count (billions) 	Unique words (millions) 	% Hapaxes
0 	peS2o 	57 	- 	- 	23.2%
1 	Project Gutenberg 	4.8 	3.53 	14.3 	62.2%
2 	Wikipedia 	3.6 	2.59 	12.9 	54.7%
print(metadata_df.to_markdown())

|    | Source            |   GPT-NeoX Tokens (billions) | This word count (billions)   | Unique words (millions)   | % Hapaxes   |
|---:|:------------------|-----------------------------:|:-----------------------------|:--------------------------|:------------|
|  0 | peS2o             |                         57   | -                            | -                         | 23.2%       |
|  1 | Project Gutenberg |                          4.8 | 3.53                         | 14.3                      | 62.2%       |
|  2 | Wikipedia         |                          3.6 | 2.59                         | 12.9                      | 54.7%       |

top_dfs[2].head(10)
	count 	word 	source 	rank 	pct 	zipf
0 	57425445 	the 	peS2o 	1 	0.059086 	1.000000
1 	36987140 	of 	peS2o 	2 	0.038057 	0.644090
2 	28712503 	and 	peS2o 	3 	0.029543 	0.499996
3 	20797356 	in 	peS2o 	4 	0.021399 	0.362163
4 	19039849 	to 	peS2o 	5 	0.019590 	0.331558
5 	15170079 	a 	peS2o 	6 	0.015609 	0.264170
6 	11925900 	is 	peS2o 	7 	0.012271 	0.207676
7 	9286966 	for 	peS2o 	8 	0.009555 	0.161722
8 	8947168 	with 	peS2o 	9 	0.009206 	0.155805
9 	8560627 	that 	peS2o 	10 	0.008808 	0.149074
top_n = 500
cols = ["word", "pct", "rank"]
mdf = pd.merge(
    pd.merge(top_dfs[0][cols], top_dfs[1][cols], how="outer", on="word", suffixes=("_wiki", "_gutenberg")),
    top_dfs[2][cols].rename(columns={"pct": "pct_s2", "rank": "rank_s2"}),
    how="outer",
    on="word",
)  # .fillna("-")
mdf = mdf[(mdf.rank_wiki <= top_n) | (mdf.rank_gutenberg <= top_n) | (mdf.rank_s2 <= top_n)].copy()

mdf["Mean Rank"] = mdf[["rank_wiki", "rank_gutenberg", "rank_s2"]].fillna(1000001).mean(axis=1)
# mdf["Mean Rank"] = mdf["Mean Rank"].map(lambda v: f"{v:.2f}")

for column in mdf.columns:
    # if column.startswith("pct"):
    #    mdf[column] = mdf[column].map(lambda v: (f"{v:.5f}" if pd.notna(v) else "-")
    if column.startswith("rank"):
        mdf[column] = mdf[column].map(lambda v: int(v) if pd.notna(v) else 1001)

mdf = mdf[["word", "Mean Rank", "rank_s2", "pct_s2", "rank_gutenberg", "pct_gutenberg", "rank_wiki", "pct_wiki"]]


def pretty_col_name(column):
    name, source = column.split("_")
    if name == "pct":
        name = "P(w)"
    elif name == "rank":
        name = "Rank"
    if source == "wiki":
        source = "Wikipedia"
    elif source == "gutenberg":
        source = "Gutenberg"
    elif source == "s2":
        source = "peS2o"
    return f"{source} {name}"


mdf = mdf.rename(
    columns={column: pretty_col_name(column) if "_" in column else column for column in mdf.columns}
).rename(
    columns={
        "word": "Word",
    }
)
mdf = mdf.sort_values(by=["Mean Rank", "Wikipedia Rank", "Gutenberg Rank"], ascending=True).reset_index(drop=True)
mdf  # .head(20)
	Word 	Mean Rank 	peS2o Rank 	peS2o P(w) 	Gutenberg Rank 	Gutenberg P(w) 	Wikipedia Rank 	Wikipedia P(w)
0 	the 	1.000000 	1 	5.908579e-02 	1 	6.033402e-02 	1 	6.253678e-02
1 	of 	2.000000 	2 	3.805655e-02 	2 	3.578621e-02 	2 	3.411199e-02
2 	and 	3.000000 	3 	2.954267e-02 	3 	3.036963e-02 	3 	2.959591e-02
3 	in 	4.666667 	4 	2.139867e-02 	6 	1.718741e-02 	4 	2.559779e-02
4 	to 	4.666667 	5 	1.959035e-02 	4 	2.574570e-02 	5 	2.075563e-02
... 	... 	... 	... 	... 	... 	... 	... 	...
1002 	sir 	55374.333333 	116162 	1.471346e-07 	493 	1.887995e-04 	49468 	7.561635e-07
1003 	algorithm 	73239.666667 	388 	2.777036e-04 	213391 	4.189923e-08 	5940 	1.669281e-05
1004 	µ 	92365.666667 	494 	2.255655e-04 	79771 	2.249327e-07 	196832 	8.561810e-08
1005 	CHAPTER 	99115.666667 	96237 	1.954935e-07 	473 	1.975420e-04 	200637 	8.328306e-08
1006 	amp 	113960.333333 	65617 	3.529172e-07 	276029 	2.772280e-08 	235 	3.450853e-04

1007 rows × 8 columns
mdf.head(20)
	Word 	Mean Rank 	peS2o Rank 	peS2o P(w) 	Gutenberg Rank 	Gutenberg P(w) 	Wikipedia Rank 	Wikipedia P(w)
0 	the 	1.000000 	1 	0.059086 	1 	0.060334 	1 	0.062537
1 	of 	2.000000 	2 	0.038057 	2 	0.035786 	2 	0.034112
2 	and 	3.000000 	3 	0.029543 	3 	0.030370 	3 	0.029596
3 	in 	4.666667 	4 	0.021399 	6 	0.017187 	4 	0.025598
4 	to 	4.666667 	5 	0.019590 	4 	0.025746 	5 	0.020756
5 	a 	5.666667 	6 	0.015609 	5 	0.019530 	6 	0.020071
6 	is 	9.000000 	7 	0.012271 	11 	0.008102 	9 	0.009507
7 	was 	9.666667 	14 	0.005832 	8 	0.010475 	7 	0.012864
8 	that 	10.666667 	10 	0.008808 	7 	0.011018 	15 	0.005861
9 	for 	11.333333 	8 	0.009555 	16 	0.007056 	10 	0.008299
10 	with 	12.000000 	9 	0.009206 	14 	0.007531 	13 	0.007172
11 	The 	12.666667 	11 	0.007853 	19 	0.005483 	8 	0.010317
12 	as 	12.666667 	12 	0.006359 	15 	0.007149 	11 	0.007882
13 	on 	16.333333 	16 	0.005263 	21 	0.005388 	12 	0.007589
14 	by 	16.333333 	13 	0.006314 	22 	0.005273 	14 	0.006971
15 	at 	20.000000 	21 	0.003628 	23 	0.005201 	16 	0.005244
16 	be 	21.000000 	18 	0.004954 	18 	0.005717 	27 	0.002538
17 	from 	21.333333 	19 	0.004330 	28 	0.004245 	17 	0.005202
18 	were 	23.333333 	17 	0.004999 	31 	0.003648 	22 	0.003330
19 	it 	23.333333 	32 	0.002146 	13 	0.007974 	25 	0.002848
mdf.to_csv("../src/resources/top_words.csv", index=False)
Selection deleted
print(mdf.head(20).to_markdown())

|    | Word   |   Mean Rank |   peS2o Rank |   peS2o P(w) |   Gutenberg Rank |   Gutenberg P(w) |   Wikipedia Rank |   Wikipedia P(w) |
|---:|:-------|------------:|-------------:|-------------:|-----------------:|-----------------:|-----------------:|-----------------:|
|  0 | the    |     1       |            1 |   0.0590858  |                1 |       0.060334   |                1 |       0.0625368  |
|  1 | of     |     2       |            2 |   0.0380566  |                2 |       0.0357862  |                2 |       0.034112   |
|  2 | and    |     3       |            3 |   0.0295427  |                3 |       0.0303696  |                3 |       0.0295959  |
|  3 | in     |     4.66667 |            4 |   0.0213987  |                6 |       0.0171874  |                4 |       0.0255978  |
|  4 | to     |     4.66667 |            5 |   0.0195903  |                4 |       0.0257457  |                5 |       0.0207556  |
|  5 | a      |     5.66667 |            6 |   0.0156087  |                5 |       0.0195295  |                6 |       0.0200714  |
|  6 | is     |     9       |            7 |   0.0122707  |               11 |       0.00810247 |                9 |       0.0095068  |
|  7 | was    |     9.66667 |           14 |   0.00583241 |                8 |       0.0104745  |                7 |       0.0128642  |
|  8 | that   |    10.6667  |           10 |   0.00880814 |                7 |       0.0110184  |               15 |       0.00586098 |
|  9 | for    |    11.3333  |            8 |   0.00955548 |               16 |       0.00705593 |               10 |       0.00829891 |
| 10 | with   |    12       |            9 |   0.00920586 |               14 |       0.00753056 |               13 |       0.00717199 |
| 11 | The    |    12.6667  |           11 |   0.00785279 |               19 |       0.0054833  |                8 |       0.0103172  |
| 12 | as     |    12.6667  |           12 |   0.00635921 |               15 |       0.00714859 |               11 |       0.00788162 |
| 13 | on     |    16.3333  |           16 |   0.00526325 |               21 |       0.00538805 |               12 |       0.00758886 |
| 14 | by     |    16.3333  |           13 |   0.00631448 |               22 |       0.00527338 |               14 |       0.00697149 |
| 15 | at     |    20       |           21 |   0.003628   |               23 |       0.0052012  |               16 |       0.00524444 |
| 16 | be     |    21       |           18 |   0.00495423 |               18 |       0.00571736 |               27 |       0.00253783 |
| 17 | from   |    21.3333  |           19 |   0.00433035 |               28 |       0.00424531 |               17 |       0.00520234 |
| 18 | were   |    23.3333  |           17 |   0.00499865 |               31 |       0.00364787 |               22 |       0.00333038 |
| 19 | it     |    23.3333  |           32 |   0.00214591 |               13 |       0.00797386 |               25 |       0.00284839 |

### Why did I make this word list?
This app was made by [Zachary Levonian](https://www-users.cse.umn.edu/~levon003/), a computer science researcher interested in making ML-powered systems useful and accessible.
I was primarily motivated by an interest in the ImpACT license, and I wanted to produce a quick Data Derivative.
I also think [word counts are underrated](https://twitter.com/dmimno/status/1094658594262401026):
a good way to quickly highlight the similarities and differences of the datasets that make up Dolma.

View the code for this Streamlit app [on GitHub](https://github.com/levon003/dolma-count-streamlit), including [the table as a CSV](https://github.com/levon003/dolma-count-streamlit/blob/main/src/resources/top_words.csv). Shout-outs to `gunzip` for being outrageously fast.

Under the terms of the license, I must include the following attribution notice:
Dolma is licensed under the AI2 ImpACT License for Medium Risk Artifacts, © 2023 The Allen Institute for Artificial Intelligence.
