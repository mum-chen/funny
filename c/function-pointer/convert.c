#include <stdio.h>

enum CB_TYPE {
	CB_TYPE_0 = 0,
	CB_TYPE_1,
	CB_TYPE_2,
};

typedef void* (*CB)(void *);
typedef int (*CB_0)(void);
typedef int (*CB_1)(int arg0);
typedef int (*CB_2)(int arg0, int arg1);

int cb_switch(int type, CB cb, int arg0, int arg1)
{
	int res;
	CB_0 cb_0;
	CB_1 cb_1;
	CB_2 cb_2;
	switch(type) {
	case CB_TYPE_0:
		cb_0 = (CB_0)cb;
		res = cb_0();
		break;
	case CB_TYPE_1:
		cb_1 = (CB_1)cb;
		res = cb_1(arg0);
		break;
	case CB_TYPE_2:
		cb_2 = (CB_2)cb;
		res = cb_2(arg0, arg1);
		break;
	default:
		res = -1;
	}
	
	return res;
}

int cb_0(void)
{
	return 0;
}

int cb_1(int arg0)
{
	return arg0;
}

int cb_2(int arg0, int arg1)
{
	return arg0 + arg1;
}

int main(void)
{
	int res0, res1, res2;
	res0 = cb_switch(0, (CB)cb_0, 1, 2);
	res1 = cb_switch(1, (CB)cb_1, 1, 2);
	res2 = cb_switch(2, (CB)cb_2, 1, 2);

	printf("%d, %d, %d\n", res0, res1, res2);
	return 0;
}
