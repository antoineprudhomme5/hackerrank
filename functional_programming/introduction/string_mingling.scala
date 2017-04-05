object Solution {

    def main(args: Array[String]) {

        val p :String = scala.io.StdIn.readLine()
        val q :String = scala.io.StdIn.readLine()

        println(mingling(p, q))

    }

    def mingling(p :String, q :String) :String = {

        return p.toList.zip(q.toList).map(t => t._1 + "" + t._2).mkString

    } 

}