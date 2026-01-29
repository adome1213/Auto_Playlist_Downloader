import Auto_Downloader
import Config
def main():
    choice = input("Do you want to [A] to run the auto downloader or [B] Edit the configuration: \n")
    if choice.lower() == "a":
        Auto_Downloader.main()
        main()
    elif choice.lower() == "b":
        Config.main()
        main()
    else:
        print("Invalid reponse")
        main()
main()