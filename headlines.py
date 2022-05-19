import urllib.request, urllib.parse
import json, os
import pandas as pd
import constants, utils
from typing import List, Dict


class Headlines():
    def __init__(self, physical_path: str = constants.HEADLINES_PATH,
                 api_url: str = constants.HEADLINES_URL, api_key: str = constants.API_KEY):
        """Storing constants as params to make whole class unit-testable
        """
        self.physical_path = physical_path
        self.api_url = api_url
        self.api_key = api_key
        self.headlines = None


    def collect(self, news_sources: List[str], page_size: int) -> pd.DataFrame:
        self.headlines = None
        params = {"sources": ",".join(news_sources),
                  "apiKey": self.api_key,
                  "pageSize": page_size}

        # To be improved - we should first get number of pages and distribute the API querying via ThreadPool.
        # For simplification purposes (not big amount of data), we are doing one-after-another approach.

        self._worker(url_params=params, page=1)

        # Flatten output
        flattened_source = pd.json_normalize(self.headlines.source).add_prefix("source_")
        self.headlines = pd.concat([flattened_source, self.headlines], axis="columns")
        self.headlines = self.headlines.drop(columns=["source"])

        return self.headlines


    def _worker(self, url_params: Dict[str, str], page: int):
        url_params["page"] = page

        headlines_url = self.api_url + "?" + urllib.parse.urlencode(url_params)

        with urllib.request.urlopen(url=headlines_url) as response:
            resp_json = json.loads(response.read())

            if resp_json["status"] == "error":
                error = resp_json["message"]
                raise Exception(f"News API returned following error {error}")

            res_df = pd.DataFrame(resp_json["articles"])

            if self.headlines is None:
                self.headlines = res_df
            else:
                self.headlines = self.headlines.concat(res_df)

            if resp_json["totalResults"] > page * url_params["pageSize"]:
                # self._worker(url_params=url_params, page=page+1)
                # More than 100 results are not allowed in free plan...
                pass


    def save(self) -> None:
        """Method saving headlines to a physical location
        Args:
        """
        if self.headlines is None:
            raise Exception("No headlines collected")

        filepath = os.path.join(self.physical_path, f"{utils.get_current_ts()}_headlines.csv")
        self.headlines.to_csv(path_or_buf=filepath, index=False)


    def list_files(self):
        return utils.abs_listdir(self.physical_path)