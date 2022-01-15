class MaxBinaryHeap {
	public values:any[];

  constructor() {
    this.values = [];
  }

 // 리프 노드를 힙의 규칙에 따라 적합한 곳으로 이동시킴

  public insert(element) {
    this.values.push(element);
    this.heapifyUp();
  }

  public delete() {
		const last = this.values.length - 1;
		[this.values[0], this.values[last]] = [this.values[last], this.values[0]] 
    const result = this.values.pop();
    this.heapifyDown(0);
		return result
  }

	public sort() {
		const result = [];
		const length = this.values.length;
		for(let i = 0;i<length;i++) {
			[this.values[0], this.values[this.values.length - 1]]
					= [this.values[this.values.length - 1], this.values[0]];
			result.unshift(this.values.pop());
			this.heapifyDown(0);
		}
		return result;
	}

	private heapifyUp() {
    let idx = this.values.length - 1;
    while(idx > 0) {
      let parentIdx = Math.floor((idx-1)/2)
			// 부모보다 작으면 거기에 있는게 맞는 것
      if(this.values[idx] <= this.values[parentIdx]) break;
			[this.values[idx],this.values[parentIdx]]
				= [this.values[parentIdx],this.values[idx]]
      idx = parentIdx;
    }
  }

	// 루트 노드를 아래로 내리면서 힙의 규칙에 따라 적합한 곳으로 이동시킴
	private heapifyDown(idx:number) {
		if (!this.values.length) return;
		// 부모, 자식 두개 중에 가장 큰 값이 부모로 오는 꼴임
		while (idx * 2 + 1 < this.values.length) {
			let swap = idx;
			if (this.values[idx*2 + 1] > this.values[idx]) {
				swap = idx*2 + 1;
			}

			if (this.values[idx*2 + 2] > this.values[swap]) {
				swap = idx*2 + 2;
			}

			if (swap !== idx) {
				[this.values[idx],this.values[swap]] = [this.values[swap],this.values[idx]]
				idx = swap;
			} else {
				break
			}				
		}
	}

	private heapifyAll() {
		for (let i = Math.floor(this.values.length/2);i>-1;i-=1) {
			this.heapifyDown(i);
		}
	}
}


const heap  = new MaxBinaryHeap();

heap.insert(1);
heap.insert(8);
heap.insert(9);
heap.insert(2);
heap.insert(5);
heap.insert(3);
console.log(heap.values, '밸류');
console.log(heap.sort(), '정렬')

heap.insert(1);
heap.insert(8);
heap.insert(9);
heap.insert(2);
heap.insert(5);
heap.insert(3);
console.log(heap.values, '밸류');
console.log(heap.delete(), '삭제');
console.log(heap.values, '밸류');
console.log(heap.delete(), '삭제');
console.log(heap.values, '밸류');
console.log(heap.delete(), '삭제');
console.log(heap.values, '밸류');
console.log(heap.sort(), '정렬')

