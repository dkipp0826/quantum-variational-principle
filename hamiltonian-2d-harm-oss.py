#Add some more here
class Hamiltonian2DOscillator:
	def __init__(self, omega, m, lam):
		self.omega = omega
		self.mass = m
		self.lambda = lam
		
		
	#Computes the inner product <n|H|n>
	# where |n> is a 2 component wavefunction
	def product(n):
		return np.sum((n + 0.5) * omega)
		