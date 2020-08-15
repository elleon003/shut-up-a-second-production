from django.contrib.syndication.views import Feed
from blog.models import BlogPost
from django.utils.feedgenerator import Atom1Feed


class RssFeed(Feed):
    title = "Shut up A Second.com"
    link = "/blog/"
    description = "I tell other people's stories for a living. Here, I tell mine."
    feed_url = '/rss'
    author_name = 'Brandon Anderson'
    feed_copyright = 'Copyright (c) 2020 ShutUpASecond.com'
    language = "en"

    def items(self):
        return BlogPost.objects.live().order_by('-first_published_at')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return item.full_url

    # return the date the article was published
    def item_pubdate(self, item):
        return item.first_published_at

    # return the date of the last update of the article
    def item_updateddate(self, item):
        return item.last_published_at


class AtomFeed(RssFeed):
    feed_type = Atom1Feed
    link = "/atom/"
    subtitle = RssFeed.description
