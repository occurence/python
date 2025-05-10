import pandas as pd
import torchmetrics
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from torch.nn import CrossEntropyLoss
import torchvision.transforms as transforms
from torchvision.datasets import CIFAR10
from torch.utils.data import DataLoader, TensorDataset

dataloader = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\20_Course_Introduction_to_Deep_Learning_with_PyTorch\datasets\dataloader.csv')

class ImageGrid(Grid):
    # docstring inherited

    _defaultCbarAxesClass = CbarAxes

    @_api.delete_parameter("3.3", "add_all")
    def __init__(self, fig,
                 rect,
                 nrows_ncols,
                 ngrids=None,
                 direction="row",
                 axes_pad=0.02,
                 add_all=True,
                 share_all=False,
                 aspect=True,
                 label_mode="L",
                 cbar_mode=None,
                 cbar_location="right",
                 cbar_pad=None,
                 cbar_size="5%",
                 cbar_set_cax=True,
                 axes_class=None,
                 ):
        """
        Parameters
        ----------
        fig : `.Figure`
            The parent figure.
        rect : (float, float, float, float) or int
            The axes position, as a ``(left, bottom, width, height)`` tuple or
            as a three-digit subplot position code (e.g., "121").
        nrows_ncols : (int, int)
            Number of rows and columns in the grid.
        ngrids : int or None, default: None
            If not None, only the first *ngrids* axes in the grid are created.
        direction : {"row", "column"}, default: "row"
            Whether axes are created in row-major ("row by row") or
            column-major order ("column by column").  This also affects the
            order in which axes are accessed using indexing (``grid[index]``).
        axes_pad : float or (float, float), default: 0.02in
            Padding or (horizontal padding, vertical padding) between axes, in
            inches.
        add_all : bool, default: True
            Whether to add the axes to the figure using `.Figure.add_axes`.
            This parameter is deprecated.
        share_all : bool, default: False
            Whether all axes share their x- and y-axis.
        aspect : bool, default: True
            Whether the axes aspect ratio follows the aspect ratio of the data
            limits.
        label_mode : {"L", "1", "all"}, default: "L"
            Determines which axes will get tick labels:

            - "L": All axes on the left column get vertical tick labels;
              all axes on the bottom row get horizontal tick labels.
            - "1": Only the bottom left axes is labelled.
            - "all": all axes are labelled.

        cbar_mode : {"each", "single", "edge", None}, default: None
            Whether to create a colorbar for "each" axes, a "single" colorbar
            for the entire grid, colorbars only for axes on the "edge"
            determined by *cbar_location*, or no colorbars.  The colorbars are
            stored in the :attr:`cbar_axes` attribute.
        cbar_location : {"left", "right", "bottom", "top"}, default: "right"
        cbar_pad : float, default: None
            Padding between the image axes and the colorbar axes.
        cbar_size : size specification (see `.Size.from_any`), default: "5%"
            Colorbar size.
        cbar_set_cax : bool, default: True
            If True, each axes in the grid has a *cax* attribute that is bound
            to associated *cbar_axes*.
        axes_class : subclass of `matplotlib.axes.Axes`, default: None
        """
        self._colorbar_mode = cbar_mode
        self._colorbar_location = cbar_location
        self._colorbar_pad = cbar_pad
        self._colorbar_size = cbar_size
        # The colorbar axes are created in _init_locators().

        if add_all:
            super().__init__(
                fig, rect, nrows_ncols, ngrids,
                direction=direction, axes_pad=axes_pad,
                share_all=share_all, share_x=True, share_y=True, aspect=aspect,
                label_mode=label_mode, axes_class=axes_class)
        else:  # Only show deprecation in that case.
            super().__init__(
                fig, rect, nrows_ncols, ngrids,
                direction=direction, axes_pad=axes_pad, add_all=add_all,
                share_all=share_all, share_x=True, share_y=True, aspect=aspect,
                label_mode=label_mode, axes_class=axes_class)

        if add_all:
            for ax in self.cbar_axes:
                fig.add_axes(ax)

        if cbar_set_cax:
            if self._colorbar_mode == "single":
                for ax in self.axes_all:
                    ax.cax = self.cbar_axes[0]
            elif self._colorbar_mode == "edge":
                for index, ax in enumerate(self.axes_all):
                    col, row = self._get_col_row(index)
                    if self._colorbar_location in ("left", "right"):
                        ax.cax = self.cbar_axes[row]
                    else:
                        ax.cax = self.cbar_axes[col]
            else:
                for ax, cax in zip(self.axes_all, self.cbar_axes):
                    ax.cax = cax

    def _init_locators(self):
        # Slightly abusing this method to inject colorbar creation into init.

        if self._colorbar_pad is None:
            # horizontal or vertical arrangement?
            if self._colorbar_location in ("left", "right"):
                self._colorbar_pad = self._horiz_pad_size.fixed_size
            else:
                self._colorbar_pad = self._vert_pad_size.fixed_size
        self.cbar_axes = [
            self._defaultCbarAxesClass(
                self.axes_all[0].figure, self._divider.get_position(),
                orientation=self._colorbar_location)
            for _ in range(self.ngrids)]

        cb_mode = self._colorbar_mode
        cb_location = self._colorbar_location

        h = []
        v = []

        h_ax_pos = []
        h_cb_pos = []
        if cb_mode == "single" and cb_location in ("left", "bottom"):
            if cb_location == "left":
                sz = self._nrows * Size.AxesX(self.axes_llc)
                h.append(Size.from_any(self._colorbar_size, sz))
                h.append(Size.from_any(self._colorbar_pad, sz))
                locator = self._divider.new_locator(nx=0, ny=0, ny1=-1)
            elif cb_location == "bottom":
                sz = self._ncols * Size.AxesY(self.axes_llc)
                v.append(Size.from_any(self._colorbar_size, sz))
                v.append(Size.from_any(self._colorbar_pad, sz))
                locator = self._divider.new_locator(nx=0, nx1=-1, ny=0)
            for i in range(self.ngrids):
                self.cbar_axes[i].set_visible(False)
            self.cbar_axes[0].set_axes_locator(locator)
            self.cbar_axes[0].set_visible(True)

        for col, ax in enumerate(self.axes_row[0]):
            if h:
                h.append(self._horiz_pad_size)

            if ax:
                sz = Size.AxesX(ax, aspect="axes", ref_ax=self.axes_all[0])
            else:
                sz = Size.AxesX(self.axes_all[0],
                                aspect="axes", ref_ax=self.axes_all[0])

            if (cb_location == "left"
                    and (cb_mode == "each"
                         or (cb_mode == "edge" and col == 0))):
                h_cb_pos.append(len(h))
                h.append(Size.from_any(self._colorbar_size, sz))
                h.append(Size.from_any(self._colorbar_pad, sz))

            h_ax_pos.append(len(h))
            h.append(sz)

            if (cb_location == "right"
                    and (cb_mode == "each"
                         or (cb_mode == "edge" and col == self._ncols - 1))):
                h.append(Size.from_any(self._colorbar_pad, sz))
                h_cb_pos.append(len(h))
                h.append(Size.from_any(self._colorbar_size, sz))

        v_ax_pos = []
        v_cb_pos = []
        for row, ax in enumerate(self.axes_column[0][::-1]):
            if v:
                v.append(self._vert_pad_size)

            if ax:
                sz = Size.AxesY(ax, aspect="axes", ref_ax=self.axes_all[0])
            else:
                sz = Size.AxesY(self.axes_all[0],
                                aspect="axes", ref_ax=self.axes_all[0])

            if (cb_location == "bottom"
                    and (cb_mode == "each"
                         or (cb_mode == "edge" and row == 0))):
                v_cb_pos.append(len(v))
                v.append(Size.from_any(self._colorbar_size, sz))
                v.append(Size.from_any(self._colorbar_pad, sz))

            v_ax_pos.append(len(v))
            v.append(sz)

            if (cb_location == "top"
                    and (cb_mode == "each"
                         or (cb_mode == "edge" and row == self._nrows - 1))):
                v.append(Size.from_any(self._colorbar_pad, sz))
                v_cb_pos.append(len(v))
                v.append(Size.from_any(self._colorbar_size, sz))

        for i in range(self.ngrids):
            col, row = self._get_col_row(i)
            locator = self._divider.new_locator(nx=h_ax_pos[col],
                                                ny=v_ax_pos[self._nrows-1-row])
            self.axes_all[i].set_axes_locator(locator)

            if cb_mode == "each":
                if cb_location in ("right", "left"):
                    locator = self._divider.new_locator(
                        nx=h_cb_pos[col], ny=v_ax_pos[self._nrows - 1 - row])

                elif cb_location in ("top", "bottom"):
                    locator = self._divider.new_locator(
                        nx=h_ax_pos[col], ny=v_cb_pos[self._nrows - 1 - row])

                self.cbar_axes[i].set_axes_locator(locator)
            elif cb_mode == "edge":
                if (cb_location == "left" and col == 0
                        or cb_location == "right" and col == self._ncols - 1):
                    locator = self._divider.new_locator(
                        nx=h_cb_pos[0], ny=v_ax_pos[self._nrows - 1 - row])
                    self.cbar_axes[row].set_axes_locator(locator)
                elif (cb_location == "bottom" and row == self._nrows - 1
                      or cb_location == "top" and row == 0):
                    locator = self._divider.new_locator(nx=h_ax_pos[col],
                                                        ny=v_cb_pos[0])
                    self.cbar_axes[col].set_axes_locator(locator)

        if cb_mode == "single":
            if cb_location == "right":
                sz = self._nrows * Size.AxesX(self.axes_llc)
                h.append(Size.from_any(self._colorbar_pad, sz))
                h.append(Size.from_any(self._colorbar_size, sz))
                locator = self._divider.new_locator(nx=-2, ny=0, ny1=-1)
            elif cb_location == "top":
                sz = self._ncols * Size.AxesY(self.axes_llc)
                v.append(Size.from_any(self._colorbar_pad, sz))
                v.append(Size.from_any(self._colorbar_size, sz))
                locator = self._divider.new_locator(nx=0, nx1=-1, ny=-2)
            if cb_location in ("right", "top"):
                for i in range(self.ngrids):
                    self.cbar_axes[i].set_visible(False)
                self.cbar_axes[0].set_axes_locator(locator)
                self.cbar_axes[0].set_visible(True)
        elif cb_mode == "each":
            for i in range(self.ngrids):
                self.cbar_axes[i].set_visible(True)
        elif cb_mode == "edge":
            if cb_location in ("right", "left"):
                count = self._nrows
            else:
                count = self._ncols
            for i in range(count):
                self.cbar_axes[i].set_visible(True)
            for j in range(i + 1, self.ngrids):
                self.cbar_axes[j].set_visible(False)
        else:
            for i in range(self.ngrids):
                self.cbar_axes[i].set_visible(False)
                self.cbar_axes[i].set_position([1., 1., 0.001, 0.001],
                                               which="active")

        self._divider.set_horizontal(h)
        self._divider.set_vertical(v)

        
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.51378129, 0.44999619, 0.42258797],
                         std=[0.25081163, 0.24213039, 0.24616128])
])

