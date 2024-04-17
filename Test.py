import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate2d

# Generate example spectrogram data (n_freq, n_time)
n_freq = 128
n_time = 256
spectrogram1 = np.random.rand(n_freq, n_time)
spectrogram2 = np.roll(spectrogram1, shift=(10, 5), axis=(0, 1))  # Shift the spectrogram

# Perform cross-correlation on the spectrograms
cross_correlation = correlate2d(spectrogram1, spectrogram2, mode='same', boundary='wrap')
print(np.shape(spectrogram1))
print(np.shape(cross_correlation))
print(np.shape(spectrogram2))
# Display the original and shifted spectrograms
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
plt.imshow(spectrogram1, cmap='viridis', aspect='auto', origin='lower')
plt.title('Spectrogram 1')
plt.colorbar()

plt.subplot(2, 2, 2)
plt.imshow(spectrogram2, cmap='viridis', aspect='auto', origin='lower')
plt.title('Spectrogram 2')
plt.colorbar()

plt.subplot(2, 1, 2)
plt.imshow(cross_correlation, cmap='viridis', aspect='auto', origin='lower')
plt.title('Cross-Correlation of Spectrograms')
plt.colorbar()

plt.tight_layout()
plt.show()
