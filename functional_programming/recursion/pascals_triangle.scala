object Solution {

    def main(args: Array[String]) {
        val k :Int = scala.io.StdIn.readInt()
        pascalTriangle(k)
    }

    def pascalTriangle(k :Int) :Unit = {
        for (n <- 0 to k - 1) {
            var line = new Array[Int](n + 1)
            for (r <- 0 to n) {
                line(r) = binomial(n, r)
            }
            println(line.mkString(" "))
        }
    }

    def factorial(n :Int) :Int = {
        if (n > 0) {
            return n * factorial(n - 1)
        }
        return 1
    }

    def binomial(n :Int, r: Int) :Int = {
        return factorial(n) / (factorial(r) * factorial(n - r))
    }
}