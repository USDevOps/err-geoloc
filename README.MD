[![Build Status](https://travis-ci.org/DennyZhang/err-geoloc.svg?branch=master)](https://travis-ci.org/DennyZhang/err-geoloc) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

[![Slack](https://www.dennyzhang.com/wp-content/uploads/sns/slack.png)](https://goo.gl/ozDDyL) [![Github](https://www.dennyzhang.com/wp-content/uploads/sns/github.png)](https://github.com/USDevOps/err-geoloc)


# Installing errbot
- Install errbot using `pip3 install errbot`
- create an errbot folder anywhere, and enter it
- Init the errbot installation with `errbot --init`
- Edit `config.py` and replace `CHANGE ME` by your name (any name will work for development) with a starting `@`
- Launch errbot using the `errbot` command

# Installing this plugin
- Start a conversation with your bot
- Install this plugin with `!repos install https://github.com/USDevOps/err-geoloc` (Note that you need to hit enter two times after typing any command on development mode)
    - (Alternatively, you can just clone the repo inside `plugins/err-geoloc` to make it easier to work on it)
- Verify that the plugin was installed using `!status plugin`

# Configure the plugin
- Send the following command to configure the plugin : `!plugin config geoloc {'json_path': '/your/path/user_db.json', 'unique_id': 'client', 'url': 'http://your.website/'}`
unique_id should be set to one of the values sent by !whoami (Different clients send different values)

# Using the plugin
- Send a private message to the bot (room messages can create issues depending on the chosen unique_id) with `!geoloc set New York`

# Development
errbot documentation is pretty extensive : http://errbot.io/en/latest/index.html

# Examples
There is a lot of different plugins to look at on this page : https://github.com/errbotio/errbot/wiki

# Maintainers
- Romain Brucker:[![LinkedIn](https://www.dennyzhang.com/wp-content/uploads/sns/linkedin.png)](https://www.linkedin.com/in/rbrucker/) [![Github](https://www.dennyzhang.com/wp-content/uploads/sns/github.png)](https://github.com/romainrbr/)
- [Denny Zhang](https://www.dennyzhang.com): [![LinkedIn](https://www.dennyzhang.com/wp-content/uploads/sns/linkedin.png)](https://www.linkedin.com/in/dennyzhang001) [![Github](https://www.dennyzhang.com/wp-content/uploads/sns/github.png)](https://github.com/DennyZhang) [![Twitter](https://www.dennyzhang.com/wp-content/uploads/sns/twitter.png)](https://twitter.com/dennyzhang001) [![Slack](https://www.dennyzhang.com/wp-content/uploads/sns/slack.png)](https://goo.gl/ozDDyL)
