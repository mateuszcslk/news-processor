import news_sources
import headlines
import constants


def run():
    ns = news_sources.NewsSources(api_url=constants.SOURCES_URL, physical_path=constants.NEWS_SOURCES_PATH, api_key=constants.API_KEY)
    ns.read()
    sources = ns.list_sources()

    h = headlines.Headlines(api_url=constants.HEADLINES_URL, physical_path=constants.HEADLINES_PATH, api_key=constants.API_KEY)
    h.collect(news_sources=sources, page_size=constants.RESULTS_PER_PAGE)
    h.save()


if __name__ == "__main__":
    run()