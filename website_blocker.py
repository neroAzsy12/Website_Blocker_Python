# @author azsy
import time
from datetime import datetime as dt  # datetime can be written as dt instead of datetime

host_tmp = "testingHost.txt"        # Used this file to test blocker to see if it added and removed websites
host_path = r"/etc/hosts"           # this is the path to access hosts on mac
redirect_IPIV = "127.0.0.1"         # this is to block websites from IPV4
redirect_IPVI = "::1"               # this is to block websites from IPV6

# this is a list of websites that I used to see if the program functions correctly, try with other websites as well
website_list = ["coachbennyreeves.wordpress.com", "xcstats.com", "www.xcstats.com", "facebook.com", "linkedin.com/feed/", "www.facebook.com", "www.linkedin.com/feed/", "linkedin.com", "www.linkedin.com", "youtube.com", "www.youtube.com", "open.kattis.com"]

# this is an ifinite loop since the condition in the while loop will always be true
while True:
    # the conditional checks if the current time is in between 2 different times in order to add the websites to hosts
    if dt(dt.now().year, dt.now().month, dt.now().day, 15) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working Hours....")
        with open(host_path, 'r+') as file: # this opens the hosts file as readable and appendable
            content = file.read()
            for website in website_list: # for website in the list of websites for blocking
                if website in content:   # checks if the website is already added to the hosts file
                    pass                 # pass is basically skipping, since it won't need to do anything
                else:
                    file.write(redirect_IPIV + " " + website + "\n") # blocks websites from IPV4
                    file.write(redirect_IPVI + " " + website + "\n") # blocks websites from IPV6
    # this conditional block is used to remove the websites from the hosts file should it not
    else:
        print("Fun Hours")
        with open(host_path, 'r+') as file: # same thing as line 18
            content = file.readlines() # this will split the content as a list of lines of the hosts file
            file.seek(0)   # the cursor is placed at the 0 position in order to rewrite the hosts file as it was originally
            for line in content:
                if not any(website in line for website in website_list): # if the current line is not a website from the website list
                    file.write(line) # then it will write the line for the hosts file
            file.truncate() # this will delete anything below last line added to the file, basically reverts the hosts file into its original state
    time.sleep(15)
