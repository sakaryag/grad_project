from init import initiation

class PriorityQueue(object):
	def __init__(self):
		self.queue = []
	def __str__(self):
		return ' '.join([str(i) for i in self.queue])
		# for checking if the queue is empty
	def isEmpty(self):
		return len(self.queue) == 0

		# for inserting an element in the queue
	def insert(self, data):
		self.queue.append(data)
		# for popping an element based on Priority
	def delete(self):
		try:
			min = 0
			for i in range(len(self.queue)):
				if initiation.Job[self.queue[i]][3] < initiation.Job[self.queue[min]][3]:
					min = i
			item = self.queue[min]
			del self.queue[min]
			return item
		except IndexError:
			print()
			exit()
	def delete_dif(self):
		min = 0
		for i in range(len(self.queue)):
			if self.queue[i][1]+self.queue[i][2] < self.queue[min][1]+self.queue[min][2]:
				min = i

		item = self.queue[min]
		del self.queue[min]
		return item
