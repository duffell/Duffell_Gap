
import math

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

def sigma_backgnd( r = 1.0 ):
	S = math.exp( -(r/80.)**1.5 )*math.exp( -(r/110.)**10. )
	return S




N_planets = 3
qs = [2.5e-4,2e-4,2e-4]
rs = [13.1,33.0,68.6]
alphas = [1e-3,1e-3,1e-3]
Machs = [10.,12.,14.]

Rmin = 0.1
Rmax = 130

Npts = 1000

Sigmas = [1]*Npts
S_bkgnd = [1]*Npts

for i in range(Npts):
	x = (i+.5)/Npts
	r = Rmin*(Rmax/Rmin)**x
	Sigma = sigma_backgnd(r)
	S_bkgnd[i] = Sigma
	for j in range(N_planets):
		Sigma *= one_planet( r , rs[j] , qs[j] , alphas[j] , Machs[j] )
	Sigmas[i] = Sigma
	print r,Sigmas[i], S_bkgnd[i]

	

