# 못품

'''
1. 변수는 그냥 식별이 잘 되는걸로 하자 길더라도. 짧은거 하는게 크게 이점은 없는거같음 헷갈리고
2. BFS로 접근을 했는데 오히려 연산이 더 많아지는 케이스. 완전탐색으로 접근하는게 나았음
3. 문제를 또 잘 못 파악했음 방향은 2개(시계, 반시계)가 될 수 있었음
4. 시작점 자체에 대한 순회, 친구들의 순서에 대한 순회를 모두 해야한다 => 모든 것을 예측 가능하게 세팅하자 좋은 방식으로 일반화하기
'''

from itertools import permutations

def solution(n, weak, dist):
    weak_length = len(weak)
    
    # 취약지점 배열을 2배로 늘려주고 n만큼 더해준다
    for i in range(weak_length):
        weak.append(weak[i] + n)

    # 답 초기화        
    answer = len(dist) + 1
    
    # 취약지점의 개수만큼 순회한다
    for i in range(weak_length):
        
        # 취약지점의 탐색 시작점을 만든다. 특정 취약지점의 시작점부터 한바퀴에 이르는 범위다
        # 시작점을 기준으로 한바퀴를 뜯어내는 느낌이다 이 한바퀴가 어떻게됐든 친구 몇명으로 모두 커버가 되면
        # 친구들을 통해 취약지점 접근이 가능하다는 이야기가 된다
        # weak length와 개수가 같다
        start_point = [weak[j] for j in range(i, i+weak_length)]

        # 친구들의 순서 순열의 모든 경우의 수를 구한다(순서를 생각해야 하는 경우이므로 순열)
        candidates = permutations(dist, len(dist))
        
        # 가능한 모든 친구 순서에 대해 순회한다
        for order in candidates:
            friend_idx, friend_count = 0, 1

            # weak의 탐색 범위에 지금 등판한 친구의 거리의 합 => 탐색이 가능한 범위의 길이
            possible_check_length = start_point[0] + order[friend_idx]
            
            for idx in range(weak_length):
                # 한바퀴 범위에서 순회하면서 확인할 수 있는 최대 거리를 넘어설 경우
                # weak을 순서대로 순회하는데 커버가 안되는 범위가 있을 경우
                #! weak을 중심으로 순회를 해서 커버가 가능한 모든 범위를 알아내는 느낌
                if start_point[idx] > possible_check_length:
                    # 다음 친구를 투입하고
                    friend_count += 1
                    # 더이상 투입 못하는 경우 break(친구를 이미 다 투입했음)
                    if friend_count > len(order):
                        break
                    # 다음 친구 투입하고 친구가 확인할 수 있는 최대 거리를 업데이트 한다
                    #! 이전 친구가 커버 가능한 지점에서부터 다시 시작함
                    friend_idx += 1
                    possible_check_length = order[friend_idx] + start_point[idx]
                    
            answer = min(answer, friend_count)
    
    # answer의 초기값이 그대로면 걍 안되는거
    if answer > len(dist):
        return -1

    return answer

                    
                