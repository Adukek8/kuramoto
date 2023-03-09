import numpy as np

def kuramoto(phase, nf, coupling_strength):
    N = len(phase)
    sin_diff = np.sin(phase.reshape(N, 1) - phase)
    return (nf + coupling_strength / N * np.sum(sin_diff, axis=1)) % (2*np.pi)

def init_phase_and_freqs(N, nf_range):
    phase = np.random.rand(N) * 2*np.pi
    nf = np.random.uniform(*nf_range, size=N)
    return phase, nf