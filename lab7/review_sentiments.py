from nltk.sentiment.vader import SentimentIntensityAnalyzer
import text2emotion as te


def get_sentiment(analyzer: SentimentIntensityAnalyzer, text: str) -> dict[str, float]:
    return analyzer.polarity_scores(text)


def main() -> None:
    # 2a
    with open("hotel_reviews.txt", "r") as file:
        reviews = [review.strip().lower() for review in file.readlines()]
    
    # b
    analyzer = SentimentIntensityAnalyzer()
    for review in reviews:
        print(get_sentiment(analyzer, review))
    
    # c
    for review in reviews:
        print(te.get_emotion(review))

    # d
    # w przypadku sentiment analyzera wyniki mniej więcej jak oczekiwane. Pozytywna opinia trochę za mocno pozytywna 
    # (była prawie maksymalna a łatwo sobie wyobrazić jeszcze większy entuzjazm), a negatywna może troszkę za mało. Ale generalnie w porządku.
    # text2emotion generalnie zawiódł (w ogóle paczka wydaje się nie maintainowana) bo w obu przypadkach zdecydowanie najsilniejszą emocją jest
    # strach, a pozytywna ma wyższy wynik smutku niż negatywna.


if __name__ == "__main__":
    main()