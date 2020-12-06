import pytube

url = 'https://www.youtube.com/watch?v=aiRY36TPVo8'

video = pytube.YouTube(url)

stream = video.streams.get_by_itag(299)
print("Downloading.....")
stream.download(filename="trial")

'''
for stream in video.streams:
    if "video" in str(stream) and "mp4" in str(stream):
        print(stream)

'''