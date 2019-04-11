#include <stdio.h>

bool hasAlternatingBits(int n) {
    int pre_bit = n & 1;
    int current_bit;
    while (n) {
      n >>= 1;
      current_bit = n & 1;
      if (current_bit == pre_bit) {
        return 0;
      }
      pre_bit = current_bit;
    }
    return 1;
}

int main(int argc, char const *argv[]) {
  for (int i = 0; i < 100; ++i) {
    printf("%d %d\n", i, hasAlternatingBits(i));
  }
  return 0;
}
