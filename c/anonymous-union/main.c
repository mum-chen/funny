#include <stdio.h>

struct attr{
	int age;
	int gender;
};

#define TEST_UNION(name)        \
union {                         \
	struct {                \
		int age;        \
		int gender;     \
	};                      \
				\
	struct attr name;       \
}

struct animal 
{
	int id; 
	TEST_UNION(attr);
};

int main()
{
	struct animal ani;
	ani.age = 10;
	struct attr *a = &ani.attr;
	printf("%d\n", a->age);
	return 0;
}
