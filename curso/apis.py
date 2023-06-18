from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from decouple import config
from urllib.parse import urlparse, parse_qs
from pytube import YouTube

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
    
def tempo_video_youtube(url):
    try:
        video = YouTube(url)
        duracao = video.length
        minuto, secondo = divmod(duracao, 60)
        hora, minuto = divmod(minuto, 60)
        return f'{hora:02d}:{minuto:02d}:{secondo:02d}'
    except Exception as e:
        return e
    
    
def obter_id_video_youtube(url):
    dado_url = urlparse(url)
    query_dado_url = parse_qs(dado_url.query)
    video_id = query_dado_url.get('v', [None])[0]
    return video_id
