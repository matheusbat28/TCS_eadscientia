from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from decouple import config
from urllib.parse import urlparse, parse_qs

def validar_youtube_url(url):
    dadoUrl = urlparse(url)
    queryDadoUrl = parse_qs(dadoUrl.query)
    video_id = queryDadoUrl.get('v', [None])[0]
    if video_id is None:
        return False
    else:
        try:
            youtube = build('youtube', 'v3', developerKey=config('KEY_YOUTUBE'))
            resposta_youtube = youtube.videos().list(part='id', id=video_id).execute()
            resposta_youtube.get('items') 
            return True
        except:
            pass
        return False