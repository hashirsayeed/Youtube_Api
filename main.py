from stats import Youtube_stats

API_KEY = "AIzaSyDRKqdFtKZjAV7Xgl6kqEHSgCJOaY9WX2A"
Channel_id = "UC9N0DmacOi4iWKQyygX89OQ"
# Channel_id = "UCbXgNpp0jedKWcQiULLbDTA"

yt = Youtube_stats(API_KEY, Channel_id)
yt.get_channel_stats()
yt.get_channel_videos()
yt.dump()