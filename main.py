"""
MIT License

Copyright (c) 2021 HazemMeqdad

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import requests
import bs4
import discord
from discord.ext import tasks
import os

bot = discord.Client()  # bot client

my_page_followers = "https://github.com/HazemMeqdad?tab=followers"  # my followers page
required_account = "al-bimani"  # name Ahlin Chan

webhook = os.environ['webhook']
token = os.environ['token']


@tasks.loop(minutes=1)
async def show_Ahlin_Chan():
    date = requests.get(my_page_followers)
    soup = bs4.BeautifulSoup(date.content, "lxml")
    followers = soup.find_all("span", {"class": "Link--secondary"})
    list_followers = [x.text for x in followers]  # followers list

    if required_account not in list_followers:
        requests.post(webhook, json={"content": "الحق اهلين شان شال عنك الفلوا بسرعا <@750376850768789534>"})
        print("Fuck")


@bot.event
async def on_ready():
    print("Hazem show `Ahlin Chan` now")
    show_Ahlin_Chan.start()


bot.run(token)

