import mne 

def plot_epochs_overwiev(
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