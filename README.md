# Weather Bot

## Setup

### Register Line@ Messaging API
Go to [Messaging API](https://business.line.me/zh-hant/services/bot) and register an account.

### Set credentials

First, must set the follow three variables.  
1. `SECRET_KEY`  
2. `LINE_CHANNEL_ACCESS_TOKEN`  
3. `LINE_CHANNEL_SECRET`  
4. `WEATHER_AUTHORIZATION_KEY`

You can do that by two ways:  
1. Set in environment variables.  
2. Set in `weather_bot/settings_secret.py`.  

### Deploy on HTTPS server

I choose [Heroku](https://dashboard.heroku.com/) to be the server. You can follow the step below to setup Heroku.  
1. Go to [Heroku](https://dashboard.heroku.com/) and sign up.  
2. Install [heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)  
3. And follow the below script.  

    $ heroku login

    $ cd weather_bot/
    $ git init
    $ heroku git:remote -a heroku_project_name

### Set Webhook URL
Go to **Line Developer** and set the webhook to `https://"your domain name"/bot/callback/`

## Usage

Add your Line Bot as your line friend by Line Bot ID or QRCode.

## Reference

- [My note](http://haotse-blog.logdown.com/posts/1193477)
