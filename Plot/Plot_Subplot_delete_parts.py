from tqdm import tqdm
import matplotlib.pyplot as plt

zoom_indx=300
#plt_t_min=4754
#plt_t_max=4757

plt_t_min=3600
plt_t_max=4600

plot_spacing=1000 #for speed, plot the once time every 10 time sliced

cartoon_spacing=100

plt_indx_min=np.argmin(abs(plt_t_min-time))
plt_indx_max=np.argmin(abs(plt_t_max-time))

fig = plt.figure(figsize=(10, 12))

ax_te_fit = fig.add_subplot(3, 2, 1)
ax_ne_fit = fig.add_subplot(3, 2, 2)

ax_te = fig.add_subplot(3, 2, (3,4))

ax_RMP = fig.add_subplot(3, 2, (5,6))

ax_te.imshow(np.array(profile_te_smooth_list[plt_indx_min:plt_indx_max+1:plot_spacing,zoom_indx:]).T,aspect='auto',cmap='inferno',\
               extent=[time[plt_indx_min], time[plt_indx_max],\
                       Z_smooth[zoom_indx:][-1], Z_smooth[zoom_indx:][0]])
ax_te.invert_yaxis()
ax_te.set_xlim(plt_t_min,plt_t_max)
ax_te.set_ylabel('Z (ms)')
ax_te.set_xlabel('ms')
ax_te.set_title(r'$T_e$')

ax_RMP.plot(actu_file['IU90']['xdata'][:],min(Z_smooth[zoom_indx:])+actu_file['IU90']['zdata'][:]*0.1**5,alpha=0.4,label='RMP')
ax_RMP.plot(time[plt_indx_min:plt_indx_max+1],mid_ped_te[plt_indx_min:plt_indx_max+1],color='blue',label='mid_pedestal')
ax_RMP.plot(time[plt_indx_min:plt_indx_max+1],top_ped_te[plt_indx_min:plt_indx_max+1],color='green',label='top_pedestal')
ax_RMP.plot(TS_file['TS.BLESSED.CORE.density']['xdata'][:],0.3+TS_file['TS.BLESSED.CORE.density']['zdata'][20,:]*0.1**20,color='green')
ax_RMP.plot(time[plt_indx_min:plt_indx_max+1],0.2+TS_ne_pred_roll_avg[plt_indx_min:plt_indx_max+1,20]*0.1**20,color='white')

Da=profile_file['fs00']['zdata'][:]*0.1**17*5
ax_RMP.plot(profile_file['fs00']['xdata'][:],Da+min(Z_smooth[zoom_indx:]),alpha=0.2,color='blue')
ax_RMP.set_xlim(plt_t_min,plt_t_max)
ax_RMP.set_ylim(Z_smooth[zoom_indx:][0],Z_smooth[zoom_indx:][-1])
ax_RMP.set_ylabel('a.u.')
ax_RMP.set_xlabel('ms')


for i in tqdm(range(plt_indx_min,plt_indx_max+1,cartoon_spacing)):
    
    
    ax_ne_fit.clear()
    ax_te_fit.clear()
    
    ax_ne_fit.plot(Z_smooth,profile_ne_smooth_list[i,:],color='orange')
    ax_ne_fit.scatter(TS_Z[:40],TS_ne_pred_roll_avg[i,:40]*0.1**19,s=1)
    ax_ne_fit.set_xlabel(r'$Z (m)$')
    ax_ne_fit.set_ylabel(r'$n_e (10^{19}m^{-3})$')
    ax_ne_fit.set_ylim(0,10)

    ax_te_fit.plot(Z_smooth,profile_te_smooth_list[i,:],color='orange')
    ax_te_fit.scatter(TS_Z[:40],TS_te_pred_roll_avg[i,:40]*0.1**3,s=1)
    ax_te_fit.set_xlabel(r'$Z (m)$')
    ax_te_fit.set_ylabel(r'$T_e (keV)$')
    ax_te_fit.set_ylim(0,10)
    
    for ax in [ax_te]:
        for line in ax.lines[:]:
            line.remove()

    ax_te.axvline(time[i],color='red') 
    
    plt.savefig(f'/scratch/gpfs/mc5076/Data/cartoon/{i}.png')#save the 
