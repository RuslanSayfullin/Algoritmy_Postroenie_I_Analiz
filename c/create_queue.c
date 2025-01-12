#include <stdio.h>
#include <stdlib.h>

// Структура для хранения элемента очереди
typedef struct Node {
    int value;
    struct Node* next;
} Node;

// Структура для хранения очереди
typedef struct Queue {
    Node* front; // Указатель на передний элемент очереди
    Node* rear; // Указатель на задний элемент очереди
} Queue;

// Создание пустой очереди
Queue* createQueue() {
    Queue* queue = (Queue*)malloc(sizeof(Queue));
    queue->front = NULL;
    queue->rear = NULL;
    return queue;
}

// Проверка, пуста ли очередь
int isEmpty(Queue* queue) {
    return (queue->front == NULL);
}

// Добавление элемента в задний конец очереди
void enqueue(Queue* queue, int value) {
    // Создание нового элемента
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->value = value;
    newNode->next = NULL;
    
    // Если очередь пуста, задний и передний элементы будут указывать на новый элемент
    if (isEmpty(queue)) {
        queue->front = newNode;
        queue->rear = newNode;
        return;
    }
    
    // Иначе обновление указателя заднего элемента
    queue->rear->next = newNode;
    queue->rear = newNode;
}

// Удаление элемента из переднего конца очереди
int dequeue(Queue* queue) {
    if (isEmpty(queue)) {
        printf("Очередь пуста.\n");
        return -1;
    }
    
    // Сохранение значения переднего элемента
    int value = queue->front->value;
    
    // Обновление указателя переднего элемента
    Node* temp = queue->front;
    queue->front = queue->front->next;
    free(temp);
    
    // Если очередь пуста, обновление указателя заднего элемента
    if (isEmpty(queue)) {
        queue->rear = NULL;
    }
    
    return value;
}

// Вывод элементов очереди
void printQueue(Queue* queue) {
    if (isEmpty(queue)) {
        printf("Очередь пуста.\n");
        return;
    }
    
    Node* current = queue->front;
    while (current != NULL) {
        printf("%d ", current->value);
        current = current->next;
    }
    printf("\n");
}

// Освобождение памяти, занятой очередью
void freeQueue(Queue* queue) {
    Node* current = queue->front;
    while (current != NULL) {
        Node* temp = current;
        current = current->next;
        free(temp);
    }
    free(queue);
}

int main() {
    Queue* queue = createQueue();
    
    enqueue(queue, 1);
    enqueue(queue, 2);
    enqueue(queue, 3);
    
    printf("Очередь: ");
    printQueue(queue);
    
    printf("Удален элемент из очереди: %d\n", dequeue(queue));
    
    printf("Очередь после удаления: ");
    printQueue(queue);
    
    freeQueue(queue);
    
    return 0;
}
