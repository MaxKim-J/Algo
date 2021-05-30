function solution(participant, completion) {
  participant.sort()
  completion.sort()
  const length = participant.length
  for (let i = 0; i<length;i++) {
      if(participant[i] !== completion[i]) {
          return participant[i]
      }
  }
}