#include <stdio.h>

int afloor(float a)
{
	int temp;
	float diff;
	diff = a - (int)a;

	if (diff > 0.5)
	{
		temp = (int)a -1;
	}
	else
	{
		temp = (int)a;
	}
	//printf("%d, %d", (int)a, temp);
	return((int)temp);
}



int main()
{
	printf("Hello!!\nEnter a number: ");
	int no = 0;
	scanf("%d",&no);
	printf("The numer entered is: %d \n",no);
	for(int itr =0; itr< no; itr++)
	{
		for(int j =0 ; j <afloor((no-itr)/2);j++)
		{
			printf(" ");
		}
		for (int i=0; i<itr;i++)
		{
			printf("*");
		}
		printf("\n");
	}
	return(0);
}
