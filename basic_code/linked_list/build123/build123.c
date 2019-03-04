#include <stdio.h>
#include <stdlib.h>

struct node {
  int data;
  struct node* next;
};

struct node* Buildonetwothree() {
  struct node* one = NULL;
  struct node* two = NULL;
  struct node* three = NULL;

  one = malloc(sizeof(struct node));
  two = malloc(sizeof(struct node));
  three = malloc(sizeof(struct node));

  one->data = 1;
  one->next = two;

  two->data = 2;
  two->next = three;

  three->data = 3;
  three->next = NULL;

  return one;
}

void print_out(struct node* head) {
  if (head == NULL) {
    return 0;
  }
  struct node* temp = head;

  int len = 0;
  while (temp != NULL) {
    printf("node address is %p, data is %d, next address is %p\n", temp,
        temp->data, temp->next);
    temp = temp->next;
  }
}

int main(int argc, char const *argv[]) {
  // run as : tcc -run build123.c
  printf("length of Buildonetwothree is %d", length(Buildonetwothree()));
  return 0;
}