# Comic Downloader

A tool for downloading several webcomics, built using tkinter (for the user interface) and BeautifulSoup (for the webscrapping). All in Python3. Project was inspired by a coding exercise from the book 'Automate the boring stuff with python, 2nd Edition' by Al Sweigart.

## How to use:
1. Run comic_downloader.py. This will launch the tkinter GUI.
2. For each comic, enter which page you are currently or check the checkbox next to the comic entry to disable it (so no attempt will be made to download it).
3. Click the 'Download' button to begin the download.
4. As the program runs, the status section will show which comic is being currently downloaded and when the whole operation has completed.
5. The comics will be downloaded in the same location as the program, with a folder being created for each comic.
6. Once complete, the latest page number and the disabled/enabled status for each comic will be stored in a JSON file (same location as the program). Next time the program is ran, it will fetch the data from that file instead of asking the user to enter it again.

## Notes
1. Validation won't let anything other than a number be entered into the entry fields. An error message will show up if the user tries to enter any other character.
2. The "latest page number" saved into a JSON file takes into account how many comics have just been downlaoded. So if the user enters "200" for the XKCD entry and currently XKCD is 215 pages long, the program will download the 15 new comics and save "215" as the latest page number for XKCD.
