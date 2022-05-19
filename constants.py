import os


API_KEY = os.environ["NEWS_API_API_KEY"]

AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_BUCKET_NAME = "news-processor"

LANGUAGE = "en"
SOURCES_URL = "https://newsapi.org/v2/top-headlines/sources"
NEWS_SOURCES_PATH = os.path.join(os.getcwd(), "data/sources/sources.json")

HEADLINES_URL = "https://newsapi.org/v2/top-headlines"
HEADLINES_PATH = os.path.join(os.getcwd(), "data/headlines")
RESULTS_PER_PAGE = 100