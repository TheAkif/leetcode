func mySqrt(x int) int {
  if x < 2 {
    return x
  }
  for i := 1; i <= x; i++ {
    if i * i > x {
      return i-1
    }
  }
  return -1
}
