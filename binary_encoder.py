# %%
from torch import tensor, cat, arange, long
import math

def dec2bin(x: tensor, bits: int) -> tensor:
    # calculate the sign bit
    sign = tensor([[0 if x.signbit() == False else 1]])
    if x.signbit() == True:
        x = x.abs()
    # and the binary version of the num
    mask = 2 ** arange(bits - 2, -1, -1).to(x.device, x.dtype)
    encoded = x.unsqueeze(-1).bitwise_and(mask).ne(0).float()
    return cat((sign, encoded), dim = 1)

def dec2bin_sequence(x: tensor, bits: int) -> tensor:
    b = []
    for i in range(x.shape[0]):
        b.append(dec2bin(x[i].unsqueeze(0), bits))
    return cat(b).flatten()



# %%
def float2bin(x: tensor, integral_bits: int, fractional_bits: int, precision: int) -> tensor:
    # calculate the sign bit
    sign = tensor([[0 if x.signbit() == False else 1]])
    if x.signbit() == True:
        x = x.abs()
    
    fractional, integral = math.modf(x.item())
    fractional = round(fractional * (10 ** precision))
    print(fractional)

    # and the binary version of the integral
    integral_mask = 2 ** arange(integral_bits - 1, -1, -1).to(x.device, long)
    integral_encoded = tensor([int(integral)], device=x.device, dtype=long).unsqueeze(-1).bitwise_and(integral_mask).ne(0).float()

    # and the binary version of the fractional
    fractional_mask = 2 ** arange(fractional_bits - 1, -1, -1).to(x.device, long)
    fractional_encoded = tensor([int(fractional)], device=x.device, dtype=long).unsqueeze(-1).bitwise_and(fractional_mask).ne(0).float()

    # then concat the 3
    return cat((sign, integral_encoded, fractional_encoded), dim = 1)
# %%
def float2bin_sequence(x: tensor, integral_bits: int, fractional_bits: int, precision: int) -> tensor:
    b = []
    for i in range(x.shape[0]):
        b.append(float2bin(x[i].unsqueeze(0), integral_bits, fractional_bits, precision))
    return cat(b).flatten()
# %%
