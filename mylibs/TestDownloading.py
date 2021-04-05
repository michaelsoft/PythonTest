import requests
 
hd = {
    'Connection':'keep-alive',
    'y':'v9-xg-web-s.ixigua.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}
 
print("Downloading...")
# 貌似这url是有时效性的，过一阵子就不行了。
url = 'https://v9-xg-web-s.ixigua.com/36a01655384e24c6bb1e81a5c86a0b48/606ac6f9/video/tos/cn/tos-cn-o-0004/b5748a67206e4389b5325d18944d901d/media-audio-und-mp4a/'
url2 = "https://v9-xg-web-s.ixigua.com/f5ba47f6371b4b67695d1473f0f188a4/606ae737/video/tos/cn/tos-cn-vd-0026/fea3b5fea9f245d7b5d3dbef448fdb64/media-audio-und-mp4a/"
r = requests.get(url2, headers=hd, stream=True)
 
with open(r'd:\mp3\test2.mp3', "wb") as mp3:
    for chunk in r.iter_content(chunk_size=1024 * 1024):
        if chunk:
            mp3.write(chunk)
 
print("Finished")
