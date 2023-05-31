import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def apply_average_pooling(spectrogram, pool_size,plot=False):
    reduced_spectrogram=signal.convolve2d(spectrogram, np.ones((pool_size, pool_size)), mode='valid')[::pool_size, ::pool_size]
    
    if plot:
        # Plot original and reduced spectrograms
        plt.figure(figsize=(10, 5))

        plt.subplot(1, 2, 1)
        plt.imshow(spectrogram, cmap='hot', aspect='auto')
        plt.title('Original Spectrogram')
        plt.xlabel('Frequency Bins')
        plt.ylabel('Time Frames')
        plt.colorbar()

        plt.subplot(1, 2, 2)
        plt.imshow(reduced_spectrogram, cmap='hot', aspect='auto')
        plt.title('Reduced Spectrogram')
        plt.xlabel('Frequency Bins (Reduced)')
        plt.ylabel('Time Frames (Reduced)')
        plt.colorbar()

        plt.tight_layout()
        plt.show()
        
    
    return reduced_spectrogram

# Generate mock spectrogram
np.random.seed(42)
num_frames = 100
num_bins = 80
spectrogram = np.random.rand(num_frames, num_bins)

# Apply average pooling
pool_size = 2
reduced_spectrogram = apply_average_pooling(spectrogram, pool_size,plot=True)