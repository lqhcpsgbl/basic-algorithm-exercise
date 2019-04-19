int* twoSum(int* nums, int numsSize, int target) {
    int* array = (int*)malloc(sizeof(int) * 2);
    int i;
    int j;
    for (i = 0; i < numsSize - 1; i++) {
        for (j = i + 1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                array[0] = i;
                array[1] = j;
                break;
            }
        }
    }
    return array;
}
