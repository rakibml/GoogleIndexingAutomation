import feedparser
from urllib.parse import urlparse

class BloggerFeedParser:
    def __init__(self, feed_url):
        self.feed_url = feed_url

    def get_all_post_urls(self):
        feed = feedparser.parse(self.feed_url)
        urls = []
        
        # Extract URLs from entries
        for entry in feed.entries:
            if hasattr(entry, 'link'):
                url = entry.link
                # Filter out non-post URLs
                if self._is_valid_post_url(url):
                    urls.append(url)
        return urls

    def _is_valid_post_url(self, url):
        parsed_url = urlparse(url)
        path = parsed_url.path
        if any(x in path for x in ['/search', '/archive']):
            return False
            
        if path.endswith('.html'):
            return True
            
        return False
