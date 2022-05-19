import news_sources
import headlines
import constants


def run():
    ns = news_sources.NewsSources()
    ns.read()
    sources = ns.list_sources()

    h = headlines.Headlines()
    h.collect(news_sources=sources, page_size=constants.RESULTS_PER_PAGE)
    h.save()


if __name__ == "__main__":
    run()