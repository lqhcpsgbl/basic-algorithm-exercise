// https://leetcode.com/problems/count-and-say/

#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_LEN 4096

char* next_num(char* num) {

  int count = 1;
  int index = 0, next_index = 0;

  int length = strlen(num);
  char *res = (char*)malloc(sizeof(char*) * (length*2));
  res[0] = '\0';

  char tmp_res[3];

  while (1) {
    next_index = index + 1;
    if (next_index >= length) {
      sprintf(tmp_res, "%d%c", count, num[index]);
      strcat(res, tmp_res);
      break;
    } else {
      if (num[index] == num[next_index]) {
        count++;
      } else {
        sprintf(tmp_res, "%d%c", count, num[index]);
        strcat(res, tmp_res);
        count = 1;
      }
    }
    index++;
  }

  return res;
}


char* countAndSay(int n) {
  char *res = (char*)malloc(sizeof(char*) * MAX_LEN);
  res[0] = '1';
  res[1] = '\0';
  int i;
  for (i = 1; i < n; i++) {
    res = next_num(res);
  }
  return res;
}

