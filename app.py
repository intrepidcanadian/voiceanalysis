import streamlit as st;
import torch;
from torch.utils.data import DataLoader;
from torchvision import datasets;
from torchvision.transforms import ToTensor;

print("Hello World!");

st.title("Hello World!");

# download dataset
# create data loader
# build model
# train model
# save trained model

def download_mint_datasets():
    train_data = datasets.MNIST(
        root="data",
        download=True,
        train=True,
        transform=ToTensor()
    )
    validation_data = datasets.MNIST(
        root="data",
        download=True,
        train=False,
        transform=ToTensor()
    )
    return train_data, validation_data

if __name__ == "__main__":
# download MNIST dataset
    train_data, _ = download_mint_datasets()

    print("MNIST dataset downloaded")


