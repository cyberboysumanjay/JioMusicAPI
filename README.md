## JioMusic API [Deprecated]


### Show some :heart: and :star: the repo to support the project

[![GitHub stars](https://img.shields.io/github/stars/cyberboysumanjay/jiomusicapi.svg?style=social&label=Star)](https://github.com/cyberboysumanjay/JioMusicAPI)
![GitHub followers](https://img.shields.io/github/followers/cyberboysumanjay.svg?style=social&label=Follow)
[![Twitter Follow](https://img.shields.io/twitter/follow/cyberboysj.svg?style=social)](https://twitter.com/CyberboySj)

#### JioMusic API written in Python using Flask  
![JioMusic](https://telegra.ph/file/a053512b3f86018f275a2.png)
 ---
###### **NOTE:** You don't need to have JioMusic link of the song in order to fetch the song details, you can directly search Songs/Albums/Playlists by their name using this API.  

 ---

#### Features:
##### Currently the API can get the following details for a specific song in JSON format:
* **Song Name**
* **Singer Name**
* **Album Name**
* **Song Thumbnail URL (Max Resolution)**
* **Streamable Link (320Kbps)**
* **Album Art Link (Max Resolution)**
* .... and much more!

```json
{
    "songs":
        {
          "albumid": "1734322",
          "artist": "Shreya Ghoshal, NAKASH AZIZ",
          "id": "1735_1734322_1",
          "image": "http://jioimages.cdn.jio.com/hdindiamusic/images/1735/1734322/1734322_1556177408_800x800.jpg",
          "s_order": "286",
          "subtitle": "Bharat",
          "title": "Slow Motion",
          "type": "songs",
          "url": "http://jiobeats.cdn.jio.com/mod/_definst_/mp4:hdindiamusic/audiofiles/1735/1734322/1735_1734322_1_320.mp4/playlist.m3u8"
        }
}
```

#### Installation:

Clone this repository using
```sh
$ git clone https://github.com/cyberboysumanjay/JioMusicAPI
```
Enter the directory and install all the requirements using
```sh
$ pip3 install -r requirements.txt
```
Run the app using
```sh
$ python3 app.py
```
Navigate to 127.0.0.1:5000 to see the Homepage

#### Usage:
```sh
http://127.0.0.1:5000/result/?query=<insert-song-or-playlist-or-album-name-here>
```
**Example:** Navigate to http://127.0.0.1:5000/result/?query=slow%20motion to get a json response of song data in return.
**Live Example:** Navigate to https://jiomusic.herokuapp.com/result/?query=slow%20motion and see yourself! (Maybe Slow, Thanks to Heroku!)
### You can fork the repo and deploy on VPS or deploy it on Heroku :)  
[![Deploy](https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku)](https://heroku.com/deploy?template=https://github.com/cyberboysumanjay/JioMusicAPI/tree/master)


#### Star the Repo in case you liked it :)

# © [Sumanjay](https://cyberboysumanjay.github.io)
