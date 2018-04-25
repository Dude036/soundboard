#!/usr/bin/python3
import os
import sys
import vlc
import time

inputs = ['\'1\'', '\'2\'', '\'3\'', '\'4\'', '\'5\'', '\'6\'', '\'7\'', '\'8\'', '\'9\'', '\'0\'']
special = ['\'*\'', '\'+\'', '\'-\'', '\'+\'', '\'/\'', '\'.\'']

instance = vlc.Instance('--input-repeat=999999')
player = instance.media_player_new()


def loadPresets():
	''' Get all the Presets in the current directory '''
	l = []
	for file in os.listdir(os.getcwd()):
	    if file.endswith(".preset"):
	        print("Preset Found:", os.path.join(os.getcwd(), file))
	        l.append(os.path.join(os.getcwd(), file))
	return l


def getPresetTracks(preset):
	''' Get all the links inside of a preset track '''
	l = []
	with open(preset) as file:
		for line in file:
			 # Need to get rid of those pesky \n's
			print(str(len(l)) + ': ', line[:-1])
			l.append(line[:-1])
	if len(l) < 10:
		print("Too little links. Cannot correctly populate.")
		l = []
	elif len(l) > 10:
		print("Too many links. Cannot correctly populate.")
		l = []
	return l


def isYouTubeAudio(link):
	import re
	if re.match(r'http[s]:\/\/www\.youtube\.com/watch\?v=([\w-]{11})', link) == None:
		return False
	else:
		return True
	

def getYouTubeAudioTrack(link):
	''' Get Audio track of a link '''
	import pafy

	video = pafy.new(link)
	bestaudio = video.getbestaudio()

	# print(bestaudio.url)
	return bestaudio.url


def playQuick(num):
	''' Make quick sound '''
	l = ['up.mp3', 'down.mp3', 'preset_change.mp3', 'startup.mp3']
	s = instance.media_new(os.path.join(os.getcwd(), l[num]))
	player.set_media(s)
	player.play()
	if num == 3:
		time.sleep(4)
	else:
		time.sleep(1)
	player.stop()


def switchPresets(readyPresets):
	playQuick(2)
	
	print("Ready to swap the preset. Loaded presets:")
	i = 0
	for link in readyPresets:
		print(i, "-", link)
		i += 1

	newPreset = input("What would you like your preset to be?: ")
	
	if newPreset.isdigit() and int(newPreset) < len(presetList):
		# Number preset. We're goood
		numPre = int(newPreset)
		print("New Preset: ", numPre)
		playQuick(0)
		return numPre
	else:
		# It's a character. Stop
		print("Invalid preset. Skipping.")
		playQuick(1)
		return None
		

def playTrack(track):
	''' Play an audio track indefinetly. Also awaits response so it can detect a change in information '''
	from readchar import readkey

	# Load and add media file
	media = instance.media_new(track)
	player.set_media(media)

	# Play
	player.play()

	# Pause before getting the status, to update everything
	print(str(player.get_state()) + "          ", end='\r')
	sys.stdout.flush()
	time.sleep(1)
	
	print(str(player.get_state()) + "          ")


if __name__ == '__main__':
	presetList = loadPresets()
	preset = getPresetTracks(presetList[0])
	
	# Start Up and initial setup
	active = False
	
	playQuick(3)

	import readchar

	keyInput = '\'0\''
	# Start Main loop
	print("Ready for input")
	while keyInput not in inputs or keyInput not in special:
		keyInput = repr(readchar.readkey())

		# Sanitize input
		if keyInput in inputs:
			# Play sound
			santized = int(keyInput[1])
			player.stop()
			active = True
			# print(preset[santized])
			if isYouTubeAudio(preset[santized]):
				playTrack(getYouTubeAudioTrack(preset[santized]))
			else:
				playTrack(preset[santized])

		# Special Characters
		elif keyInput == special[0]: # '\'*\'
			# Preset
			active = False
			player.stop()
			np = switchPresets(presetList)
			if np != None:
				preset = getPresetTracks(presetList[np])

		elif keyInput == special[1]: # '\'+\''
			# Play/Pause. +
			if active:
				player.pause()
				active = False
			else:
				player.play()
				active = True
		elif keyInput == special[2]: # '\'-\''
			pass

		elif keyInput == '\'x\'':
			# End case
			exit() 

