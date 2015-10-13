#!/usr/bin/env python2.7  
   
   

import tweepy  
from subprocess import call  
from datetime import datetime  
       
i = datetime.now()               #take time and date for filename  
now = i.strftime('%Y%m%d-%H%M%S')  
photo_name = now + '.jpg'  
cmd = 'raspistill -t 500 -w 1024 -h 768 -o /home/pi/cam' + photo_name   
call ([cmd], shell=True)         #shoot the photo  
      
   
consumer_key = 'CONSUMERKEY'  
consumer_secret = 'SECRET'  
access_token = 'ACCESSTOKEN'  
access_token_secret = 'TOKENSECRET'  
      
    # OAuth process, using the keys and tokens  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)  
       
    # Creation of the actual interface, using authentication  
api = tweepy.API(auth)  
      
    # Send the tweet with photo and time 
photo_path = '/home/pi/cam' + photo_name  
status = 'Dexvision live update at: ' + i.strftime('%Y/%m/%d %H:%M:%S')   
api.update_with_media(photo_path, status=status) 