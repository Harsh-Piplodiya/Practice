//Performing Bisection Method
#include<conio.h>
#include<stdio.h>
#include<math.h>

float f(float x){
    return(x * x - x - 1);
}

int main(){
    float a, b, m, e = 0.0001;
    int i;
    printf("\n Enter Values of a, b: ");
    scanf("%f %f", &a, &b);

    if(f(a) * f(b) > 0){
        printf("Invalid Intervals!");
    }
    else{
        m = (a + b) / 2;
        i = 1;
        while /* ((b - a) >= e) */ ((fabs(f(m))) > e){
            printf("\n %d %f %f %f %f \n", i, a, b, m, f(m));
            if (f(m) < 0){
                a = m;
            }
            else{
                b = m;
            }
            m = (a + b) / 2;
            i++;
        }
        printf("The Root is: %f", m);
    }
    return 0;
    getch();
}