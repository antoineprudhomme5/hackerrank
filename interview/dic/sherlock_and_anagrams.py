def main(s):
  c = 0
  for l in range(1, len(s)):
    for i in range(0, len(s)-l):
      a = s[i:i+l]
      for j in range(i+1, len(s)-l+1):
        b = s[j:j+l]
        if sorted(a) == sorted(b):
          c = c + 1
  return c

main("abba")
main("kkkk")
main("mom")