import requests
import json
import time
from tqdm import tqdm

class Youtube_stats:
    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_stats = None
        self.video_stats = None
    
    def get_channel_stats(self):
        url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}"
        j_url = requests.get(url)
        data = json.loads(j_url.text)
        try:
            items = data['items'][0]['statistics']
        except:
            items = None
        self.channel_stats = items
        return items

    def dump(self):
        if not self.channel_stats or not self.video_stats:
            return
        fused_data = {self.channel_id: {"channel_statistics": self.channel_stats, "video_data": self.video_stats}}
        channel_title = self.video_stats.popitem()[1].get('channelTitle', self.channel_id).replace(" ", "_").lower()
        filename = channel_title+'.json'
        with open(filename, 'w') as f:
            json.dump(fused_data, f, indent=4)
        print('File Dumped')
    
    def get_channel_videos(self):
        channel_videos = self.get_videos(limit=2)
        parts = ['snippet', 'statistics', 'contentDetails']
        for video_id in tqdm(channel_videos):
            for part in parts:
                data = self.get_single_video(video_id, part)
                channel_videos[video_id].update(data)
        self.video_stats = channel_videos
        return channel_videos

    def get_single_video(self, video_id, part):
        url = f"https://www.googleapis.com/youtube/v3/videos?part={part}&id={video_id}&key={self.api_key}"
        j_url = requests.get(url)
        d = json.loads(j_url.text)
        try:
            data = d['items'][0][part]
        except:
            print('error while getting video data')
            data = {}
        return data

    def get_videos(self, limit = None):
        url = f"https://www.googleapis.com/youtube/v3/search?channelId={self.channel_id}&key={self.api_key}&part=snippet&order=date"
        if limit and isinstance(limit, int):
            url += "&maxResults="+str(limit)
        idx = 0
        vid, npt = self.get_vids_perpage(url)
        while npt and idx < 2:
            next_url = url+'&pageToken='+npt
            next_vid, npt = self.get_vids_perpage(next_url)
            vid.update(next_vid)
            idx += 1
        return vid
    
    def get_vids_perpage(self, url):
        jdata = requests.get(url)
        data = json.loads(jdata.text)
        channel_vids = {}
        if 'items' not in data:
            return channel_vids, None
        
        items = data['items']
        npt = data.get('nextPageToken', None)
        for item in items:
            try:

                if item['id']['kind'] == "youtube#video":
                    video_id = item['id']['videoId']
                    channel_vids[video_id] = {}
            except:
                print('Error while getting video ID')
        return channel_vids, npt







 