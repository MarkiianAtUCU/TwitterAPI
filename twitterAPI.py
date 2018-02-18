import urllib.request
import urllib.parse
import urllib.error
import twurl
import ssl
import json

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_user_json(acct):
    """
    (str) -> dict

    Function gets info about user from twitter
    """
    TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '1'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    js = json.loads(data)
    return js


def get_user_friends_json(acct, num):
    """
    (str, int) -> dict
    
    Function gets info about defined amount of users friends from twitter
    """
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': str(num)})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    js = json.loads(data)
    return js


def json_get_user_info(acct):
    """
    (str) -> tuple

    Function returns info about user: location
                                      profile image url
                                      name
                                      friend number
                                      follower number
                                      date of creation
                                      language
    """
    js = get_user_json(acct)
    return (js[0]['user']['location'],
            js[0]['user']['profile_image_url_https'],
            js[0]['user']['name'],
            js[0]['user']['friends_count'],
            js[0]['user']['followers_count'],
            js[0]['user']['created_at'],
            js[0]['user']['lang'])


def json_get_user_friend_info(acct, num):
    """
    (str) -> tuple

    Function returns info about users friend: location
                                              profile image url
                                              name
                                              friend number
                                              follower number
                                              date of creation
                                              language
    """
    js = get_user_friends_json(acct, num)
    res = []
    for i in range(num):
        res.append((js['users'][i]['location'],
                    js['users'][i]['profile_image_url_https'],
                    js['users'][i]['name'],
                    js['users'][i]['friends_count'],
                    js['users'][i]['followers_count'],
                    js['users'][i]['created_at'],
                    js['users'][i]['lang']))
    return res
