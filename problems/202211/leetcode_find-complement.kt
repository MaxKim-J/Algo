// 이진수 보수 구하기

class Solution {
    fun findComplement1(num: Int): Int { //? 자료형
        var i = 0
        var j: Double = 0.0
        while(i < num){
            //? 캐스팅
            // 거듭제곱후 정수로 바꿈. Math.pow는 더블만 가능
            i = i + Math.pow(2.toDouble(), j).toInt()
            j = j + 1 // ? 형간 덧셈뺄셈?
        }

        return i - num
    }

    // 비트연산
    fun findComplement2(num: Int): Int {
        var cap = 1L // long, 1

        while (cap <= num) {
            cap = cap.shl(1) // shift left 비트연산자, 왼쪽으로 하나씩 옮기기
        }

        return (cap - 1).toInt().xor(num) // 정수로 바꾼다음에 두개 비트가 서로 다르면 1을 반환
    }
}

fun main() {
    val solution = Solution()
    val solution1 = solution.findComplement1(5)
    val solution2 = solution.findComplement2(10)

    println("솔루션 1: $solution1") //? 포매팅
    println("솔루션 2: $solution2")
}
