// https://leetcode.com/problems/reverse-bits/

uint32_t reverseBits(uint32_t n) {

  int i = 0;
  uint32_t reverse_num = 0;

  while (n) {
    reverse_num += ((n & 1) << (31 - i));
    n >>= 1;
    ++i;
  }

  return reverse_num;
}
