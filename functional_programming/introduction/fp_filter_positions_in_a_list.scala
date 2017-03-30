def f(arr:List[Int]):List[Int] = {

    var output = List[Int]()

    for (i <- 0 to arr.length - 1) {
        if (i % 2 == 1) {
            output = output ::: List(arr(i))
        }
    }

    return output
}
