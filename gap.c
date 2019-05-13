
#include <stdio.h>
#include <math.h>

double delta( double q , double alpha , double Mach ){

   double qNL = 1.15/pow(Mach,3.);
   double qW = 6.1*qNL*pow(alpha*Mach,0.2);
   double delta = 1.0;
   if( q>qNL ) delta = qNL/q*exp( (q-qNL)/qW );

   return( delta );
}

double q_tilde( double q , double Mach , double r ){

   double D = 55.*Mach;

   return( q/sqrt( 1. + D*D*pow( pow(r,.25)-1. , 4. ) ) );

}

double S_gap( double q , double alpha , double Mach ){
   double d = delta( q , alpha , Mach );
   return( 1./( 1. + (0.45/3./M_PI)*q*q*pow(Mach,5.)/alpha*d ) );
}

double one_planet( double r , double rp , double alpha , double Mach, double q ){
   
   double qt = q_tilde( q , Mach , r/rp );
   double Sigma = S_gap( qt , alpha , Mach );

   return( Sigma );
}

int main(void){

   double S1 = 2.5;
   double k = 1.5;

   int N_planets = 2;
   double qs[3] = {7e-4,7e-4,3e-4};
   double rs[3] = {0.63,1.0,2.0};
   double alphas[3] = {0.01,0.01,0.01};
   double Machs[3] = {25.2,20.,25.};

   double Rmin = 0.03;
   double Rmax = 5.0;

   FILE * pFile = fopen("output.dat","w");
   int N = 1000;
   int i;
   for( i=0 ; i<N ; ++i ){
      double x = ((double)i+.5)/(double)N;
      double r = Rmin*pow(Rmax/Rmin,x);
      double Sigma = S1*pow(r,-k);
      int p;
      for( p=0 ; p<N_planets ; ++p ){
         Sigma *= one_planet( r , rs[p] , alphas[p] , Machs[p] , qs[p] );
      }
      fprintf(pFile,"%e %e\n",r,Sigma);
   }
   fclose(pFile);

   return(0);
}
