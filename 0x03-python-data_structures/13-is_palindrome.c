#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head;
int stack[2048], top = 0;

/* Push the first half of the list onto the stack */
while (fast && fast->next)
{
stack[top++] = slow->n;
slow = slow->next;
fast = fast->next->next;
}

/* If the list has an odd number of elements, skip the middle element */
if (fast)
slow = slow->next;

/* Compare the second half of the list with the first half (in reverse order) */
while (slow)
{
if (slow->n != stack[--top])
return (0);
slow = slow->next;
}

return (1);
}
