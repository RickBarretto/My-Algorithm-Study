// C Example:

# include <stdio.h>

int main(){

    // defining The Dividend, Divisor, Rest and Quotient
    int D, d, R, Q;
    printf("Say two numbers, that the first will be divided by the second for discover the rest of solution.\n");

    scanf("%d %d",&D,&d);
    printf("\n");

    Q = D/d;
    R = D - Q*d;

    printf("The Rest of %d/%d is %d, and the Result is %d.\n",D,d,R,Q);
}
