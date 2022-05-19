from discord.ext.commands import bot
import requests
import discord
from discord.ext import commands
from discord_webhook import DiscordWebhook, DiscordEmbed
from geohack import find

#set prefix of commands to !
bot = commands.Bot(command_prefix="!")
client = discord.Client()

#make sure the bot is online
@bot.event
async def on_ready():
    print("Bot is online!")

#create command locate to return embed of location
@bot.command()
async def locate(ctx, gameID):

    #create discord webhook
    webhook = DiscordWebhook(url="DISCORD_WEBHOOK_HERE")
    embed = DiscordEmbed (title="🗺️ Location Found! 👁️", color=2303786)
    embed.set_footer(text='by n8te')
    #refer to find in geohack.py and use list notaion to specify field from the find function call output
    embed.add_embed_field(name= 'Coordinates: ', value='{}'.format((find(gameID))[1]), inline=False)
    embed.add_embed_field(name= 'Location:', value='{}'.format((find(gameID))[0]), inline=False)
    embed.set_timestamp()
    webhook.add_embed(embed)

    #execute webhook :D
    response = webhook.execute()


bot.run("BOT_TOKEN_HERE")
