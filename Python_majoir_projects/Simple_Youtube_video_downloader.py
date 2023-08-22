from pytube import YouTube

url = input('Paste the YouTube video URL here : ')

yt = YouTube(url)

stream = yt.streams.get_highest_resolution()

print('Your Video is Downloading...')
stream.download()
print('Your Video is downloaded sucessfully!')