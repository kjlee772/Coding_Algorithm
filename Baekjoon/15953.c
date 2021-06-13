#include <stdio.h>
#include <stdlib.h>

int main() {
	int size;
	scanf("%d", &size);
	
	int* T = (int*)malloc(sizeof(int) * size);
	
	int a[] = { 0,500,300,300,200,200,200,50,50,50,50,30,30,30,30,30,10,10,10,10,10,10 };
	int b[] = { 0,512,256,256,128,128,128,128,64,64,64,64,64,64,64,64,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32 };

	int x, y;

	for (int i = 0; i < size; i++) {
		scanf("%d %d", &x, &y);
		if (x > 21) {
			x = 0;
		}
		if (y > 31) {
			y = 0;
		}
		T[i] = (a[x] + b[y])*10000;
	}

	for (int i = 0; i < size; i++) {
		printf("%d\n", T[i]);
	}

	return 0;
}