## Website Blocker 

This is a python script which runs in the background and blocks websites from being accessed during a particular time by redirecting the website to another address.


## Setup and Usage
1. On Windows, open Task Scheduler.
2. Create a task under the 'Actions" pane and give it a name.
3. Configure the task for your OS version.
4. Checklist 'Run with highest privileges' so the script can access the admin folders.
5. Go to triggers and choose when you want the script to run.
6. Under the action tab select 'Start a program' then locate the 'website_blocker' on your system and click 'OK'.
7. The script will run when next the pc is turned on or restarted.


## Video
A video on how to set up the script is also included.
![Watch the video](https://user-images.githubusercontent.com/101701760/162276355-84ccceac-2cab-442e-8fa4-bc27180c3552.mp4)

## Modifications
1. You can add as many sites to the script as you want just go to 'website_list' and a site to the list.
2. You can also edit the times at which the script blocks a website by going to line 17 and changing 8(starting hour of the script) and 15(ending hour of the script). 



