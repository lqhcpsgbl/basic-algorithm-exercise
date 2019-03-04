#include <stdio.h>
#include <stdlib.h>

struct node {
  int data;
  struct node* next;
};

struct node* Buildn(int num) {
  struct node* head = NULL;
  head = malloc(sizeof(struct node));
  if (head == NULL) {
    exit(1);
  }

  struct node* temp = head;
  for (int i = 1; i <= num; i++) {
    struct node* newnode = malloc(sizeof(struct node));
    newnode->data = i;
    newnode->next = NULL;

    temp->next = newnode;
    temp = newnode;
  }

  return head;
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
  // run as : tcc -run buildn.c
  print_out(Buildn(10));
  return 0;
}
