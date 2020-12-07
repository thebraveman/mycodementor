"""RSS feed reader in terminal

RSS feed reader in terminal

https://www.codementor.io/projects/rss-feed-reader-in-terminal-atx32jp82q

**Install & imports**
pip install feedparser

"""


import feedparser

def pureValue(v):
  if(not v):
    return ""
  else:
    return v.replace(';',' ').replace('  ',' ').replace("\r","").replace("\n",". ")

def getFileFromFeed(NewsFeed):
  print(pureValue(NewsFeed.feed.title),'-Number of RSS posts :', len(NewsFeed.entries))

  feedTitle = NewsFeed.feed.title
  fileName = feedTitle+".csv"
  f = open(fileName, "w")
  f.write("".join(("published",";","title",";","summary",";","link")))

  for entry in NewsFeed.entries: 
    published = entry.published
    title = pureValue(entry.title)
    summary = pureValue(entry.summary)
    link = entry.link

    f.write("\r\n")
    f.write("".join((published,";",title,";",summary,";",link)))
  f.close()
  return f



"""Use Case"""

ls = [
      'https://azurecomcdn.azureedge.net/en-us/blog/feed/',
      'https://feeds.npr.org/510312/podcast.xml',
      'https://cloudblog.withgoogle.com/products/gcp/rss/',
      'https://www.simoahava.com/index.xml',
      'https://www.analyticsmania.com/feed/',
      'http://feeds.feedburner.com/blogspot/tRaA?format=xml']

for url in ls:
  #Get the data from the feed 
  NewsFeed = feedparser.parse(url)

  #Writing result in csv file
  fileOfmMyFeed = getFileFromFeed(NewsFeed)



"""
    References :

*   [Python - Reading RSS feed](https://www.tutorialspoint.com/python_text_processing/python_reading_rss_feed.htm)
*   [Python File Write](https://www.w3schools.com/python/python_file_write.asp)
*   [codebeautify - RSS Viewer](https://codebeautify.org/rssviewer)

"""