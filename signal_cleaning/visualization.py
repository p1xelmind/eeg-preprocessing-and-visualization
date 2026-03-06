import mne
import matplotlib.pyplot as plt


def plot_epochs_overview(
        epochs: mne.Epochs,
        n_epochs: int = 5,
        n_channels: int = 10,
) -> None:
    epochs.plot(
        n_epochs=n_epochs,
        n_channels=n_channels,
        scalings="auto",
        block=True
    )


def plot_average_epoch(
        epochs: mne.Epochs
) -> None:
    evoked = epochs.average()

    evoked.plot(                #type: ignore
        spatial_colors=True,    #type: ignore
        gfp=True,
        time_unit="s"
    )


def plot_psd_epochs(
        epochs: mne.Epochs,
        fmin: float = 1.0,
        fmax: float = 40.0
) -> None:
    psd = epochs.compute_psd(   
        method="multitaper",
        fmin=fmin,              #type: ignore
        fmax=fmax
    )

    psd.plot(average=True)
    plt.show(block=True)


def plot_topomap(evoked, times=None):
    if times is None:
        times = [0.1, 0.3, 0.5, 0.7]

    evoked.plot_topomap(
        times=times,
        ch_type="eeg",
        time_unit="s",
        colorbar=True
    )
    plt.show(block=True)


def psd_before_after(
        raw: mne.io.BaseRaw,
        clean_raw: mne.io.BaseRaw,
        fmax: float = 40.0
) -> None:
    fig, ax = plt.subplots(figsize=(8, 4))

    raw.plot_psd(
        fmax=fmax,
        average=True,
        axes=ax,
        color="red",
        show=False    
    )
    
    clean_raw.plot_psd(
        fmax=fmax,
        average=True,
        axes=ax,
        color="blue",
        show=False
    )

    ax.lines[0].set_color("red")
    ax.lines[1].set_color("blue")
    ax.legend(["Raw EEG", "Cleaned EEG"])
    ax.set_title("PSD before and after ICA")

    plt.show(block=True)