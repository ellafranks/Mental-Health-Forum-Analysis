from reddit.scrape import RedditCollector
import datetime as dt


def execute(subreddit, output_path, start_date, end_date):
    RedditCollector(subreddit=subreddit,
                    output_path=output_path,
                    start_date=start_date,
                    end_date=end_date).write()


if __name__ == '__main__':
    SUBREDDIT = 'SuicideWatch'
    OUTPUT_PATH = '/Users/ella.franks/PycharmProjects/redditscrape/data/'
    START_DATE = dt.datetime(2019, 1, 30)
    END_DATE = dt.datetime(2020, 1, 30)

    execute(subreddit=SUBREDDIT,
            output_path=OUTPUT_PATH,
            start_date=START_DATE,
            end_date=END_DATE)
