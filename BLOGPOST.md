# AI2 Dolma Most Frequent Words: a derivative dataset of the most common words

_Published August 21, 2023 by [Zachary Levonian](https://www-users.cse.umn.edu/~levon003/). Best viewed [as a Streamlit app](https://dolma-count-levon003.streamlit.app/)._

In August 2023, AI2 released [Dolma](https://huggingface.co/datasets/allenai/dolma), an open corpus for training large language models.
Read their [blog post](https://blog.allenai.org/dolma-3-trillion-tokens-open-llm-corpus-9a0ff4b8da64) to learn more.

The texts in Dolma come from six data sources.
This blog post shows the most frequent words in the three smallest sources: [peS2o](https://github.com/allenai/peS2o), [Project Gutenberg](https://www.gutenberg.org/), and Wikipedia.

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
This blog post was made by [Zachary Levonian](https://www-users.cse.umn.edu/~levon003/), a computer science researcher interested in making ML-powered systems useful and accessible.
I was primarily motivated by an interest in the ImpACT license, and I wanted to produce a quick Data Derivative.
I also think [word counts are underrated](https://twitter.com/dmimno/status/1094658594262401026):
a good way to quickly highlight the similarities and differences of the datasets that make up Dolma.

View the code for this blog post and Streamlit app [on GitHub](https://github.com/levon003/dolma-count-streamlit), including [the full table as a CSV](https://github.com/levon003/dolma-count-streamlit/blob/main/src/resources/top_words.csv). Shout-outs to `gunzip` for being outrageously fast.

Under the terms of the license, I must include the following attribution notice:
Dolma is licensed under the AI2 ImpACT License for Medium Risk Artifacts, © 2023 The Allen Institute for Artificial Intelligence.
