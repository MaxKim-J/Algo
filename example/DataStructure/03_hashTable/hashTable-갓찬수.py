# 갓찬수
# 사실 삭제까지 제대로 하려면 오지게 골치아픔

class HashOpenAddr:
	def __init__(self, size=10):
		self.size = size
    # Key와 value에 대한 배열을 따로 준비
		self.keys = [None]*self.size
		self.values = [None]*self.size

	def __str__(self):
		s = ""
		for k in self:
				if k == None:
						t = "{0:5s}|".format("")
				else:
						t = "{0:-5d}|".format(k)
				s = s + t
		return s

	def __iter__(self):
		for i in range(self.size):
				yield self.keys[i]

	def find_slot(self, key):
		i = self.hash_function(key)
		start = i
    # keys에 한번도 저장된 적이 없거나 이미 그 키값에 대한 값이 저장되어 있다면 탐색을 안함
		while (self.keys[i] != None) and (self.keys[i] != key):
      # 만약에 다른 값이 저장되어 있어 충돌이 발생한다면 다른 칸을 탐색함(한칸 옆으로)
			i = (i+1) % self.size
      # 한바퀴 다 돌았는데도 칸이 남은것이 없으면 해쉬 테이블이 다 찬 것이므로 안된다고 반환
			if i == start:
				i = None
				break
		return i

	def set(self, key, value=None):
		i = self.find_slot(key)
    # 꽉 차서 넣을 수가 없음
		if i == None:
			return None

    # key의 값이 None이 아닐때면 이미 있는 Key의 값을 수정하는 케이스
		if self.keys[i] != None:
			self.values[i] = value
    # key의 값이 None이면 처음 값을 저장하는 케이스(키 생성)
		else:
			self.keys[i] = key
			self.values[i] = value
		return i


	def hash_function(self, key):
			return key % self.size

	def remove(self, key):
		i = self.find_slot(key)
		
		if self.keys[i] == None:
			return None
		
		j = i
    # 일단 해당하는 값의 키를 지움
		self.keys[i] = None

		while True:
      # 기존 값에서 옆으로 한칸씩 이동하면서 이동할 해쉬값을 찾음
			j = (j+1) % self.size

			# 빈칸 만났을 때 -> 비로소 끝남
			if self.keys[j] == None:
				return i
				break

			k = self.hash_function(self.keys[j])

			# 다른 인덱스 키값을 가진 친구일때
			# 다 돌아봐서 빈칸으로 올릴 것을 search해줌
			# 조건에 안맞는게 나오고 나서, 이동 발생 안하고,나중에 j를 증가시켰을때 빈칸을 만나면 그때 끗
			if not (i<k<=j or j<i<k or k<=j<i):
				self.keys[i] = self.keys[j]
				self.keys[j] = None
				i = j


	def search(self, key):
		i = self.find_slot(key)
		if self.keys[i] != None:
			return self.keys[i]
		else:
			return None