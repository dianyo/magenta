N_PC = 12
UNKNOWN_STR = 'unknown'
EPSILON = 2 ** -8

def createConsVec(cons_inv_list):
	vec = [False] * N_PC
	for i in cons_inv_list:
		vec[i] = True
	return vec

chordTypeList = [(0, 4, 7), (0, 3, 7), (0, 4, 8), (0, 3, 6)]
sortedChordList = [tuple(sorted([(pc + i) % 12 for pc in ct])) for ct in chordTypeList for i in range(N_PC)]
chordList = [tuple([(pc + i) % 12 for pc in ct]) for ct in chordTypeList for i in range(N_PC)]
sortedChord2IdxDict = {c: i for i, c in enumerate(sortedChordList)}
chord2IdxDict = {c: i for i, c in enumerate(chordList)}
stdConsInvList = [0, 3, 4, 5, 7, 8, 9]
triadConsInvList = [0, 3, 4, 5, 6, 7, 8, 9]
susConsInvLlist = [2, 5, 7, 10]
stdConsVec = createConsVec(stdConsInvList)
triadConsVec = createConsVec(triadConsInvList)
susConsVec = createConsVec(susConsInvLlist)
