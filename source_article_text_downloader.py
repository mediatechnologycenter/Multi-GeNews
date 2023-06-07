import re
from typing import List, Dict

import requests
import json


def write_jsonl(file_name: str, json_lines_content: List[Dict]):
    with open(file_name, 'w+') as file:
        for json_data in json_lines_content:
            json.dump(json_data, file, ensure_ascii=False)
            file.write("\n")


def read_jsonl(file_name: str) -> List[Dict]:
    json_lines_content = []
    with open(file_name, 'r') as file:
        for line in file:
            json_lines_content.append(json.loads(line))
    return json_lines_content


def add_space_between_letters_with_punctuation(text: str):
    cleaned_text = re.sub(r'(?<=[^\d\W])[.:](?=[^\d\W])', r'\g<0> ', text)
    return cleaned_text


def get_article_text(url):
    search_url = url + "/search"

    response = requests.get(search_url)

    # Ensure we got a successful response
    if response.status_code != 200:
        print(f"Failed to get data from {search_url}, status code: {response.status_code}")
        return None

    data = response.json()

    paragraphs = data.get('paragraphs', [])

    text = add_space_between_letters_with_punctuation('\n'.join(paragraphs))

    return text


def set_source_article_texts(dataset_json_lines: List[Dict]):
    for cluster in dataset_json_lines:
        articles = cluster['articles']
        for article in articles:
            url = article['article_link']
            text = get_article_text(url)
            if text is not None:
                # Replace the existing text with the downloaded one
                article['text'] = text
            else:
                print(f"The url: {url} does not exist")


def main():
    dataset_dir = "Multi-GeNews.jsonl"
    dataset_json_lines = read_jsonl(file_name=dataset_dir)
    set_source_article_texts(dataset_json_lines=dataset_json_lines)

    out_dataset_dir = "Multi-GeNews-With-Text.jsonl"
    write_jsonl(file_name=out_dataset_dir, json_lines_content=dataset_json_lines)


if __name__ == '__main__':
    main()
