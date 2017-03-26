object Solution {

    def main(args: Array[String]) {
        var s :List[Char] = scala.io.StdIn.readLine().toList
        print(reduce(s))
    }

    def reduce(s: List[Char]) :String = {
        if (s.length > 0) {
            // get and remove the last char
            val last :Char = s.last
            var newS :List[Char] = s.dropRight(1)
            // use the char only if it's not in s
            if (newS.indexOf(last) > -1) {
                return reduce(newS)
            }
            return reduce(newS) + last
        }
        return ""
    }
}