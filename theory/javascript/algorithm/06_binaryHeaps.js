// 이진 맥스힙

class MaxBinaryHeap {
  constructor() {
    this.values = [];
  }
  insert(element) {
    this.values.push(element);
    this.hipifyUp();
  }
  hipifyUp() {
    // 끝에서부터 시작(리프에서부터 시작)
    let idx = this.values.length - 1;
    const element = this.values[idx];
    while(idx > 0) {
      // 이것은 파이썬의 //2
      // 힙의 부모 성질 이용
      let parentIdx = Math.floor((idx-1)/2)
      let parent = this.values[parentIdx];
      if(element <= parent) break;

      // 자식이 부모보다 더 클때 => 맥스힙이니까 
      // 부모와 자식이 위치를 바꿈
      this.values[parentIdx] = element;
      this.values[idx] = parent;
      
      // 그 다음 idx는 올라가서 부모 인덱스
      // 큰 값이 계속 올라가는 상황을 만듬
      idx = parentIdx;
    }
  }
}