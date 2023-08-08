import pytube

from pytube import YouTube

link=("https://www.youtube.com/watch?v=OKuiyX5k6zg&t=11307s")

youtu = YouTube(link)
print(youtu)
# except Exception as e:
# print('error:',e)
#print(youtube_1.title)
#print(youtube_1.tumbnail_url)

videos =youtu.streams.all()                                         #stream= multiple pixer
vid = list(enumerate(videos))                                           # stream are convert into list & enumerate give the index number
for i in vid:
    print(i)
print()
strm = int(input("enter :"))                                            
videos[strm].download()
print("Succesfully")