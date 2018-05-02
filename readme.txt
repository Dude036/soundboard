Hello!

This is a Dungeon's and Dragon's ambience soundboard. Allow me to explain what each of the files means to you.
_______________________________________________________________

main.py : This is the main python file. This is what you'll need to run if you're wanting to use this script at all

#.preset: These contain the needed url links to various youtube videos containing ambience.
	You may make as many preset files as you want, and they are accessible to anyone who will follow a simple format
	First, you need to have 10 links. It will not accept more or less than 10 links
	Second, the first link will be attatched to the '0' key, and go in ascending order.
	Thirdly, the link must be either a file within the main directory, YouTube link, or a raw audio file URL
		See:
			- '0.preset' for full YouTube Link
			- '1.preset' for local files
			- '2.preset' for any other link 
	Fourthly, there should be no spaces on either side of the link. See any of the initial presets for demonstration
	Finally, make sure the preset file is in the same directory as the 'main.py' file

0.preset: This is the default soundboard to be used. It contains a wide variety of soundscapes for Dungeons and Dragons.
________________________________________________________________

How to get setup:
1. Install
	a. Python 3.6 
	b. pip3 (A Python package manager)
	c. VLC media player
2. Use pip3 to install these libraries
	a. python-vlc
	b. pafy
	c. youtube-dl
	d. readchar
3. Run the Application with the below command
	> python3 main.py
