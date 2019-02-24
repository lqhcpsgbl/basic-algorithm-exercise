package main

import (
  "fmt"
  "strconv"
)

func fizzBuzz(n int) []string {
  var res_slice []string
  res := ""
  for i := 1; i <= n; i++ {
    res = ""
    if i%3 == 0 {
      res += "Fizz"
    }
    if i%5 == 0 {
      res += "Buzz"
    }
    if res == "" {
      num_str := strconv.Itoa(i)
      res_slice = append(res_slice, num_str)
    } else {
      res_slice = append(res_slice, res)
    }
  }
  return res_slice
}

func main() {
  fmt.Println(fizzBuzz(15))
}
