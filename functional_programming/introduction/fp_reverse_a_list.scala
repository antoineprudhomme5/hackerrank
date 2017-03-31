def f(arr :List[Int]) :List[Int] = {

    var out = List[Int]()

    for (a <- arr) {
        out ::= a
    }

    return out

}