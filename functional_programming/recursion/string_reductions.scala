object Solution {

    def main(args: Array[String]) {
        val s :String = scala.io.StdIn.readLine()
        print(reduce(s, Set[Char](), 0))
    }

    def reduce(s: String, used: Set[Char], i: Int) :String = {
        if (i < s.length) {
            if (used.contains(s(i))) {
                return reduce(s, used, i+1)
            }
            return s(i) + reduce(s,used + s(i) , i+1)
        }
        return ""
    }
}