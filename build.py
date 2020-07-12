import feedparser

URL="https://rasjani.github.io/feed.xml"
feed = feedparser.parse(URL)
print("### Latests posts")
for post in feed["entries"][0:5]:
    title = post["title"]
    url = post["links"][0]["href"]
    ts = post["published_parsed"]
    date = f"* {ts.tm_mday:02}.{ts.tm_mon:02}.{ts.tm_year}"
    print(f"{date} - [{title}]({url})")
print("\nMore in the [blog](http://rasjani.github.io)")
