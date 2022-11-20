from pytube import YouTube


def printCompleted(a, b):
    print(type(a), type(b))
    print("Download completed & saved on this path:", b)


def justDownloading(a, b, c):
    print(type(a), type(b))
    print("Remaining: ", str(b), "bytes")


# Create a YouTube object. Supply valid youtube watch url.
yt = YouTube("https://youtu.be/c3_NntYhzV4")

# Print the title of this youtube object(a single youtube video).
# print("Video title:", yt.title)

# Print thumbnail url
# print("Thumbnail url:", yt.thumbnail_url)

# Neat, right? Let's download the video in this directory.
# yt.streams.last().download()

for a in yt.streams:
    print(type(a))
