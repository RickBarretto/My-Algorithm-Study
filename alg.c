// C Example:


// DIF
// C :

# include <stdio.h>

int main(){

    int D,d,R,Q;
    printf("Say two numbers, that the firs will be divided by the second for discover the rest of solution.\n");

    scanf("%d %d",&D,&d);
    printf("\n");

    Q = D/d;
    R = D - Q*d;

    printf("The Rest of %d/%d is %d, and the Result is %d.\n",D,d,R,Q);
}
