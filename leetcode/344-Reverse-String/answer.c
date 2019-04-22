// https://leetcode.com/problems/reverse-string/

#include <string.h>

char* reverseString(char* s) {
    char *res;
    int length = strlen(s);
    res = (char*)malloc(sizeof(char*) * length);

    int i;
    for (i = 0; i < length; i++) {
        res[i] = s[length - 1 - i];
    }
    res[length] = '\0';

    return res;
}
