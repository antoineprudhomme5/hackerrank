object Solution {

    def main(args: Array[String]) {

        val n :Int = scala.io.StdIn.readInt()
        for (_ <- 1 to n) {
            val d :Double = scala.io.StdIn.readDouble()
            println(exp(d, 9))
        }
    }

    /**
     * Calculate exp(d) recursively. 
     * @param d : the target
     * @param p : the power (here we calculate exp with the 10 first terms)
     */
    def exp(d :Double, p :Int) :Double = {
        if (p == 0) {
            return 1
        } else {
            return (pow(d, p) / factorial(p)) + exp(d, p-1)
        }
    }

    def pow(n :Double, e:Int) :Double = {
        if (e == 0) {
            return 1
        }
        return n * pow(n, e-1)
    }

    def factorial(n :Int) :Int = {
        if (n == 1) {
            return 1
        }
        return n * factorial(n - 1)
    }
}
