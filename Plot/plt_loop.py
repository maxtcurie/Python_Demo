import matplotlib.pyplot as plt
from tqdm import tqdm

spacing = 1000
image_path = './cartoon/'
time_min = 4095
time_max = 4105

# Find the indices for the minimum and maximum time
indx_min = np.argmin(np.abs(time_min - ECE_data['ece_time']))
indx_max = np.argmin(np.abs(time_max - ECE_data['ece_time']))

# Extract the relevant portion of ECE data just once
ECE_spec = ECE_data['ECE_sum'][indx_min:indx_max + 1, :]

# Create the figure and axes outside the loop. Use subplots_adjust to fine-tune spacing if necessary.
fig = plt.figure(figsize=(10, 6))
axs_ne = fig.add_subplot(2, 2, 1)
axs_te = fig.add_subplot(2, 2, 2)
axs_spec = fig.add_subplot(2, 2, (3,4))

# Initial plot setups for axs_ne and axs_te, which will be cleared and reused

# Display the unchanging ECE spectrum image outside of the loop
axs_spec.imshow(ECE_spec.T, aspect='auto', cmap='inferno', extent=[ECE_data['ece_time'][indx_min], ECE_data['ece_time'][indx_max], ECE_data['ece_freq'][-1], ECE_data['ece_freq'][0]])

for i in tqdm(range(0, len(indx_list), spacing)):
    indx = indx_list[i]

    # Clear previous scatter and line plots without affecting the ECE spectrum image
    axs_ne.clear()
    axs_te.clear()
    
    axs_ne.set_ylim(0, 6)
    axs_te.set_ylim(0, 5)  # Adjust if necessary for your TE data
    axs_spec.set_ylim(0, 100)
    
    axs_ne.set_xlabel('Z (m)')
    axs_te.set_xlabel('Z (m)')
    
    axs_ne.set_ylabel(r'$n_e (10^{19}m^{-3})$')
    axs_te.set_ylabel(r'$T_e (keV)$')
    # Plot for NE
    axs_ne.scatter(TS_RZ_file['S.BLESSED.CORE.Z']['zdata'][:40], TS_ne_pred_roll_avg[indx, :] * 0.1**19, alpha=0.2)
    axs_ne.plot(Z_smooth, profile_smooth_ne_list[i, :], ms=5, alpha=0.8, color='orange')
    
    # Assuming you have data to plot on axs_te, otherwise adjust this section
    # Plot for TE on the second y-axis sharing the same x-axis
    axs_te.scatter(TS_RZ_file['S.BLESSED.CORE.Z']['zdata'][:40], TS_te_pred_roll_avg[indx, :] * 0.1**3, alpha=0.2)  # Adjust values as needed
    axs_te.plot(Z_smooth, profile_smooth_te_list[i, :] * 1.1, ms=5, alpha=0.8, color='orange')  # Example adjustment

    # Update only the vertical line for each iteration
    for line in axs_spec.lines[:]:
        line.remove()
    axs_spec.axvline(time_sorted_roll_avg[indx], color='green')

    # Update title with the current index
    fig.suptitle(f't={time_sorted_roll_avg[indx]:.3f}')
    
    # Save each figure with the updated line and title
    plt.savefig(f"{image_path}{indx}.png")
    plt.tight_layout()
    plt.show()

plt.close(fig)  # Close the figure to free memory
