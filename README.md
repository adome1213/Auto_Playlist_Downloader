# What does this do? #
* Allows you to use yt-dlp to download a constant running playlist
* Faster than simply using --no-overwrite
* Allows you to split up files so you don't get rate limited

# How does it work #
1. Gets list of all songs in playlist
2. Puts thoose into a log file
3. Counts how many songs are in the playlist
4. Compares it to the amount of songs already downloaded (It does this by looking at the log file before)
5. Subtracts the amount of songs before vs the amount of songs in the playlist currently
6. Downloads songs not downloaded

# Heads up #
* When writing command don't add yt-dlp just add the extensions to it i.e -x --audio-format mp3
* Don't mess with the log outside of the program, it can cause the program to download incorrect things
* The program works in a very specific way, simply put don't edit the order your songs are in, it will cause an error
* When using config don't use keyboard interupt (ctrl + c) because it won't save your configuration

# How to use it #
1. Configure it by simply typing 'config'
2. Add your link
3. Add command (optional)
4. Run auto downloader
5. Enjoy!



