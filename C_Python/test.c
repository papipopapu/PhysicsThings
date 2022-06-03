#include <stdio.h>
void bprint(double *v)
{
    printf("%f", v[0]);
    printf("%f", v[1]);
}
void bchange(double *v)
{
    v[0] = 6; v[1] = 9;
}
void bruh()
{
    double x[2];
    x[0] = 1; x[1] = 2;
    bchange(x);
    bprint(x);
}
int main()
{
    bruh();
    return 0;
}