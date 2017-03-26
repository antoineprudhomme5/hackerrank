// return a copy of arr with each element replicated num times

def f(num :Int, arr :List[Int]) :List[Int] = {
    for (a <- arr; _ <- 1 to num) yield a
}