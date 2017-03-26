object Solution {

    def main(args: Array[String]) {
        val t :Int = scala.io.StdIn.readInt()
        for (_ <- 1 to t) {
            val s :String = scala.io.StdIn.readLine()
            val sLen :Int = s.length
            // print each rotation
            for (i <- 1 to sLen) {
                print(s.substring(i) + s.substring(0, i) + " ")
            }
            // new line before the next string to rotate
            print("\n")
        }
    }
}