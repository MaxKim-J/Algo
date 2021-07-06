// 카카오 2021

function solution(id) {
  id = id
    .toLowerCase()
    .replace(/[~!@#$%^&*\(\)=+\[{\]}:?\,<>\/]/g, "") // 정규표현식 특수문자 /앞에 다는거..
    .replace(/\.\.+/g, ".");

  // js에서도 문자열 인덱싱 정도는 된다
  if (id[0] === ".") id = id.slice(1, id.length);
  if (id[id.length - 1] === ".") id = id.slice(0, id.length - 1);

  if (!id.length) id = "a";

  if (id.length >= 16) {
    id = id.slice(0, 15);
    if (id[id.length - 1] === ".") {
      id = id.slice(0, id.length - 1);
    }
  }

  if (id.length <= 2) {
    const tail = id[id.length - 1];
    while (id.length !== 3) {
      id += tail;
    }
  }

  return id;
}
