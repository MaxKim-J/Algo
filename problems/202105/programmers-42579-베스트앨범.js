function solution(genres, plays) {
  let answer = []
  
  let countObj = {}
  let indexObj = {}
  
  genres.forEach((g, i) => {
      countObj[g] = countObj[g] === undefined ? plays[i] : countObj[g]+plays[i]
      indexObj[g] = indexObj[g] === undefined ? [i] : [...indexObj[g], i]
  })

  // 내림차순 정렬
  const gOrder = Object.entries(countObj).sort((a,b) => b[1]-a[1]).map((c) => c[0])
  
  for (const g of gOrder) {
      if (indexObj[g].length <= 1) {
          answer.push(indexObj[g][0])
      } else {
          // 재생 횟수에 대해 오름차순 정렬, 인덱스에 대해 내림차순 정렬
          indexObj[g].sort((a,b) => plays[a] === plays[b] ? a-b : plays[b] - plays[a])
          answer.push(indexObj[g][0])
          answer.push(indexObj[g][1])
      }
  }
  return answer
}

// 매우 깔끔한 함수형 프로그래밍 + play 빈도만으로 푸는 것도 가능했음

function solution(genres, plays) {
    var dic = {};
    // 빈도를 먼저 구해놓고
    genres.forEach((t,i)=> {
        dic[t] = dic[t] ?  dic[t] + plays[i] :plays[i];        
    });

    var dupDic = {};
    return genres          
          .map((t,i)=> ({genre : t, count:plays[i] , index:i})) // 장르 정보까지 한번에 밀어넣기
          .sort((a,b)=>{               
               if(a.genre !== b.genre) return dic[b.genre] - dic[a.genre];
               if(a.count !== b.count) return b.count - a.count;
               return a.index - b.index;
           })
           .filter(t=>  {
               if(dupDic[t.genre] >= 2) return false;
               dupDic[t.genre] = dupDic[t.genre] ? dupDic[t.genre]+ 1 : 1;
               return true;
            })
           .map(t=> t.index);    
}