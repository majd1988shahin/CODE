#include <iostream>
 
using namespace std;

// Base class
class Shape {
   public:
   	
  
      void setWidth(int w) {
         width = w;
      }
      void setHeight(int h) {
         height = h;
      }
      
   protected:
      int width;
      int height;
};

// Derived class
class Rectangle: public Shape {
   public:
      int getArea() { 
         return (width * height); 
      }
};

int main(void) {

auto numbers = std::vector<int> {1,2,3};

for(auto number : numbers) {
    std::cout << number << std::endl;
}
   Rectangle Rect;
 
   Rect.setWidth(5);
   Rect.setHeight(7);

   // Print the area of the object.
   cout << "Total area: " << Rect.getArea() << endl;
	
	
	//Shape a;
   return 0;
}
