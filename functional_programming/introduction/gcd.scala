def gcd(x: Int, y: Int): Int = y match {
    case 0 => x;
    case _=> gcd(y, x%y)
}