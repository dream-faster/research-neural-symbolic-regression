from binary_encoder import dec2bin, float2bin
import pytest
import numpy as np
from torch import tensor

def test_dec2bin():
    assert np.all(dec2bin(tensor([1]), 10).numpy() == tensor([[0., 0., 0., 0., 0., 0., 0., 0., 0., 1.]]).numpy())
    assert np.all(dec2bin(tensor([-1]), 10).numpy() == tensor([[1., 0., 0., 0., 0., 0., 0., 0., 0., 1.]]).numpy())
    assert np.all(dec2bin(tensor([2]), 10).numpy() == tensor([[0., 0., 0., 0., 0., 0., 0., 0., 1., 0.]]).numpy())
    assert np.all(dec2bin(tensor([-2]), 10).numpy() == tensor([[1., 0., 0., 0., 0., 0., 0., 0., 1., 0.]]).numpy())
    assert np.all(dec2bin(tensor([200]), 10).numpy() == tensor([[0., 0., 1., 1., 0., 0., 1., 0., 0., 0.]]).numpy())
    assert np.all(dec2bin(tensor([999]), 10).numpy() == tensor([[0., 1., 1., 1., 1., 0., 0., 1., 1., 1.]]).numpy())
    assert np.all(dec2bin(tensor([9999]), 12).numpy() == tensor([[0., 1., 1., 1., 0., 0., 0., 0., 1., 1., 1., 1.]]).numpy())


def test_float2bin():
    assert np.all(float2bin(tensor([0.01]), 3, 3, 2).numpy() == tensor([[0., 0., 0., 0., 0., 0., 1.]]).numpy())
    assert np.all(float2bin(tensor([0.01]), 7, 7, 2).numpy() == tensor([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.]]).numpy())
    assert np.all(float2bin(tensor([1.01]), 7, 7, 2).numpy() == tensor([[0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 1.]]).numpy())

