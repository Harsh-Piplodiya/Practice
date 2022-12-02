//Finding the roots of a equation using fixed-point method
#include<stdio.h>
#include<conio.h>
#include<math.h>

float f(float x){
    return (sqrt(x  + 1));
}

int main(){
    float a, e, m, b;
    int i;

    printf("Enter a, e: ");
    scanf("%f %f", &a, &m);
    m = f(a);
    i = 1;
    while((b - a) <= e){
        printf("\n %d %f %f %f \n", i, a, m, f(m));
        b = m;
        m = f(b);
        i++;
    }
    printf("\n %d %f %f %f \n", i, a, m, f(m));
    return 0;
    getch();
}