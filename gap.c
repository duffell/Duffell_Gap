
#include <stdio.h>
#include <math.h>

double delta( double q , double alpha , double Mach ){

   double qNL = 1.04/pow(Mach,3.);
   double qW = 34.*qNL*sqrt(alpha*Mach);
   double delta = 1.0;
   if( q>qNL ) delta = sqrt(qNL/q);
   delta += pow(q/qW,3.);

   return( delta );
}

double q_tilde( double q , double Mach , double alpha , double r ){

   double D = 7.*pow(Mach,1.5)/pow(alpha,1./4.);

   return( q/pow( 1. + D*D*D*pow( pow(r,1./6.)-1. , 6. ) , 1./3. ) );

}

double S_gap( double q , double alpha , double Mach ){
   double d = delta( q , alpha , Mach );
   return( 1./( 1. + (0.45/3./M_PI)*q*q*pow(Mach,5.)/alpha*d ) );
}

double one_planet( double r , double rp , double alpha , double Mach, double q ){
   
   double qt = q_tilde( q , Mach , alpha , r/rp );
   double Sigma = S_gap( qt , alpha , Mach );

   return( Sigma );
}

double sigma_backgnd( double r ){
   return( exp( -pow(r/80.,1.5) )*exp(-pow(r/110.,10.)) );
}

int main(void){

   int N_planets = 3;
   double qs[3] = {2.5e-4,2e-4,2e-4};
   double rs[3] = {13.1,33.0,68.6};
   double alphas[3] = {0.001,0.001,0.001};
   double Machs[3] = {10.0,12.0,14.0};

   double Rmin = 0.1;
   double Rmax = 130.0;

   FILE * pFile = fopen("output.dat","w");
   int N = 1000;
   int i;
   for( i=0 ; i<N ; ++i ){
      double x = ((double)i+.5)/(double)N;
      double r = Rmin*pow(Rmax/Rmin,x);
      double Sigma = sigma_backgnd( r );
      int p;
      for( p=0 ; p<N_planets ; ++p ){
         Sigma *= one_planet( r , rs[p] , alphas[p] , Machs[p] , qs[p] );
      }
      fprintf(pFile,"%e %e %e\n",r,Sigma,sigma_backgnd(r));
   }
   fclose(pFile);

   return(0);
}
