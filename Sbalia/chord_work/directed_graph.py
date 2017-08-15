class Directed_Graph:
	def __init__(self, nNode, edgeList):
		self.nNode = nNode
		self.outAdjList = [[] for i in range(self.nNode)]
		for i, j in edgeList:
			self.outAdjList[i].append(j)

	def floydWarshallAlgorithm(self):
		distMat = [[self.nNode + 1] * self.nNode for i in range(self.nNode)]
		nextMat = [[-1] * self.nNode for i in range(self.nNode)]
		for i in range(self.nNode):
			for j in self.outAdjList[i]:
				distMat[i][j] = 1
				nextMat[i][j] = j

		for k in range(self.nNode):
			for i in range(self.nNode):
				for j in range(self.nNode):
					if distMat[i][k] + distMat[k][j] < distMat[i][j]:
						distMat[i][j] = distMat[i][k] + distMat[k][j]
						nextMat[i][j] = nextMat[i][k]

		return distMat, nextMat

	def getCyclePath(self, i, nextMat):
		if nextMat[i][i] == -1:
			return -1

		nodeList = [i]
		thisNode = nextMat[i][i]
		while thisNode != i:
			nodeList.append(thisNode)
			thisNode = nextMat[thisNode][i]
		nodeList.append(thisNode)

		return nodeList

	def rotateCycle(self, cycle):
		minIdx = cycle.index(min(cycle))
		return cycle[minIdx:] + cycle[:minIdx]

	def findMinCycle(self):
		distMat, nextMat = self.floydWarshallAlgorithm()
		minCycleLen = self.nNode + 1
		minCycleStartNodeList = []

		for i in range(self.nNode):
			if distMat[i][i] <= minCycleLen:
				if distMat[i][i] < minCycleLen:
					minCycleLen = distMat[i][i]
					minCycleStartNodeList.clear()
				minCycleStartNodeList.append(i)

		if minCycleLen == self.nNode + 1:
			return -1, -1

		cycleList = list(set(tuple(self.rotateCycle(self.getCyclePath(i, nextMat)[:-1])) for i in minCycleStartNodeList))
		return minCycleLen, cycleList

	def topoSort(self):
		inAdjList = [[] for i in range(self.nNode)]
		for i, jList in enumerate(self.outAdjList):
			for j in jList:
				inAdjList[j].append(i)
		sortedNodeList = []
		frontierList = [j for j, iList in enumerate(inAdjList) if len(iList) == 0]

		while len(frontierList) != 0:
			i = frontierList.pop()
			sortedNodeList.append(i)
			for j in self.outAdjList[i]:
				inAdjList[j].remove(i)
				if len(inAdjList[j]) == 0:
					frontierList.append(j)

		if any(map(lambda iList: len(iList) > 0, inAdjList)):
			return -1
		return sortedNodeList

	def backtrackPathRecur(self, thisNode, prevNodeListList):
		if thisNode == -1:
			return [[]]
		return [remainingPath + [thisNode] for prevNode in prevNodeListList[thisNode] for remainingPath in self.backtrackPathRecur(prevNode, prevNodeListList)]

	def findMaxPath(self):
		maxInPathLenList = [0] * self.nNode
		maxInPathPrevNodeList = [[-1] for i in range(self.nNode)]
		sortedNodeList = self.topoSort()
		if sortedNodeList == -1:
			return -1, -1

		for i in sortedNodeList:
			for j in self.outAdjList[i]:
				pathLen = maxInPathLenList[i] + 1
				if pathLen >= maxInPathLenList[j]:
					if pathLen > maxInPathLenList[j]:
						maxInPathLenList[j] = pathLen
						maxInPathPrevNodeList[j].clear()
					maxInPathPrevNodeList[j].append(i)

		maxPathLen = max(maxInPathLenList)
		minPathList = [path for endNode, maxInPathLen in enumerate(maxInPathLenList) if maxInPathLen == maxPathLen for path in self.backtrackPathRecur(endNode, maxInPathPrevNodeList)]
		return maxPathLen, minPathList
