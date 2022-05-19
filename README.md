# Intro
The aim of news-processor is to:
- Gather English news sources from News API
- For these sources - collect top headlines and save them as flat files
- Push saved files to Amazon S3 bucket

# How to run
- In order to run the application, execute dag.py file. This will trigger 3 steps to be run, in the respective order:
    - step_collect_news_sources.py
    - step_collect_headlines.py
    - step_push_to_s3.py

# Contents

- Pipeline files:
    - step_collect_news_sources.py - pipeline's step file aiming at collecting English news sources and saving them as a file
    - step_collect_headlines.py - step with a goal to load English news sources (saved in previous step) and to retrieve top headlines for these news sources, save as flat file with a name [timestamp]_headlines.csv 
    - step_push_to_s3.py - step responsible for uploading all available flat files with top headlines to Amazon S3 bucket
    - dag.py - file "orchestrating" the whole pipeline (just runs the steps in the order)
- Handlers:
    - news_sources.py - file holding a class responsible for handling all news sources connected operations (collecting from API, saving locally, reading from local)
    - headlines.py - file holding a class responsible for handling all top headlines related operations (collecting from API, saving locally, listing all local top headlines files)
    - s3.py - file holding a class responsible for S3 interaction (uploading files specified in parameter)
- Other:
    - constants.py - file holding all global configuration constants
    - utils.py - commonly used helper functions
    - requirements.txt - pip-compliant file with all require libraries to run the app

# Features
- Pipeline files and actual handlers are isolated
- Whole application is unit-testable - it is convenient to change API URLs / API keys etc., in order to use non-production versions of these (it is possible to add them as parameters for the classes - if not provided default production values from constants.py are used)
- Configuration file is a central point for constants storage
- All secret credentials are stored as environment variables, rather than being hardcoded

# Areas for improvement
- Orchestration - due to high overhead for the AirFlow Server setup, this has not been used in the project
- Fault-tolerance - as the application becomes more complex, fault-tolerance procedures must be implemented (like partial result saving, multithreading for API calls, caching etc.)