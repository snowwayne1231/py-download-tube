from pytube import YouTube
import os

urls = [
    "https://www.youtube.com/watch?v=WEAwtnGpDmk",
    "https://www.youtube.com/watch?v=VOcb6ZHxSjc",
    "",
]

target_path = "./Downloads"

def download_by_url(url):

    yt = YouTube(url)

    video = yt.streams.filter(only_audio=True).first()

    out_file = video.download(output_path=target_path)

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print("target path = " + (new_file))
    print("mp3 has been successfully downloaded.")



list_downloaded = os.listdir(target_path)
length_downloaded = len(list_downloaded)
index_pos = 1
for u in urls:
    if index_pos > length_downloaded:
        download_by_url(u)
    index_pos += 1