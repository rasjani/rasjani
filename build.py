import feedparser
import jinja2
from pathlib import Path
from pprint import pprint

BLOGURL="https://rasjani.github.io"
FEED=f"{BLOGURL}/feed.xml"
MAX_POSTS=5
template = None


def format_date(ts):
    return f"{ts.tm_mday:02}.{ts.tm_mon:02}.{ts.tm_year}"

with Path("README.template").open("r") as f:
    template = jinja2.Template(f.read())

feed = feedparser.parse(FEED)
posts = list(map(lambda post: {"date": format_date(post["published_parsed"]),"title": post["title"], "link": post["links"][0]["href"]}, feed["entries"][0:MAX_POSTS]))


with Path("README.md").open("w") as f:
    f.write(template.render(blogurl=BLOGURL, posts=posts))

