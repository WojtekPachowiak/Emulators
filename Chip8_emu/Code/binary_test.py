# f = open(r"C:\Users\48501\Desktop\Programming\Python\Chip8_emu\Roms\15PUZZLE", "rb")

# for i in range(10):
#     b = f.read(1)
#     print(b, "==", int.from_bytes(b, byteorder = "big"))

# import numpy as np

# path = r"C:\Users\48501\Desktop\Programming\Python\Chip8_emu\Roms\15PUZZLE"

# np_f = np.fromfile(path, dtype='uint8')
# print(np_f)

def kur():
    print("kur")

def huiaa():
    print("huiaa")

def czipa(stringg):
    print("czipa:", stringg)

funct_dit = {
    1:kur,
    2:huiaa,
    3:czipa
}

funct_dit[3]("ej")
