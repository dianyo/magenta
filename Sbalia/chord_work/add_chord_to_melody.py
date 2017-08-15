import my_constant as mc
from chord import rec_chord
import music21 as m21
from sys import argv
from os import listdir

def cMPairList2Score(cMPairList):
	score = m21.stream.Score()
	melodyPart = m21.stream.Part()
	chordPart = m21.stream.Part()
	woodblockPart = m21.stream.Part()
	melodyPart.append(m21.instrument.AcousticGuitar())
	chordPart.append(m21.instrument.AcousticGuitar())
	pm = m21.midi.percussion.PercussionMapper()
	woodblockPart.append(m21.instrument.Woodblock())

	cnt = 0.0
	for c, m in cMPairList:
		chordPart.append(m21.chord.Chord(c, duration=m21.duration.Duration(4.0)))
		for i in range(2):
			woodblockPart.append(m21.note.Note(36.0, quarterLength=2.0))
		for note in m:
			melodyPart.append(m21.note.Note(note[0], quarterLength=note[1]))

	score.insert(0, m21.tempo.MetronomeMark(number=120))
	score.insert(0, melodyPart)
	score.insert(0, chordPart)
	score.insert(0, woodblockPart)
	return score

inputFilenameList = [fn for fn in listdir(argv[1]) if (fn[-4:] == '.mid') and (fn[:3] != 'out')]

for s in inputFilenameList:
	input_ = m21.converter.parse(argv[1] + '/' + s)
	noteList = []
	for part in input_:
		for obj in part:
			if (type(obj) == m21.note.Note):
				noteList.append((obj.pitch.ps, obj.quarterLength))

	outCMPairList = []
	measureNoteList = []
	noteValueSum = 0
	for note in noteList:
		noteValueSum += note[1]
		if noteValueSum < 4.0:
			measureNoteList.append(note)
		else:
			measureNoteList.append((note[0], note[1] - (noteValueSum - 4.0)))
			outCMPairList.append((rec_chord(tuple(int(note[0]) for note in measureNoteList))[0][:3], measureNoteList))
			measureNoteList = []
			noteValueSum = 0.0
	if len(measureNoteList) != 0:
		outCMPairList.append((rec_chord(tuple(int(note[0]) for note in measureNoteList))[0], measureNoteList))
	
	outScore = cMPairList2Score(outCMPairList)
	outScore.write('midi', fp=argv[1] + '/' + 'out_'+s)
