
import math

#Only two parts of this code need to be modified by the user.  The "sigma_backgnd" function, and the values of qs, rs, alphas, Machs, and potentially Rmin, Rmax, Npts, which define the range and resolution you want to sample the disk model.

def delta( q = 1e-3 , alpha = 0.01 , Mach = 20. ):
	qNL = 1.04/Mach**3
	qW = 34*qNL*(alpha*Mach)**0.5
	delt = 1.0
	if( q>qNL ):
		delt = (qNL/q)**0.5
	delt += (q/qW)**3.
	return delt

def q_tilde( q = 1e-3 , alpha = 0.01 , Mach = 20. , r = 1.0 ):
	D = 7.*Mach**1.5/alpha**0.25
	qt = q/( 1 + D**3*( r**(1./6.) - 1. )**6 )**(1./3.)
	return qt

def S_gap( q = 1e-3 , alpha = 0.01 , Mach = 20. ):
	d = delta( q , alpha , Mach )
	S = 1./( 1. + (0.45/3./3.14159)*q**2*Mach**5/alpha*d )
	return S

def one_planet( r = 1.0 , rp = 1.0 , q = 1e-3 , alpha = 0.01 , Mach = 20. ):
	x = r/rp
	qt = q_tilde( q , alpha , Mach , x )
	Sigma = S_gap( qt , alpha , Mach )
	return Sigma

#The Background Density Profile:

def sigma_backgnd( r , disk_params ):
	S = math.exp( -(r/80.)**1.5 )*math.exp( -(r/110.)**10. )
	return S

def get_sigma( r , rs , qs , alphas , Machs , disk_params ):
        Sigma = sigma_backgnd( r , disk_params )
	Np = len(rs)
	for j in range(Np):
		Sigma *= one_planet( r , rs[j] , qs[j] , alphas[j] , Machs[j] )
	return( Sigma )
		
#Disk and Planet Parameters:

qs = [2.5e-4,2e-4,2e-4]
rs = [13.1,33.0,68.6]
alphas = [1e-3,1e-3,1e-3]
Machs = [10.,12.,14.]

#Potential Disk Parameters to Feed to sigma_backgnd:

disk_params = [1,2,3,4,5,6]

#Range and Resolution of Output:

Rmin = 0.1
Rmax = 130
Npts = 1000


for i in range(Npts):
	x = (i+.5)/Npts
	r = Rmin*(Rmax/Rmin)**x
	S_bkgnd = sigma_backgnd( r , disk_params )
	Sigma = get_sigma( r , rs , qs , alphas , Machs , disk_params )
	print r , Sigma , S_bkgnd

	

