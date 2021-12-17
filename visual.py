import pandas as pd
import json
import matplotlib.pyplot as plt
f = "fightincowboy.json"
with open(f, 'r') as q:
    data = json.load(q)
channel_id, stats = data.popitem()
channel_stats , video_stats = stats['channel_statistics'], stats['video_data']

result_stats = []

for vid in sorted(video_stats.items(), key=lambda item: int(item[1]['viewCount'])):
    video_id = vid[0]
    title = vid[1]['title']
    views = int(vid[1]['viewCount'])
    likes = int(vid[1]['likeCount'])
    comments = int(vid[1]['commentCount'])
    result_stats.append([video_id, title, views, likes, comments])

df = pd.DataFrame(result_stats, columns=['Video ID', 'Title', 'Views', 'Likes', 'Comments'])
ax = df.head(5).plot.bar(x = "Title", y = "Views", figsize = (16, 8), fontsize = 8, width = 0.2)
plt.show()