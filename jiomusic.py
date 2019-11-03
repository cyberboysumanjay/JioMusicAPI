import requests
import json

def song_search(query):
    query=query.replace(' ','+')
    base_url="http://beatsapi.media.jio.com/v2_1/beats-api/jio/src/response/search2/"+query+"/"
    results=requests.get(base_url).json()
    data={}
    if (results['messageCode']==200):
        base_imageurl=results['result']['imageurl']
        s_result,p_result,a_result=[],[],[]
        for song in results['result']['data']['Songs']:
            song_data={}
            song_data["id"]=song['id']
            song_data["title"]=song['title']
            song_data["artist"]=song["artist"]
            song_data["subtitle"]= song["subtitle"]
            song_data["image"]= base_imageurl+str(song["image"]).replace('400x400','800x800')
            song_data["url"]=get_stream_link(song["id"])
            song_data["s_order"]= song["s_order"]
            song_data["type"]= song["type"]
            song_data["albumid"]=song["albumid"]
            s_result.append(song_data)
        data['songs']=s_result
        for album in results['result']['data']['Albums']:
            album_data={}
            album_data["id"]=album['id']
            album_data["title"]=album['title']
            #album_data["artist"]=album["artist"]
            album_data["subtitle"]= album["subtitle"]
            album_data["image"]= base_imageurl+str(album["image"]).replace('400x400','800x800')
            #album_data["url"]=get_stream_link(album["id"])
            #album_data["s_order"]= album["s_order"]
            album_data["type"]= album["type"]
            album_data["albumid"]=album["albumid"]
            album_data["songCount"]=album["songCount"]
            a_data=album_details(album['id'])
            album_data["label"]=a_data["header"]["label"]
            album_data["songs"]=a_data["list"]
            for song in album_data["songs"]:
                song["image"]= base_imageurl+str(song["image"]).replace('400x400','800x800')
                song["url"]=get_stream_link(song["id"])
            a_result.append(album_data)
        data['albums']=a_result
        for playlist in results['result']['data']['Playlists']:
            playlist_data={}
            playlist_data["id"]=playlist['id']
            playlist_data["title"]=playlist['title']
            #playlist_data["artist"]=playlist["artist"]
            playlist_data["subtitle"]= playlist["subtitle"]
            playlist_data["image"]= base_imageurl+str(playlist["image"]).replace('400x400','800x800')
            #playlist_data["url"]=get_stream_link(playlist["id"])
            #playlist_data["s_order"]= playlist["s_order"]
            playlist_data["type"]= playlist["type"]
            playlist_data["playlistid"]=playlist["playlistid"]
            playlist_data["songCount"]=playlist["songCount"]
            p_data=playlist_details(playlist['id'])
            playlist_data["label"]=p_data["header"]["label"]
            playlist_data["songs"]=p_data["list"]
            for song in playlist_data["songs"]:
                song["image"]= base_imageurl+str(song["image"]).replace('400x400','800x800')
                song["url"]=get_stream_link(song["id"])
            p_result.append(playlist_data)
        data['playlists']=p_result
        return (data)
    else:
        print("Error Code "+results['messageCode'])
    
def playlist_details(id):
    base_url="http://beatsapi.media.jio.com/v2_1/beats-api/jio/src/response/listsongs/playlistsongs/"+str(id)
    results=requests.get(base_url).json()
    data={}
    if (results['messageCode']==200):
        return results["result"]["data"]
        
def album_details(id):
    base_url="http://beatsapi.media.jio.com/v2_1/beats-api/jio/src/response/albumsongs/albumid/"+str(id)
    results=requests.get(base_url).json()
    data={}
    if (results['messageCode']==200):
        return results["result"]["data"]
        
def get_stream_link(id,bitrate=320):
    _id=id.split("_")
    url="http://jiobeats.cdn.jio.com/mod/_definst_/mp4:hdindiamusic/audiofiles/"+_id[0]+'/'+_id[1]+'/'+str(id)+'_'+str(bitrate)+".mp4/playlist.m3u8"
    return url    
