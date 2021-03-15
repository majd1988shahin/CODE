int maxsub_c(int *arr, int n, int *start, int *end) 
{

int max_sum = 0;

*start = 0;

*end = -1;

    for (int i=0; i < n; i++) 
    {
        int sum = 0;
         for (int j=i; j < n; j++) 
          { 
              sum += arr[j]; // sum == sum(arr[i..j])
              
              if (sum > max_sum) {
                  max_sum = sum;
                  *start = i;
                  *end = j;
                   }
          }
         }  
    return max_sum;  }