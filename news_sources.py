import urllib.request, urllib.parse
import json
import pandas as pd
import constants
from typing import List


class NewsSources():
    def __init__(self, physical_path: str = constants.NEWS_SOURCES_PATH,
                 api_url: str = constants.SOURCES_URL,
                 api_key: str = constants.API_KEY):
        """Storing constants as params to make whole class unit-testable
        """
        self.physical_path = physical_path
        self.api_url = api_url
        self.api_key = api_key


    def collect(self, language_iso_code: str) -> pd.DataFrame:
        """Method collecting all news sources with of a specific language. Function assumes no paging (single call to the API returns all results)
        Args:
            - language_iso_code - two char iso code representing a language which news sources should be collected from
        """
        params = {"language": language_iso_code, "apiKey": self.api_key}
        news_url = self.api_url + "?" + urllib.parse.urlencode(params)

        with urllib.request.urlopen(url=news_url) as response:
            resp_json = json.loads(response.read())
            if resp_json["status"] == "ok":
                self.news_sources = pd.DataFrame(resp_json["sources"])
                return self.news_sources

            error = resp_json["message"]
            raise Exception(f"News API returned following error {error}")


    def save(self) -> None:
        """Method saving news sources to a physical location
        Args:
        """
        if self.news_sources is None:
            raise Exception("No news collected")

        self.news_sources.to_json(path_or_buf=self.physical_path)


    def read(self) -> pd.DataFrame:
        """Method loading news sources from a physical location
        Args:
        """
        self.news_sources = pd.read_json(path_or_buf=self.physical_path)
        return self.news_sources


    def list_sources(self) -> List[str]:
        """Method returning all identifiers of news sources as a list
        """
        return self.news_sources["id"].values.tolist()