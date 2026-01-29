import os
def main():
    with open('Settings.txt', 'r') as f:
        link= f.readline()
        cmd= f.readline()
    print("Welcome to the configuration for your python auto downloader!")
    choice = "not exit"
    while choice.lower != "exit":
        choice = input("What do you want to do?: ")
        if choice.lower() == 'cng-link' or choice.lower() == 'cng link' or choice.lower() == 'link':
            try:
                link = change_link()
            except Exception:
                link = link
        elif choice.lower() == 'cng-cmd' or choice.lower() == 'cng cmd' or choice.lower() == 'cmd' or choice.lower() == 'command':
            try:
                cmd = change_cmd()
            except Exception:
                cmd = cmd
        elif choice.lower() == 'exit':
            break
        elif choice.lower() =='help':
            print("Commands:")
            print("cng-cmd: This changes the command you use when downloading, use this to add meta data or check for overflow")
            print("cng-link: This changes the link for your playlist, however if you change playlists it will cause the sync to break")
            print("exit: this exits the configuration page and saves changes DONT KEYBOARD INTERUPT (ctrl+c) NOTHING WILL WRITE")
            print("help: Shows this page")
        else:
            print("Command invalid")
            print("If you need help type 'help'")
    rewrite_file(link,cmd)
    return()


def change_link():
    correct = False
    while correct == False:
        link = input("Please enter your new link: ")
        if link.lower() == "exit" or cmd.lower() == 'cancel':
            print("Cancelling new link")
            raise Exception()
        correct = input(f"Is '{link}' correct?: ")
        correct =  True if correct.lower() == 'y' or correct.lower() == 'yes' else False
    log_change = input("Thank you! Would you like to [A] erase the log (WILL ERASE ALL PROGRESS) or [B] keep it the same: ")
    if log_change.lower() == 'a':
        with open("Log.txt",'r+') as file:
            file.write("STOP-HERE \n")
        print("Log has been erased!")
    return link

def rewrite_file(link,cmd):
    os.remove("Settings.txt")
    with open("Settings.txt", 'a') as f:
        f.write(f'{link}{cmd}')


def change_cmd():
    correct = False
    while correct == False:
        cmd = input("Please enter your new command: ")
        if cmd.lower() == "exit" or cmd.lower() == 'cancel':
            print("Cancelling new command")
            raise Exception()
        correct = input(f"Is '{cmd}' correct?: ")
        correct =  True if correct.lower() == 'y' or correct.lower() == 'yes' else False
    return cmd

