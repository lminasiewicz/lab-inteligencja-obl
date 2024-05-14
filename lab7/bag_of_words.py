import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
from wordcloud import WordCloud



def main() -> None:
    with open("article.txt", "r") as file:
        article = "".join([line.strip() for line in file.readlines()])
    # b
    article_tokenized = word_tokenize(article.lower())
    print(f"Length after tokenization: {len(article_tokenized)} words")

    # c / d
    article_filtered = [token for token in article_tokenized if token not in ["(", ")", "pp", "doi"] + stopwords.words("english")]
    print(f"Length after stopword removal: {len(article_filtered)} words")

    # e
    lemmatizer = WordNetLemmatizer()
    article_lemmatized = [lemmatizer.lemmatize(token) for token in article_filtered]
    print(f"Length after lemmatization: {len(article_lemmatized)} words")
    
    # f
    article_df = pd.DataFrame(article_lemmatized)
    print(article_df.value_counts()[:10])

    # g
    cloud = WordCloud(height=400, width=800, margin=10, )
    cloud = cloud.generate_from_text(".".join(article_lemmatized))
    cloud.to_file("wordcloud.jpg")



if __name__ == "__main__":
    main()