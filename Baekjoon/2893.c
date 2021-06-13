#include <stdio.h>
#include <stdlib.h>

int main() {
	int count = 0;
	int sugar;
	scanf("%d", &sugar);
	while (sugar > 0) {
		if (sugar >= 3) {
			if (sugar > 0) {
				if (sugar % 5 == 0) {
					sugar -= 5;
					count++;
					continue;
				}
			}
			sugar -= 3;
			count++;
		}
		else
			break;
	}
	if (sugar == 0)
		printf("%d",count);
	else
		printf("-1");
	return 0;
}