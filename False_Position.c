//Printing the roots  of a equation using Regula-False Method
#include<stdio.h>
#include<conio.h>
#include<math.h>

float f(float x){
    return ((x * x) - x - 1);
}

int main(){
    float a, b, m, e = 0.0001;
    int i;

    printf("Enter a, b: ");
    scanf("%f %f", &a, &b);

    if ((f(a) * f(b)) > 0){
        printf("Invalid Intervals!");
    }
    else{
        m = (a * f(b) - b * f(a)) / (f(b) - f(a));
        i = 1;
        while (fabs(f(m)) > e){
            printf("\n %d %f %f %f %f \n", i, a, b, m, f(m));
            if (f(m) < 0){
                a = m;
            }
            else{
                b = m;
            }
            m = (a * f(b) - b * f(a)) / (f(b) - f(a));
            i++;
        }
        printf("\n %d %f %f %f %f \n", i, a, b, m, f(m));
        printf("The Root is: %f", m);
    }
    getch();
}