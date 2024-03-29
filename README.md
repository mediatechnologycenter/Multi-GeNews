# Multi-GeNews
<img src="images/logo.png" alt="image" width="300" height="auto">  <br/>
Due to the lack of German multi-document summarization data,
we have created a new mds dataset called 'Multi-GeNews'. This dataset contains news articles
sourced from the news portal of SRF, a Swiss media company. The included articles span from January to March 2020.\
The dataset includes hyperlinks directing to the webpages of the original source articles. We provide a Python script
named ```source_article_text_downloader.py```, which downloads the textual data from these linked webpages. The script
also automatically integrates this downloaded text into the existing dataset.

- The dataset can be found under:```Multi-GeNews.jsonl```.
- Each line of the jsonl file corresponds to a single cluster with the following json format:
  ```json
  {
    "articles": [
      {
        "title": "Title of Article 1",
        "text": "Text of Article 1",
        "article_link": "Link to Article 1"
      },
      {
        "title": "Title of Article 2",
        "text": "Text of Article 2",
        "article_link": "Link to Article 2"
      },
      ...
    ],
    "summary": "Summary of the cluster"
  }
  ```

## Installation

1. Clone this repository to your local machine.
2. Install requirements:

```
pip install requirements.txt
```

## Downloading Source Articles

1. Run:

```
python3 source_article_text_downloader.py
```

2. The command will take some time to download all the data. At the end, a file called ```Multi-GeNews-With-Text.jsonl``` will be created, containing the downloaded
   source articles.

## Reference

When using the Multi-GeNews dataset, please cite:

```bibtex
@inproceedings{mascarell-etal-2023-entropy,
    title = "Entropy-based Sampling for Abstractive Multi-document Summarization in Low-resource Settings.",
    author = {Mascarell, Laura and Chalumattu, Ribin and Heitmann, Julien},
    booktitle = "Proceedings of the 16th International Conference on Natural Language Generation",
    month = sep,
    year = "2023",
    address = "Prague, Czech Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://doi.org/10.3929/ethz-b-000624074"
}
```