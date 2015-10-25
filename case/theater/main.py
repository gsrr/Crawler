import os
import crawler
from parseplatform import upload_data


if __name__ == "__main__":
    crawler.main()
    upload_data.main("theater_thewall")
    upload_data.main("legacy")
    upload_data.main("indievox")

