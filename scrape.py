import snscrape.modules.twitter as twitterScraper

scraper = twitterScraper.TwitterUserScraper("RaymundRRR")

for i,tweet in enumerate(scraper.get_items()):
    print(f"{i} content: \n")