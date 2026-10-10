"""Generate an illustrative waveform/STFT/log-Mel figure, not patient audio."""
from pathlib import Path
import os
os.environ.setdefault("MPLCONFIGDIR", "/tmp/digital-scribe-mpl")
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
FS, DURATION = 16000, 1.8
t = np.arange(int(FS * DURATION)) / FS
rng = np.random.default_rng(7)
envelope = sum(np.exp(-((t - c) / w) ** 4) for c, w in [(0.30, .18), (.88, .22), (1.44, .20)])
phase = 2 * np.pi * np.cumsum(125 + 12 * np.sin(2 * np.pi * 1.8 * t)) / FS
signal = sum(np.sin(k * phase) / k for k in range(1, 18)) * envelope
signal += .025 * rng.normal(size=t.size)
signal /= np.max(np.abs(signal))
n_fft, hop = 400, 160  # 25 ms frames, 10 ms hop at 16 kHz
frames = np.lib.stride_tricks.sliding_window_view(signal, n_fft)[::hop]
power = np.abs(np.fft.rfft(frames * np.hanning(n_fft), axis=1)) ** 2
freq = np.fft.rfftfreq(n_fft, 1 / FS)
mel = lambda hz: 2595 * np.log10(1 + hz / 700)
hz = lambda mel_value: 700 * (10 ** (mel_value / 2595) - 1)
edges = hz(np.linspace(mel(0), mel(FS / 2), 42))
filters = np.zeros((40, len(freq)))
for i in range(40):
    filters[i] = np.maximum(0, np.minimum((freq - edges[i]) / (edges[i + 1] - edges[i]),
                                         (edges[i + 2] - freq) / (edges[i + 2] - edges[i + 1])))
mel_power = power @ filters.T
db = lambda a: 10 * np.log10(np.maximum(a / a.max(), 1e-7))
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9,
                     "text.color": "#183747", "axes.labelcolor": "#183747",
                     "xtick.color": "#62747E", "ytick.color": "#62747E",
                     "axes.spines.top": False, "axes.spines.right": False,
                     "axes.edgecolor": "#BCCAD0", "pdf.fonttype": 42})
fig, axes = plt.subplots(1, 3, figsize=(12.8, 3.15), gridspec_kw={"wspace": .38})
axes[0].plot(t, signal, color="#00547A", lw=.6)
axes[0].axvspan(.865, .890, color="#B75940", alpha=.25)
axes[0].set(title="1. Onda digitalizada", xlabel="Tiempo (s)", ylabel="Amplitud", xlim=(0, DURATION))
axes[0].annotate("ventana: 25 ms", (.878, .8), (.06, 1.2), arrowprops={"arrowstyle": "->", "color": "#B75940"}, color="#B75940", fontsize=8)
axes[0].set_ylim(-1.12, 1.45)
axes[1].imshow(db(power).T, origin="lower", aspect="auto", extent=[0, DURATION, 0, FS/2], cmap="viridis", vmin=-65, vmax=0, rasterized=True)
axes[1].set(title="2. Espectrograma (STFT)", xlabel="Tiempo (s)", ylabel="Frecuencia (Hz)", ylim=(0, 5000))
axes[2].imshow(db(mel_power).T, origin="lower", aspect="auto", extent=[0, DURATION, 0, 40], cmap="viridis", vmin=-65, vmax=0, rasterized=True)
axes[2].set(title="3. Energía en bandas Mel", xlabel="Tiempo (s)", ylabel="Índice de banda Mel")
fig.subplots_adjust(left=.06, right=.99, top=.85, bottom=.19)
fig.savefig(OUT / "signal_features.pdf", bbox_inches="tight", facecolor="white")
fig.savefig(OUT / "signal_features.png", dpi=170, bbox_inches="tight", facecolor="white")
plt.close(fig)
