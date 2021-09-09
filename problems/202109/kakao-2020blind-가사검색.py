#! 70분, 정확성 다맞고 효율성에서 틀림
# 맵을 사용하기는 하지만 쌩노가다 완전탐색보다 조금 빠른 정도(효율성 3개 맞음)
'''
제일 최악 : 쿼리 하나에 모든 word를 하나씩 대조해서 풀이
내풀이 : word에 가능한 모든 쿼리를 도출해서 쿼리를 찾는 방법 
  - 쿼리와 word를 모두순회할 필요는 없어지는데 word하나당 모든 경우의 수를 도출해야함.
  - word의 개수가 커지면 커질수록 시간복잡도도 늘어남. 1만으로 충분히 커서 불가
해설의 풀이 : 이진탐색이나 트라이를 이용하여 queries에 맞는 word를 탐색함

* 선형적으로 순회하는 for문에서 시간이 너무 많이 들때, 그 수를 낮춘다고 해서 확 빨라지고 이러지는 않는듯 하다
* 데이터를 일관성있게 맞춰주고, 같은 로직으로 처리하는 방법을 고려해봐야 한다. 이 생각 잘 못하는듯
'''
def my_solution(words, queries):
    search_map={}
    
    def update_map(k):
        if search_map.get(k):
            search_map[k] += 1 
        else:
            search_map[k] = 1
            
    for w in words:
        length = len(w)

        for i in range(1, length):
            update_map('?'* i + w[i:])
            update_map(w[:i] + '?'*(length-i))
        
        update_map('?'*length)     

    answer = []
    
    for q in queries:
        if search_map.get(q):
            answer.append(search_map[q])
        else:
            answer.append(0)
            
    return answer


from collections import defaultdict

# Trie 자료구조안에 위치하고 있는 노드 정의
class Node(object):
    def __init__(self, key, passnumber=None, isEnd=None):
        self.key = key
        # 해당 노드를 지나간 길이 별 단어 갯수 => 이게 쿼리 탐색의 결과가 된다(물음표)
        self.passnumber = defaultdict(int)  
        self.isEnd = False
        self.children = {}

# Trie 자료구조
class Trie(object):
    def __init__(self):
        self.head = Node(None)

    # 새로운 단어 추가
    def insert(self, string):
        curr_node = self.head

        # head부터 passnumber을 모두 업데이트
        curr_node.passnumber[len(string)] += 1

        # 문자열을 탐색하면서 아래로 계속 내려감 
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char] # 이동
            curr_node.passnumber[len(string)] += 1

        curr_node.isEnd = True # 단어의 끝에는 표시를 해준다

    # 쿼리 단어에 일치하는 단어 수 반환 => passnumber
    def search(self, query):
        curr_node = self.head
        # 가장 가까운 물음표를 찾을때까지 내려간다 => 물음표를 모두 뒤에 몰았으니 ㄱㅊ
        for q in query:
            if q == "?": # !! 요 앞까지만 찾아보면 되기 때문에 물음표가 나오면 끝낸다
                break

            if q in curr_node.children:
                curr_node = curr_node.children[q]
            else:
                return 0 # 없음

        # 종착점 노드에서 쿼리의 길이만큼의 단어가 지나온 수
        # 그 다음 노드가 갈라지는 곳 까지는 관심없다(갈라지기 전에 답이 다 있음) + 단어의 개수는 matter 함
        return curr_node.passnumber[len(query)]


def trei_solution(words, queries):
    trie = Trie()
     # "?"가 앞에 있는 단어들을 뒤에서 부터 검사하기 위한 r_trie
    r_trie = Trie()
    # 단어 reverse
    r_words = [w[::-1] for w in words]
    # 중복되는 쿼리를 담기 위한 딕셔너리
    dic = {}
    answer = []

    for word in words:
        trie.insert(word)

    for word in r_words:
        r_trie.insert(word)

    for query in queries:
        if query in dic: # 중복되는 쿼리는 무시(메모이제이션)
            answer.append(dic[query])
            continue

        # 뒤가 물음표임
        if query.endswith("?"): # 아.........이게 있네
            result = trie.search(query)
            answer.append(result)
            dic["query"] = result
        else: # 앞이 물음표임
            result = r_trie.search(query[::-1]) # 뒤집어서 넣기
            answer.append(result)
            dic["query"] = result

    return answer