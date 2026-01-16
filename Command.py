import os
import sys
def main():
    file = open("Python/Music Downloader/Log.txt","r+")
    link = get_link()
    start = get_start(file,link)
    curr_pos= file.tell()
    file.close()
    end = get_end(link)
    file = open("Python/Music Downloader/Log.txt","r+") 
    if (end-start) > 300:
        print("Disclaimer: Youtube begins to rate limit at about 300 videos per hour, the amount to download exceeds 300, do you wish to \n [A]risk the rate limit [B]Break the files up?")
        choice = input(" ")
        if choice.lower() == 'a':
            #download(start,end,link)
            return()
        elif choice.lower() == 'b':
            #download((start+1),(start+300),link)
            print(curr_pos)
            file.seek(curr_pos,0)
            print(f"tell? {file.tell()}")

            count = 0
            count = count + 1
            print(f"tell? {file.readline()}")

            file.write("\n Meow )")

        else:
            print("Invalid input")
    elif (end-start) == 0:
        print("Nothing to Download")
    else:
        #download(start,end,link)
        return()



def download(start,end,link):
    start = start
    end = end
    os.system(f"yt-dlp --playlist-items {start+1}-{end}")
    return()


def get_end(link):
    command = f"cd 'Python/Music Downloader'  && yt-dlp --flat-playlist --print title '{link}'  > Log.txt"
    os.system(command)
    end = 0
    file = open("Python/Music Downloader/Log.txt","r+")
    for x in file:
        end = end + 1
    return(end)

def get_start(file,link):
    start = 0
    for line in file:
        start = start + 1
    return(start)

def get_link():
    try: 
        link = sys.argv[1]
    except IndexError:
        link = input("Error: Please input your playlist link: ")
    return link


main()

