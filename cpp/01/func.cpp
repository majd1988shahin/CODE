#include "func.h"
<<<<<<< HEAD
#include <cstdarg>
=======

>>>>>>> aae3d75c1a846f0cfdcd8f3430173ed0d283b9de
double average(int num,...) {
    /// num , is the number of arguments !!
   va_list valist;
   double dum;
   double sum = 0.0;
   int i;
   va_start(valist, num); //initialize valist for num number of arguments
   for (i = 0; i < num; i++) { //access all the arguments assigned to valist
      dum=(double) va_arg(valist, int);
      cout<<"func -> valist["<<i<<"]="<<dum<<endl;
      sum+=dum;
   }
   va_end(valist); //clean memory reserved for valist
   return sum/num;
<<<<<<< HEAD
}
=======
}
>>>>>>> aae3d75c1a846f0cfdcd8f3430173ed0d283b9de
