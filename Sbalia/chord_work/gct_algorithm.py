from itertools import combinations
import my_constant as mc

class My_GCT_Algorithm:
	def __init__(self, consVec=mc.stdConsVec):
		self.consVec = consVec
		self.N_PC = len(consVec)

	def isConsPcPair(self, pcPair):
		return self.consVec[(pcPair[1] - pcPair[0]) % self.N_PC]

	def findChord(self, pitchList, keyTonicPc=0):
		keyTonicPc = keyTonicPc % self.N_PC
		pcList = sorted(list(set(map(lambda pitch: (pitch - keyTonicPc) % self.N_PC, pitchList))))
		consPcTupleListList = [None] * (self.N_PC + 1)
		consPcTupleListList[2] = [pcPair for pcPair in combinations(pcList, 2) if self.isConsPcPair(pcPair)]
		if len(consPcTupleListList[2]) == 0:
			if len(pcList) == 0:
				return 0, []
			return 1, [(pc,) for pc in pcList]
		maxConsPcTupleLen = 2
		for pcTupleLen in range(3, len(pcList) + 1):
			consPcTupleListList[pcTupleLen] = []
			for pcTuple in combinations(pcList, pcTupleLen):
				if (pcTuple[:-1] in consPcTupleListList[pcTupleLen - 1]) and (pcTuple[1:] in consPcTupleListList[pcTupleLen - 1]) and (self.isConsPcPair((pcTuple[0], pcTuple[-1]))):
					consPcTupleListList[pcTupleLen].append(pcTuple)
			if len(consPcTupleListList[pcTupleLen]) != 0:
				maxConsPcTupleLen = pcTupleLen
			else:
				break
		maxConsPcTupleList = list(consPcTupleListList[maxConsPcTupleLen])
		consPcTupleListList = None
		
		return maxConsPcTupleLen, maxConsPcTupleList
	