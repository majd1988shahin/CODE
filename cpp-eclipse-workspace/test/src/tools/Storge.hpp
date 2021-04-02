// It is not possible to write the implementation of a template class in a separate cpp
#ifndef Storge_H
#define Storge_H
#include <iostream>
#include <string>
#include <vector>
//#include <memory>
using namespace std;

template <class T> class Storge
{
private:

public:
	unsigned i,j,N,SIZE;
	T data, *p;
	vector<T*> v;
	Storge(unsigned _N=10):i(0),j(0),N(_N),SIZE(0)
	{
		p=new T[N];
		v.push_back(p);
	}
	~ Storge()
	{
		for(int ii=0;ii<=i;ii++)
			this->v.clear();
	}
	bool push(const T& e);
	T & operator [](unsigned n) const;

};
template <class T>
bool Storge<T>::push(const T& e)
{
	if(j<N)
	{
		p[j]=e;
		j++;
		SIZE=i*N+j;
		return true;
	}
	else
	{
		p=new T[N];v.push_back(p);i++;
		j=0;
		SIZE=i*N+j;
		push(e);
	}
	return true;
}
template <class T>
T & Storge<T>::operator [](unsigned n) const
	{
		static T res;
		if (n>=SIZE)
			{
				std::cout<< "cannot access obj. "<<n<<" > max size("<<i*N+j<<")"<<std::endl;
				return res;
			}
		unsigned a=n/N,b=n%N;
		return v[a][b];

	}

#endif
