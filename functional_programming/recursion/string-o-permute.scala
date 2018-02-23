object Solution {
  def permute(s: String): String =
    s.sliding(2, 2).toList.map(_.reverse).mkString

  def main(args: Array[String]): Unit = {
    val nbTests: Int = scala.io.StdIn.readLine().toInt
    0.to(nbTests).foreach(_ => println(permute(scala.io.StdIn.readLine())))
  }
}
