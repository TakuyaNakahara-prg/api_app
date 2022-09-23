from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import pandas as pd


try:
    from .localapi import *
except ImportError:
    pass
YOUTUBE_API_SERVICE_NAME = 'youtube' 


def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, 'v3', developerKey = YOUTUBE_API_KEY)
    search_response = youtube.search().list(part = 'id, snippet', q = options, maxResults = 10, order = 'viewCount', type = 'video',).execute()

    viewcount_list = []
    title_list = []
    channel_list = []
    thumbnail_list = []
    videoid = []


    for search_result in search_response['items']:
        viewcount = youtube.videos().list(part = 'statistics', id = search_result['id']['videoId']).execute()
        viewcount_list.append(viewcount['items'][0]['statistics']['viewCount'] + '回')
        title_list.append(search_result['snippet']['title']) 
        channel_list.append(search_result['snippet']['channelTitle'])
        thumbnail_list.append(search_result['snippet']['thumbnails']['default']['url'])
        videoid.append(search_result['id']['videoId']) 


        df = pd.DataFrame({
            'title':title_list,
            'channel':channel_list,
            'viewcount':viewcount_list,
            'thumbnail':thumbnail_list,
            'videoid':videoid
        })

    return df



if __name__ == "__main__":
    word = input('キーワードを入力')
    #print(youtube_search(word))