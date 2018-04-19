#include <stdio.h>
/* print Fahrenheit-Celsius table
   for fahr = 0, 20, ..., 300 */
main()
{ int fahr, celsius;
  int upper, step;
  // lower = 0;
  int lower = 0;
  upper = 300;
  step = 20;
  /* lower limit of temperature scale */
  /* upper limit */
  /* step size */
  fahr = lower;
  while (fahr <= upper) {
    celsius = 5 * (fahr-32) / 9;
    printf("%d\t%d\n", fahr, celsius);
    fahr = fahr + step;
  }
}
