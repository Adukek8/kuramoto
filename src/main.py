import numpy as np
import matplotlib.pyplot as plt
import consts
import kuramoto as kmto

def main():
    phase, nf = kmto.init_phase_and_freqs(consts.NUM_OSCILLATORS, consts.NATURAL_FREQUENCY_RANGE)
    print(phase)
    t = np.arange(0, consts.TIME, consts.TIME_STEP_DT)
    phase_history = np.zeros((len(t), consts.NUM_OSCILLATORS))
    phase_history[0] = phase
    
    for i in range(1, len(t)):
        phase = kmto.kuramoto(phase, nf, consts.COUPLING_STRENGTH)
        phase_history[i] = phase
    
    _, ax = plt.subplots(figsize=(8,5))

    for i in range(consts.NUM_OSCILLATORS):
        ax.plot(t, phase_history[:, i], 'b', alpha=0.1)
    
    ax.set_xlabel('Time')
    ax.set_ylabel('Phase')
    plt.show()

if __name__ == '__main__':
    main()