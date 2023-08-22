from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd
import streamlit as st


@st.cache_data
def get_top_words():
    data_filepath = Path(__file__).parent / "resources" / "top_words.csv"
    df = pd.read_csv(data_filepath)
    return df


st.set_page_config(page_title="AI2 Dolma Most Frequent Words", page_icon="🪨")
st.markdown(
    """# AI2 Dolma Most Frequent Words: a derivative dataset of the most common words

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
As expected, these word counts are lower as they exclude punctuation and many words are composed of multiple tokens.""",
)

metadata_df = pd.DataFrame(
    {
        "Source": ["peS2o", "Project Gutenberg", "Wikipedia"],
        "GPT-NeoX Tokens (billions)": ["57", "4.8", "3.6"],
        "This word count (billions)": ["*", "3.53", "2.59"],
        "Unique words (millions)": ["*", "14.3", "12.9"],
        "% Hapaxes": ["23.2%", "62.2%", "54.7%"],
    },
)
st.dataframe(
    metadata_df,
    use_container_width=True,
    hide_index=True,
)

st.markdown(
    """*The word counts for the peS2o data are based on a random 500,000 documents (about 1% of the total, sampled using `shuf`'s reservoir sampling), so we can't compute full word counts or compare to the reported token counts.
(In the sample: 0.97 billion total words with 4.9 million unique words.)

## Most Frequent Words

Sort the table by tapping on a column header.
Word ranks are tinted green if they are more common than the mean rank and pink if they are lesson common than the mean rank.
""",
)

df = get_top_words()
# style the dataframe
# I have no idea how the colormap code works
# see: https://matplotlib.org/stable/tutorials/colors/colormap-manipulation.html#creating-listed-colormaps
PiYG = matplotlib.pyplot.get_cmap("PiYG", 512)
newcmp = matplotlib.colors.ListedColormap(PiYG(np.linspace(0.3, 0.7, 256)))
styler = df.style.format(
    "{:.2f}",
    subset="Mean Rank",
)
for source in ["peS2o", "Gutenberg", "Wikipedia"]:
    gmap = df["Mean Rank"] - df[f"{source} Rank"]
    styler = styler.background_gradient(
        subset=f"{source} Rank",
        cmap=newcmp,
        gmap=gmap,
        vmin=-20,
        vmax=20,
    )

st.dataframe(
    styler,
    use_container_width=True,
    hide_index=True,
)

st.markdown(
    """### Why did I make this word list?
This app was made by [Zachary Levonian](https://www-users.cse.umn.edu/~levon003/), a computer science researcher interested in making ML-powered systems useful and accessible.
I was primarily motivated by an interest in the ImpACT license, and I wanted to produce a quick Data Derivative.
I also think [word counts are underrated](https://twitter.com/dmimno/status/1094658594262401026):
a good way to quickly highlight the similarities and differences of the datasets that make up Dolma.

View the code for this Streamlit app [on GitHub](https://github.com/levon003/dolma-count-streamlit), including [the table as a CSV](https://github.com/levon003/dolma-count-streamlit/blob/main/src/resources/top_words.csv). Shout-outs to `gunzip` for being outrageously fast.

Under the terms of the license, I must include the following attribution notice:
Dolma is licensed under the AI2 ImpACT License for Medium Risk Artifacts, © 2023 The Allen Institute for Artificial Intelligence.
""",
)
