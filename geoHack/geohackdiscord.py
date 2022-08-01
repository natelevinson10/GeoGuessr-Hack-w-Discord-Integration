import requests, time, discord
from discord.ext import commands
from discord_webhook import DiscordWebhook, DiscordEmbed
from discord.ext.commands import bot

def getLocation(gameID)
 response = requests.get(f"https://www.geoguessr.com/api/v3/games/{gameID}")

    obj = response.json()
    round = obj['round']
    lat = (obj["rounds"][round - 1]["lat"]) 
    lng = (obj["rounds"][round - 1]["lng"])


    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
    }

    response2 = requests.get("https://api.opencagedata.com/geocode/v1/json?q=" + str(lat) + "+" + str(lng) + "&key=03c48dae07364cabb7f121d8c1519492", headers=  headers)
    obj2 = response2.json()

    formatted = (obj2["results"][0]["formatted"])
    return formatted


bot = commands.Bot(command_prefix="!")
client = discord.Client()

@bot.event
async def on_ready():
    print("Everything's all ready to go~")

@bot.command()
async def find(ctx, gameID):
    webhook = DiscordWebhook(url="DISCORD_WEBHOOK_URL")
    embed = DiscordEmbed (title="🗺️ Location Found! 👁️", color=2303786)
    embed.set_footer(text='by n8te', icon_url = "https://wallpaperaccess.com/full/5036271.jpg%22")
    embed.add_embed_field(name= 'Location:', value='{}'.format(getLocation(gameID)), inline=False)
    embed.set_timestamp()
    webhook.add_embed(embed)
    response = webhook.execute()

bot.run("BOT_AUTH_KEY")
