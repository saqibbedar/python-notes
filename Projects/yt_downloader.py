from pytube import YouTube

# setup link
link = input("Enter download link: ")
yt = YouTube(link)

# print video info
print(f"Title: {yt.title}")
print(f"Views: {yt.views}")

# get highest resolution stream available
yt_download = yt.streams.get_highest_resolution()

# ask user for download path
PATH = "/Users/Saqib Bedar/Downloads"

# download the video
yt_download.download(PATH)