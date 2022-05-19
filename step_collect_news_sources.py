import news_sources
import constants


def run():
    ns = news_sources.NewsSources()
    ns.collect(language_iso_code=constants.LANGUAGE)
    ns.save()


if __name__ == "__main__":
    run()