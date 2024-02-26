
expected_version = {
    "Python":       "3.10.13",
    "Numpy":        "1.23.5",
    
    "Torch":        "2.1.0+cu121",
    "TorchVision":  "0.16.1+cu121",
    "TorchAudio":   "2.1.0+cu121",
    
    "gradio":       "3.50.2",
    "numba":        "0.58.1",
    "pyworld":      "0.3.4",
    "scipy":        "1.10.0",
    "tqdm":         "4.66.1",
    "parselmouth":  "0.4.3",
    "fairseq":      "0.12.2",
    "librosa":      "0.9.1",
}

import sys
print("Python", sys.version, "✓" if sys.version.split(" ")[0] == expected_version["Python"] else "✗")
import numpy as np
print("Numpy", np.__version__, "✓" if np.__version__ == expected_version["Numpy"] else "✗")

import torch
print("Torch", torch.__version__, "✓" if torch.__version__ == expected_version["Torch"] else "✗")
import torchvision
print("TorchVision", torchvision.__version__, "✓" if torchvision.__version__ == expected_version["TorchVision"] else "✗")
import torchaudio
print("TorchAudio", torchaudio.__version__, "✓" if torchaudio.__version__ == expected_version["TorchAudio"] else "✗")

import gradio
print("gradio", gradio.__version__, "✓" if gradio.__version__ == expected_version["gradio"] else "✗")
import numba
print("numba", numba.__version__, "✓" if numba.__version__ == expected_version["numba"] else "✗")
import pyworld
print("pyworld", pyworld.__version__, "✓" if pyworld.__version__ == expected_version["pyworld"] else "✗")
import scipy
print("scipy", scipy.__version__, "✓" if scipy.__version__ == expected_version["scipy"] else "✗")
import tqdm
print("tqdm", tqdm.__version__, "✓" if tqdm.__version__ == expected_version["tqdm"] else "✗")
import parselmouth
print("parselmouth", parselmouth.__version__, "✓" if parselmouth.__version__ == expected_version["parselmouth"] else "✗")
import fairseq
print("fairseq", fairseq.__version__, "✓" if fairseq.__version__ == expected_version["fairseq"] else "✗")
import librosa
print("librosa", librosa.__version__, "✓" if librosa.__version__ == expected_version["librosa"] else "✗")