train_dataset = CIFAR10(root='./data', train=True, download=True, transform=transform)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

model = nn.Sequential(
    nn.Flatten(start_dim=1),
    nn.Linear(3072, 3)
)

def plot_errors(model, dataloader): 
    # find mismatches
    mismatches = []
    for data in dataloader:
        if len(mismatches) > 8:
            break
        features, labels = data
        outputs = model(features)
        gt = labels.argmax(-1)
        pred = outputs.argmax(-1)
        for f, g, p in zip(features, gt, pred):
            if g != p:
                mismatches.append((f, g, p))
    
    
    fig = plt.figure(figsize=(8, 8))
    grid = ImageGrid(fig, 111,  # similar to subplot(111)
                     nrows_ncols=(2, 4),  # creates 2x2 grid of axes
                     axes_pad=0.5,  # pad between axes in inch.
                     )
    mapping = {0: 'No mask', 1: 'Mask', 2: 'Incorrect'}
    for idx, ax in enumerate(grid):
        ax.imshow(mismatches[idx][0].permute(1, 2, 0))
        ax.set_title(f'GT: {mapping[mismatches[idx][1].item()]} \n PRED: {mapping[mismatches[idx][2].item()]}')
        ax.axis('off')
    plt.show()

# Create accuracy metric
metric = torchmetrics.Accuracy(task="multiclass", num_classes=3)
for features, labels in dataloader:
    outputs = model(features)
    
    # Calculate accuracy over the batch
    metric.update(outputs, labels.argmax(dim=-1))
    
# Calculate accuracy over the whole epoch
accuracy = metric.compute()
print(f"Accuracy on all data: {accuracy}")

# Reset metric for the next epoch
metric.reset()
plot_errors(model, dataloader)

print("Accuracy is key for classification. Analyzing misclassifications helps spot patterns and improve your model.")