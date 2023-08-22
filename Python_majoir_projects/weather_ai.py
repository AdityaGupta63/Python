from pytube import YouTube

# ask the user for the video URL
url = input("Enter the YouTube video URL: ")

# create a YouTube object
yt = YouTube(url)

# get the highest resolution stream
stream = yt.streams.get_highest_resolution()

# download the video
print("Downloading video...")
stream.download()
print("Video downloaded successfully!")