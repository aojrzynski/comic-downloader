"""The comic webscrapping code is here. The following functions can be found here:

download_abstruse_goose
download_cyanide_and_happiness
download_lfg
download_lovenstein
download_order_of_the_stick
download_chapel
download_wukrii
download_xkcd
"""

import os
import bs4
import requests


def download_abstruse_goose(program_abs_path, abstruse_page_num):
    """Downloads latest Abstruse Goose comics."""
    # Create/change appropriate comic folder.
    comic_folder = os.path.join(program_abs_path, "abstruse")
    if os.path.exists(comic_folder):
        os.chdir(comic_folder)
    else:
        os.mkdir(comic_folder)
        os.chdir(comic_folder)

    while True:
        # Create the comic URL.
        url = 'https://abstrusegoose.com/' + str(abstruse_page_num)

        try:
            # Get the comic page.
            res = requests.get(url)
            res.raise_for_status()

            # Extract the image src.
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            match1 = soup.select("img[src*='/strips/']")
            if not match1: # If img element is not found, no futher new comics can be downloaded.
                return abstruse_page_num
            comic_url = match1[0].get("src")

            # Get the comic image.
            res = requests.get(comic_url)
            res.raise_for_status()

            # Download the comic image.
            image_file = open('abstruse' + str(abstruse_page_num) + '.jpg', 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

            # Increment the latest comic num.
            abstruse_page_num += 1

        except requests.exceptions.HTTPError:
            return abstruse_page_num

def download_cyanide_and_happiness(program_abs_path, cyanide_page_num):
    """Downloads latest Cyanide and Happiness comics."""
    # Create/change appropriate comic folder.
    comic_folder = os.path.join(program_abs_path, "cyanide_and_happiness")
    if os.path.exists(comic_folder):
        os.chdir(comic_folder)
    else:
        os.mkdir(comic_folder)
        os.chdir(comic_folder)

    while True:
        # Create the comic URL.
        url = 'https://explosm.net/comics/' + str(cyanide_page_num) +'/'

        try:
            # Get the comic page.
            res = requests.get(url)
            res.raise_for_status()

            # Extract the image src.
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            match1 = soup.find('div', id='comic-wrap')
            match2 = match1.find('img', id='main-comic')
            comic_url = 'https:' + match2.get('src')

            # Get the comic image.
            res = requests.get(comic_url)
            res.raise_for_status()

            # Download the comic image.
            image_file = open('cyanide_and_happiness' + str(cyanide_page_num) + '.jpg', 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

            # Increment the latest comic num.
            cyanide_page_num += 1

        except requests.exceptions.HTTPError:
            return cyanide_page_num

def download_lfg(program_abs_path, lfg_page_num):
    """Downlaods latest LFG comics."""
    # Create/change appropiate comic folder.
    comic_folder = os.path.join(program_abs_path, "lfg")
    if os.path.exists(comic_folder):
        os.chdir(comic_folder)
    else:
        os.mkdir(comic_folder)
        os.chdir(comic_folder)

    while True:
        # Create the comic URL.
        url = "https://www.lfg.co/page/" + str(lfg_page_num) + "/"

        try:
            # Get the comic page.
            res = requests.get(url)
            res.raise_for_status()

            # Extract the image source.
            soup = bs4.BeautifulSoup(res.text, "html.parser")
            match1 = soup.find("div", id="comic-img")
            match2 = match1.find("img")
            comic_url = match2.get("src")

            # Get the comic image.
            res = requests.get(comic_url)
            res.raise_for_status()

            # Downlad the comic image.
            image_file = open(f"lfg{lfg_page_num}.jpg", "wb")
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

            # Increment latest comic number.
            lfg_page_num += 1

        except requests.exceptions.HTTPError:
            return lfg_page_num

def download_lovenstein(program_abs_path, lovenstein_page_num):
    """Downloads latest Lovenstein comics."""
    # Create/change appropriate comic folder.
    comic_folder = os.path.join(program_abs_path, "lovenstein")
    if os.path.exists(comic_folder):
        os.chdir(comic_folder)
    else:
        os.mkdir(comic_folder)
        os.chdir(comic_folder)

    while True:
        # Create the comic URL.
        url = 'https://www.mrlovenstein.com/comic/' + str(lovenstein_page_num) + "/"

        try:
            # Get the comic page.
            res = requests.get(url, headers={"User-Agent": "XY"})
            res.raise_for_status()

            # Extract the image src.
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            match1 = soup.find("img", id="comic_main_image")
            if not match1: # If img element is not found, no futher new comics can be downloaded.
                return lovenstein_page_num
            comic_url = "https://www.mrlovenstein.com" + str(match1.get("src"))

            # Get the comic image.
            res = requests.get(comic_url)
            res.raise_for_status()

            # Download the comic image.
            image_file = open('lovenstein' + str(lovenstein_page_num) + '.jpg', 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

            # Increment the latest comic num.
            lovenstein_page_num += 1

        except requests.exceptions.HTTPError:
            return lovenstein_page_num

def download_order_of_the_stick(program_abs_path, stick_page_num):
    """Downloads latest Order of the Stick comics."""
    # Create/change appropriate comic folder.
    comic_folder = os.path.join(program_abs_path, "order_of_the_stick")
    if os.path.exists(comic_folder):
        os.chdir(comic_folder)
    else:
        os.mkdir(comic_folder)
        os.chdir(comic_folder)

    while True:
        # Create the comic URL.
        url = 'https://www.giantitp.com/comics/oots' + str(stick_page_num).rjust(4, "0") +'.html'

        try:
            # Get the comic page.
            res = requests.get(url)
            res.raise_for_status()

            # Extract the image src.
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            match1 = soup.select("img[src*='comics/oots/']")
            if not match1: # If img element is not found, no futher new comics can be downloaded.
                return stick_page_num
            comic_url = match1[0].get("src")

            # Get the comic image.
            res = requests.get(comic_url)
            res.raise_for_status()

            # Download the comic image.
            image_file = open('order_of_the_stick' + str(stick_page_num) + '.jpg', 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

            # Increment the latest comic num.
            stick_page_num += 1

        except requests.exceptions.HTTPError:
            return stick_page_num

def download_chapel(program_abs_path, chapel_page_num):
    """Downloads latest The Chapel comics."""
    # Create/change appropiate comic folder.
    comic_folder = os.path.join(program_abs_path, "the_chapel")
    if os.path.exists(comic_folder):
        os.chdir(comic_folder)
    else:
        os.mkdir(comic_folder)
        os.chdir(comic_folder)

    while True:
        # Create the comic URL.
        url = "https://www.chapelcomic.com/" + str(chapel_page_num) + "/"

        try:
            # Get the comic page.
            res = requests.get(url)
            res.raise_for_status()

            # Extract the image src.
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            match1 = soup.find('div', id='comic')
            match2 = match1.find('img', {"class": "strip"})
            comic_url = match2.get('src')

            # Get the comic image.
            res = requests.get(comic_url)
            res.raise_for_status()

            # Download the comic image.
            image_file = open('the_chapel' + str(chapel_page_num) + '.jpg', 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

            # Increment the latest comic num.
            chapel_page_num += 1

        except requests.exceptions.HTTPError:
            return chapel_page_num

def download_wukrii(program_abs_path, wukrii_page_num):
    """Downloads latest Wukrii comics."""
    # Create/change appropriate comic folder.
    comic_folder = os.path.join(program_abs_path, "wukrii")
    if os.path.exists(comic_folder):
        os.chdir(comic_folder)
    else:
        os.mkdir(comic_folder)
        os.chdir(comic_folder)

    while True:
        # Create the comic URL.
        url = 'https://www.wukrii.com/comic/chapter-3-page-' + str(wukrii_page_num) +'/'

        try:
            # Get the comic page.
            res = requests.get(url)
            res.raise_for_status()

            # Extract the image src.
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            match1 = soup.find("div", id="comic")
            match2 = match1.find("img")
            comic_url = match2.get("src")

            # Get the comic image.
            res = requests.get(comic_url)
            res.raise_for_status()

            # Download the comic image.
            image_file = open('wukrii' + str(wukrii_page_num) + '.jpg', 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

            # Increment the latest comic num.
            wukrii_page_num += 1

        except requests.exceptions.HTTPError:
            return wukrii_page_num

def download_xkcd(program_abs_path, xkcd_page_num):
    """Downloads latest XKCD comics."""
    # Create/change appropriate comic folder.
    comic_folder = os.path.join(program_abs_path, "xkcd")
    if os.path.exists(comic_folder):
        os.chdir(comic_folder)
    else:
        os.mkdir(comic_folder)
        os.chdir(comic_folder)

    while True:
        # Create the comic URL.
        url = 'https://xkcd.com/' + str(xkcd_page_num) +'/'

        try:
            # Get the comic page.
            res = requests.get(url)
            res.raise_for_status()

            # Extract the image src.
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            match1 = soup.find('div', id='comic')
            match2 = match1.find('img')
            comic_url = 'https:' + match2.get('src')

            # Get the comic image.
            res = requests.get(comic_url)
            res.raise_for_status()

            # Download the comic image.
            image_file = open('xkcd' + str(xkcd_page_num) + '.jpg', 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

            # Increment the latest comic num.
            xkcd_page_num += 1

        except requests.exceptions.HTTPError:
            return xkcd_page_num
