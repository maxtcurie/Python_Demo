import numpy as np
import matplotlib.pyplot as plt

#https://matplotlib.org/3.1.1/gallery/ticks_and_spines/multiple_yaxis_with_spines.html

x=np.arange(0,6,0.001)
y1=np.sin(x)**2.
y2=2.*np.cos(x)**2.
y3=20.*np.cos(2.*x)**2.


def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)


fig, host = plt.subplots()
fig.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()

# Offset the right spine of par2.  The ticks and label have already been
# placed on the right by twinx above.
par2.spines["right"].set_position(("axes", 1.2))
# Having been created by twinx, par2 has its frame off, so the line of its
# detached spine is invisible.  First, activate the frame but make the patch
# and spines invisible.
make_patch_spines_invisible(par2)
# Second, show the right spine.
par2.spines["right"].set_visible(True)

p1, = host.plot(x, y1, "b-", label="y1")
p2, = par1.plot(x, y2, "r-", label="y2")
p3, = par2.plot(x, y3, "g-", label="y3")

host.set_xlim(np.min(x), np.max(x))
host.set_ylim(0, np.max(y1)*1.2)
par1.set_ylim(0, np.max(y2)*1.2)
par2.set_ylim(0, np.max(y3)*1.2)

host.set_xlabel("x_axis")
host.set_ylabel("y1_axis")
par1.set_ylabel("y2_axis")
par2.set_ylabel("y3_axis")

host.yaxis.label.set_color(p1.get_color())
par1.yaxis.label.set_color(p2.get_color())
par2.yaxis.label.set_color(p3.get_color())

tkw = dict(size=4, width=1.5)
host.tick_params(axis='y', colors=p1.get_color(), **tkw)
par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
par2.tick_params(axis='y', colors=p3.get_color(), **tkw)
host.tick_params(axis='x', **tkw)

lines = [p1, p2, p3]

host.legend(lines, [l.get_label() for l in lines])

plt.show()