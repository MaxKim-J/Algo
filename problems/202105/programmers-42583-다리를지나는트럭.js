function solution(bl, w, tw) {
    let ans = 0
    let p = 0
    const bridge = Array.from({length: tw.length}, () => 0)
    const truckLength = bridge.length
    
    while (true) {
        ans += 1
        
        const onBridge = tw.reduce((acc,cur,idx) => {
            return acc + (bridge[idx] > 0 && bridge[idx] < bl ? cur:0)
        } , 0)
        
        const fwd = tw[p]
        if (onBridge + fwd <= w) {
            bridge[p] = -2 // 올리기 시작한 얘
            p += 1
        }
        
        // 다리에 있는 얘들 순회
        for (let i = 0;i < truckLength;i++) {
            if (bridge[i] > 0) {
                bridge[i] += 1
            }
            if (bridge[i] > bl) {
                bridge[i] = -1
            }
            if (bridge[i] === -2) {
                bridge[i] = 1
            }
        }
    
        
        if (bridge.every(t => t === -1)) {
            break
        }
    }
    return ans
}