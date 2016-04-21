import itertools
import musicDictionary as md 

scale = 0

cycleScale = itertools.cycle(md.scales[scale])

def getModeScale(cycleScale, mode):
	modeScale = list()
	for i in range(mode):
		cycleScale.next()
	for i in range(7):
		modeScale.append(cycleScale.next())
	return modeScale

modeScale=getModeScale(cycleScale, 6)

for i in modeScale:
	print i
