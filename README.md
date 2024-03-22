# The code for @dogpictures@convo.casa!

# Acknowledgements
This code used the **Quotable API** which was generously provided by **Luke Peavey**, you can [support him here](https://github.com/sponsors/lukePeavey)!
The code also used [dog.ceo](dog.ceo/dog-api)'s API to get the dog images, so please [donate to them here](https://paypal.me/dogapi)!

# What is this?
This is a small Python project that I made in 3 days or so, I don't really remember! 

# How does it work?
This bot will send a random dog image from the **dog.ceo** API if you hit the route **/post** with the following parameters:

``?pass={PASSWORD}``: the password so you can prevent others from abusing your thing
``?type=img``: specify that the type is img (image)

This bot will ALSO send a random quote from the **Quotable API** if you hit the route **/post** with the following parameters:

``?pass={PASSWORD}``: the password so you can prevent others from abusing your thing
``?type=text``: specify that the type is text

# SETUP

**HOW TO CREATE A BOT**
I recommend you to follow this **[guide](https://dev.to/botwiki/introduction-to-mastodon-bots-hfn)**

# ACTUAL SETUP
In your .env (or variables), create a variable named **"PASS"**, the value should be your password **(not the password to the Mastodon bot)**

You need to also add a variable called **"TOKEN"**, the value should be the access token (located in the Development section).

And the last variable you need to add is **"INSTURL"**. The value of the variable should be the instance URL (the instance where you made the bot account at), **INCLUDING THE FULL URL, IT SHOULD HAVE THE "https://" OR "http://"**

**Posting schedule**

The cons is that in the code, there is **no function for the bot to post on a schedule**, but you can use cron-job services online like [cron-job.org](console.cron-job.org)!
