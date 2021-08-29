function solution(user, banned) {
  const table = [];
  banned.forEach((id) => {
    const regex = new RegExp(id.replace(/\*/g, "."));
    const tmpArr = [];

    user.forEach((userId, idx) => {
      if (regex.test(userId) && id.length === userId.length) {
        tmpArr.push(userId);
      }
    });

    table.push(tmpArr);
  });

  const answer = [];
  let count = 0;

  const recursion = (pick, table) => {
    if (pick.length === banned.length) {
      const isUnique = answer.every(
        (c) => pick.filter((p) => c.includes(p)).length !== pick.length
      );

      if (isUnique) {
        answer.push(pick);
        count += 1;
      }

      return;
    }

    for (let id of table[0]) {
      if (!pick.includes(id)) {
        recursion([...pick, id], table.slice(1));
      }
    }
  };

  recursion([], table);

  return count;
}
