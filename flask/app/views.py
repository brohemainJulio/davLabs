from app import app
from flask import Flask, request, render_template, session, redirect, url_for, escape
import os
import urllib

#global variables
mega=0
power=0
info = {}

def get_jackpots():
    #scrape lottery results
    html = urllib.request.urlopen('http://www.walottery.com/JackpotGames/').read()
    html=str(html)
    #ugly parse out cash option jackpot amounts
    x = html.split('<p>Cash Option <strong>')
    tmpPower = x[1].split(' Million*</strong></p>')
    tmpMega = x[2].split(' Million*</strong></p>')
    power = tmpPower[0].strip('$')
    mega = tmpMega[0].strip('$')
    #get powerball jackpot
    tmpPower = x[0][-200:]
    tmpPower = tmpPower.split('<h1>')
    tmpPower = tmpPower[1].split(' Million*</h1>')
    powerJackpot = tmpPower[0].strip('$')
    #get mega jackpot
    tmpMega = x[1][-200:]
    tmpMega = tmpMega.split('<h1>')
    tmpMega = tmpMega[1].split(' Million*</h1>')
    megaJackpot = tmpMega[0].strip('$')
    info['one']=power
    info['two']=mega
    return 1 


@app.route("/")
def index():

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")

    #if app_name:
    #    return f"Hello from {app_name} running in a Docker container behind Nginx!"

    info['index_active']='active'
    info['version']='v0.1'
    out = render_template("index.html", info=info)
    return out




@app.route("/julio")
def julio():

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")
    ret = get_jackpots()
    if app_name:
        return f"{app_name} julio's ret: {ret} mega: {mega} power: {power} "

    return "2: Hello from julio app route 2"



@app.route("/jackpotax")
def jackpotax():

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")
    ret=0
    ret=get_jackpots()
    info['jackpotax_active']='active'
    info['version']=str(ret)
    out = render_template("jackpotax.html", info=info)
    return out


@app.route("/rate")
def rate():
    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")
    info['rate_active']='active'
    info['version']='v0.1'
    rate={}
    rate['one']=1
    rate['two']=2
    out = render_template("rate.html", rate=rate, info=info)
    return out


@app.route("/countdown")
def countdown():
    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")
    info['countdown_active']='active'
    info['version']='v0.1'
    out = render_template("countdown.html", info=info)
    return out
