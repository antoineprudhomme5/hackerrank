def f(arr :List[Int]) :Int = {

    var sum :Int = 0

    for (a <- arr) {
        if (a % 2 != 0) {
            sum += a
        }
    }

    return sum
}