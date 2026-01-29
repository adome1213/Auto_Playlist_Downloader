import os
import sys
try:
    with open('Settings.txt', 'r') as f:
        link = f.readline()
        cmd = f.readline()
except FileNotFoundError:
    print("You need to configure it first before you run, please add a link in config")
    return()

def main():
    if link == " ":
        print("You need to configure it first, I need a link, command, to run")
        exit()
    start,curr_pos = get_start()
    end = get_end(link)
    with open("Log.txt","r+") as file:
        if (end-start) > 300:
            choice = input("Disclaimer: Youtube begins to rate limit at about 300 videos per hour, the amount to download exceeds 300, do you wish to \n [A]risk the rate limit [B]Break the files up? \n")
            if choice.lower() == 'a':
                download(start,end)
                return()
            elif choice.lower() == 'b':
                download((start),(start+299))
                file.seek(curr_pos)
                for x in range(299):
                    file.readline()
                file.seek(file.tell())
                file.write("STOP-HERE \n")
            else:
                print("Invalid input")
        elif (end-start) == 0:
            print("Nothing to Download")
        else:
            download(start,end)
            print(start)
            return()



def download(start,end):
    start = start
    end = end
    os.system(f"yt-dlp --playlist-items {start+1}-{end} {cmd} '{link}'")
    return()


def get_end(link):
    command = f"yt-dlp --flat-playlist --print title '{link}'  > Log.txt"
    os.system(command)
    end = 0
    with open("Log.txt","r+") as file:
        for x in file:
            end = end + 1
    return(end)

def get_start():
    with open("Log.txt", "r+") as file:
            start,pos = 0,0
            for line in file:
                if line == "STOP-HERE \n" :
                    break
                start = start + 1
            file.seek(0)
            pos = file.tell()
            return(start,pos)




