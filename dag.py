import step_collect_news_sources
import step_collect_headlines
import step_push_to_s3

if __name__ == "__main__":
    step_collect_news_sources.run()
    step_collect_headlines.run()
    step_push_to_s3.run()