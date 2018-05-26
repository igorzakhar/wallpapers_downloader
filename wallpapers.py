import asyncio
import argparse
import calendar
import datetime
import os
import re

import aiohttp
from bs4 import BeautifulSoup


BASE_URL = 'https://www.smashingmagazine.com'
SIZE = ('320x480', '640x480', '800x480', '800x600', '1024x768', '1024x1024',
        '1152x864', '1280x720', '1280x800', '1280x960', '1280x1024',
        '1366x768', '1440x900', '1440x1050', '1600x1200', '1680x1050',
        '1680x1200', '1920x1080', '1920x1200', '1920x1440', '2560x1440')


def get_current_month_year():
    current_date = datetime.datetime.utcnow()
    return current_date.month, current_date.year


def process_args():
    parser = argparse.ArgumentParser(
        description='Get wallpapers from smashingmagazine.com'
    )
    parser.add_argument(
        '-s',
        '--size',
        type=str,
        required=True,
        help='Size in format {width}x{height}(e.g. 1920x1080)'
    )
    parser.add_argument(
        '-m',
        '--month',
        type=int,
        default=get_current_month_year()[0],
        help='Month(current month as default value).'
    )
    parser.add_argument(
        '-y',
        '--year',
        type=int,
        default=get_current_month_year()[1],
        help='Year(current year as default value).'
    )
    parser.add_argument(
        '-c',
        '--calendar',
        action='store_true',
        help='Wallparers with calendar.'
    )
    return parser.parse_args()


async def get_wallpapers_html(session, url):
    try:
        async with session.get(url) as response:
            return await response.text()
    except aiohttp.ClientError as err:
        print(err)


async def get_image(session, url):
    try:
        async with session.get(url) as response:
            return await response.content.read()
    except aiohttp.ClientError:
        pass


def url_making(month, year):
    _month = month - 1
    _year = year
    list_of_month = tuple(calendar.month_name)
    month_name = list_of_month[month].lower()

    if month == 1:
        _month = 12
        _year = year - 1

    url_string = '{}/{}/{:02d}/desktop-wallpaper-calendars-{}-{}/'
    url = url_string.format(BASE_URL, _year, _month, month_name, year)
    return url


def extract_links_from_html(page, size, with_calendar):
    pattern_str = ''
    if with_calendar:
        pattern_str = 'http:\/\/files\..*?\/cal\/..*?{}\..*'.format(size)
    else:
        pattern_str = 'http:\/\/files\..*?\/nocal\/..*?{}\..*'.format(size)
    pattern = re.compile(pattern_str)
    soup = BeautifulSoup(page, 'lxml')
    links = (a['href'] for a in soup.find_all('a', href=pattern))
    return links


async def download_wallpaper(session, link):
    filename = link.split('/')[-1]
    image = await get_image(session, link)
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, save_image, image, filename)


def save_image(image, filename):
    path = os.path.join(os.getcwd(), filename)
    try:
        with open(path, mode='wb') as fp:
            fp.write(image)
            print(filename)
    except OSError:
        pass


async def downloader(session, links):
    tasks = [
        asyncio.ensure_future(download_wallpaper(session, link))
        for link in links
    ]
    await asyncio.gather(*tasks)


async def main():
    args = process_args()
    url = url_making(args.month, args.year)
    async with aiohttp.ClientSession() as session:
        html = await get_wallpapers_html(session, url)
        links = extract_links_from_html(html, args.size, args.calendar)
        await downloader(session, links)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
