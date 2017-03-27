def f(delim :Int, arr :List[Int]) :List[Int] = {

    var ouput = List[Int]()

    for (i <- 0 to arr.length - 1) {
        if (arr(i) < delim) {
            ouput ::= arr(i)
        }
    }

    return output.reverse

}