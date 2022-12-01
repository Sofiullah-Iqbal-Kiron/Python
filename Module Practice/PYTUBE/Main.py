from pytube import YouTube


# Progressive streams have the video and audio in a single file.
# 2 types of stream: progressive, adaptive(DASH)


def printCompleted(a, b):
    print(type(a), type(b))
    print("Download completed & saved on this path:", b)


def justDownloading(a, b, c):
    print(type(a), type(b))
    print("Remaining: ", str(b), "bytes")


# Create a YouTube object. Supply valid youtube watch url.
yt = YouTube("https://youtu.be/zuaLWHiRXkg",
             on_complete_callback=printCompleted)

# Print the title of this youtube object(a single youtube video).
# print("Video title:", yt.title)

# Print thumbnail url
# print("Thumbnail url:", yt.thumbnail_url)

# Neat, right? Let's download the video in this directory.
yt.streams.filter(res="1080p").last().download(filename="theVideo.mp4")
yt.streams.filter(type="audio").first().download(filename="theAudio.mp3")

# for a in yt.streams:
#     print(a)
