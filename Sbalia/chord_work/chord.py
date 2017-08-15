from sys import argv
from itertools import combinations, permutations
import my_constant as mc
from gct_algorithm import My_GCT_Algorithm
from directed_graph import Directed_Graph

ACYCLIC, CYCLIC, SUSPENDED, DIM_7, NO_CHORD = range(5)
chordTypeStrList = ['acyclic', 'cyclic', 'suspended', 'dim_7', 'no_chord']

def chord2MostCompactForm(chord):
	permutationList = list(permutations(chord))
	rangeList = [sum((pcTuple[i+1] - pcTuple[i]) % mc.N_PC for i in range(len(pcTuple) - 1)) for pcTuple in permutationList]
	minRange = min(rangeList)
	return [permutationList[i] for i, r in enumerate(rangeList) if r == minRange]

triadGctAlgo = My_GCT_Algorithm(mc.triadConsVec)
susGctAlgo = My_GCT_Algorithm(mc.susConsVec)

def rec_chord(pcTuple):
	pcTuple = tuple(set(int(p) % mc.N_PC for p in pcTuple))
	triadChordSize, triadChordList = triadGctAlgo.findChord(pcTuple)
	if triadChordSize < 3:
		susChordSize, susChordList = susGctAlgo.findChord(pcTuple)
		if susChordSize >= 3:
			chordType = SUSPENDED
			susChordMCFList = [mcf for c in susChordList for mcf in chord2MostCompactForm(c)]
		else:
			chordType = NO_CHORD
			noChordMCFList = [mcf for c in triadChordList for mcf in chord2MostCompactForm(c)]
	else:
		triadChordMCFList = [mcf for c in triadChordList for mcf in chord2MostCompactForm(c)]
		edgeList = [(iCiPair[0], jCjPair[0]) for iCiPair, jCjPair in permutations(enumerate(triadChordMCFList), 2) if iCiPair[1][1:] == jCjPair[1][:-1]]
		dg = Directed_Graph(len(triadChordMCFList), edgeList)
		maxPathLen, maxPathList = dg.findMaxPath()
		if maxPathLen == -1:
			chordType = CYCLIC
			minCycleLen, minCycleList = dg.findMinCycle()
			chordList = [[triadChordMCFList[triadIdx][0] for triadIdx in cycle] for cycle in minCycleList]
		else:
			chordType = ACYCLIC
			chordList = [[triadChordMCFList[triadIdx][0] for triadIdx in path[:-1]] + list(triadChordMCFList[path[-1]]) for path in maxPathList]

	if chordType == CYCLIC:
		return chordList
	elif chordType == ACYCLIC:
		return chordList
	elif chordType == SUSPENDED:
		return susChordMCFList
	elif chordType == NO_CHORD:
		return noChordMCFList
	return -1
