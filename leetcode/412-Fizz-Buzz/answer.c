// https://leetcode.com/problems/number-of-1-bits/

#include <stdio.h>
#include <stdlib.h>

#define MAX_LEN 16

char** fizzBuzz(int n, int* returnSize) {
    
    char **res;
    res = (char **)malloc(sizeof(char**) * n);

    int i, num;
    for (i = 0; i < n; i++) {
        res[i] = (char*)malloc(sizeof(char*) * MAX_LEN);
        num = i + 1;
        if (num % 3 == 0 && num % 5 ==0) {
            res[i] = "FizzBuzz";
        } else if (num % 3 == 0) {
            res[i] = "Fizz";
        } else if (num % 5 == 0) {
            res[i] = "Buzz";
        } else {
            sprintf(res[i], "%d", num);
        }
    }

    *returnSize = n;

    return res;
}
