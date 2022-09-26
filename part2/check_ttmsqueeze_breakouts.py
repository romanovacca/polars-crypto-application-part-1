import os
import time
from typing import List

from part2.src.indicators.ttm_squeeze import TTMSqueeze
from part2.src.utils.dataloader import DataLoader
from part2.src.utils.helpers import logger

logger = logger("main")


def run_indicator_for_all_files(
    path: str, intervals: List, squeeze_indicator: TTMSqueeze
):
    breakouts = []
    dataloader = DataLoader()

    start_time = time.time()
    for file in os.listdir(path):
        if file.endswith(".csv"):
            breakout = squeeze_indicator.run(
                path=path, file=file, intervals=intervals, dataloader=dataloader
            )
            if breakout:
                breakouts.append(breakout)
    print("whole loop --- %s seconds ---" % (time.time() - start_time))

    return breakouts


def main():
    logger.info("Started main.")

    ttm_squeeze = TTMSqueeze(window=20)
    breakouts = run_indicator_for_all_files(
        path="/Users/romanovacca/Documents/Coding/git_projects/polars-crypto-application-part-1/part-1/data/USDT/",
        intervals=["1d", "2d"],
        squeeze_indicator=ttm_squeeze,
    )

    for breakout in breakouts:
        print(breakout)


if __name__ == "__main__":
    main()
