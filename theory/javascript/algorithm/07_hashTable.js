// 해쉬 테이블, 해쉬 맵이라고도 한다
// 키-값 쌍을 저장하기 위해 사용함
// 빌트인 키-값쌍 저장 자료구조, 파이썬의 딕셔너리나 자스의 오브젝트 역시 해쉬 테이블의 아이디어를 사용함
// 키-값쌍 자료구조를 사용하는 이유 : 인덱스보다 문자열이 더 직관적이므로(human readability)
// 문자열 인덱스를 숫자로 바꿔서 저장 : 그렇게 바꿔주는게 해쉬함수(convert key into valid array indexes)
// 해쉬함수는 순수함수, 특정 값을 주면 항상 같은 값을 리턴. 거의 무한에 가까운 키값을 유한한 정수값으로 바꾸는 역할을 한다.

// 괜찮은 해쉬함수 : 빨라야함(접근시에도 맨날 호출하므로), 충돌이 적어야 함(저장 공간에 고르게 분포할 수 있도록), 결정적(순수함수 키값 하나에 해쉬값 하나)

// 충돌 해결 방법 : separate chaining(한 인덱스에 같이 저장), linear probing(충돌한 데이터를 다른빈칸으로 이동)
// 여기서는 separate chaining
class HashTable {
  // 처음 만들때 사이즈를 결정
  constructor(size = 53) {
    // array의 사이즈
    this.keyMap = new Array(size)
  }
  // key는 문자열이어야만 함
  _hash(key) {
    let total = 0;
    // 임의의 소수 : 테이블의 균일한 데이터 분포에 중요함, 소수를 쓰는게 충돌 방지에 중요(쿠오라-거의 3000분의 1)
    let WEIRD_PRIME = 31;
    // 사이즈 백개로 제한하는 듯
    // 백자 이상의 문자는 앞에 100개까지만 해쉬를 돌림(완벽한 해결책은 아님)
    for (let i = 0;i < Math.min(key.length, 100);i++) {
      let char = key[i]
      // utf-16 코드를 나타내는 0부터 65535 사이의 정수를 반환함
      // 96을 빼면 알파벳의 포지션이 나옴
      let value = char.charCodeAt(0) - 96

      // 모드연산으로 length 범위의 값이 나올 수 있도록 함
      total = (total + value) * WEIRD_PRIME  % this.keyMap.length
    }
  }

  set(key, value) {
    let index = this._hash(key);
    if(!this.keyMap[index]) {
      this.keyMap[index] = [];
    }
    // 배열에 넣는다
    this.keyMap[index].push([key, value])
  }

  get(key) {
    let index = this._hash(key);
    if(this.keyMap[index]) {
      // 인덱스에 접근해서 배열 탐색
      for(let i = 0;i < this.keyMap[index].length; i++) {
        if(this.keyMap[index][i][0] === key) {
          return this.keyMap[index][i][1]
        }
      }
    }
    return undefined
  }

  // 키 배열을 반환
  keys(){
    let keysArr = [];
    for(let i = 0; i < this.keyMap.length; i++){
      if(this.keyMap[i]){
        for(let j = 0; j < this.keyMap[i].length; j++){
          if(!keysArr.includes(this.keyMap[i][j][0])){
            keysArr.push(this.keyMap[i][j][0])
          }
        }
      }
    }
    return keysArr;
  }

// 값배열 반환
 values(){
    let valuesArr = [];
    for(let i = 0; i < this.keyMap.length; i++){
      if(this.keyMap[i]){
        for(let j = 0; j < this.keyMap[i].length; j++){
          if(!valuesArr.includes(this.keyMap[i][j][1])){
            valuesArr.push(this.keyMap[i][j][1])
          }
        }
      }
    }
    return valuesArr;
  }

}

// 시간 복잡도
// insert, deletion, access - 최적의 경우 상수시간
// 직결되는 변수는 데이터가 얼마나 테이블 내에서 고르게 분포되었는지임
// chaining일 경우 데이터가 많아질수록 O(n)에 가깝게 삽입삭제조회를 해냄
// value를 조회하고 싶을 경우 O(n) - 어디있는지 알아내야 해서