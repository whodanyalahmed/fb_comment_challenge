# Facebook Post Comments Python Automation

## Getting started and installation

To get started with this software you need to clone this software on your pc or using zip for newbie...
and make sure you have a latest version of python installed after setting up everything you just need to install one library which is **Selenium** by opening *Command Prompt(CMD)* and type:

> pip install **selenium**

It will install latest version of selenium on your pc.

after that you need to find your chrome version and google chromedriver for your chrome compatible version and store it to **Driver** folder if you want to use in linux too then also download for linux too..I have already downlaoded **chromedriver v.83**.

## Support and Running program

This program support both linux and windows to run this you need to open terminal or cmd in a folder where is **app.py** is present after opening cmd/terminal you have to type:

-> for linux

> python3 app.py

-> for win
> python app.py

## Customization

### Number of comments

This is an python automation program using selenium which aims to work as a commentor....I made this because now a days challenges are coming if you do 1k comments or like this so I'll do this task...
So I made this automation which comments from 0 to 1k you can edit this on script *line 51*

> while(count <= **your number** )

You can also start your counter from whereever you want on *line 50*

> count = **your number**

But make sure your starting number is less then ending number so it works properly.

### How to add URL

To get started with the post you need to copy the post link and paste it on *line 46* but make sure you edit **www.** with **m.** to use mobile view to disable javascript.
