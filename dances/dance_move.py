import sys
import time
from naoqi import ALProxy


def main(robotIP, port):
	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 2.86667, 3.13333, 3.4, 3.66667, 5.46667, 6])
	keys.append([[0.00302603, [3, -0.111111, 0], [3, 0.222222, 0]], [0.00302603, [3, -0.222222, 0], [3, 0.2, 0]], [0.340507, [3, -0.2, 0], [3, 0.2, 0]], [-0.417291, [3, -0.2, 0.200954], [3, 0.133333, -0.133969]], [-0.664264, [3, -0.133333, 0], [3, 0.0888889, 0]], [0.0459781, [3, -0.0888889, -0.0674959], [3, 0.0888889, 0.0674959]], [0.113474, [3, -0.0888889, 0], [3, 0.0888889, 0]], [0.0996681, [3, -0.0888889, 0], [3, 0.0888889, 0]], [0.102736, [3, -0.0888889, 0], [3, 0.6, 0]], [-0.00617796, [3, -0.6, 0], [3, 0.177778, 0]], [-0.0046272, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("HeadYaw")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 2.86667, 3.13333, 3.4, 3.66667, 5.46667, 6])
	keys.append([[-1.10145, [3, -0.111111, 0], [3, 0.222222, 0]], [1.4097, [3, -0.222222, 0], [3, 0.2, 0]], [-0.00924597, [3, -0.2, 0.245439], [3, 0.2, -0.245439]], [-0.254685, [3, -0.2, 0], [3, 0.133333, 0]], [0.506179, [3, -0.133333, -0.17641], [3, 0.0888889, 0.117607]], [0.627364, [3, -0.0888889, 0], [3, 0.0888889, 0]], [-0.22554, [3, -0.0888889, 0], [3, 0.0888889, 0]], [0.645772, [3, -0.0888889, 0], [3, 0.0888889, 0]], [-0.217869, [3, -0.0888889, 0], [3, 0.6, 0]], [0.00456004, [3, -0.6, 0], [3, 0.177778, 0]], [-0.00930693, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("LAnklePitch")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 3.13333, 5.46667, 6])
	keys.append([[-0.359129, [3, -0.111111, 0], [3, 0.222222, 0]], [-0.762571, [3, -0.222222, 0.0170441], [3, 0.2, -0.0153397]], [-0.777911, [3, -0.2, 0], [3, 0.2, 0]], [-0.580025, [3, -0.2, 0], [3, 0.133333, 0]], [-0.58923, [3, -0.133333, 0.00115064], [3, 0.177778, -0.00153418]], [-0.590764, [3, -0.177778, 0], [3, 0.777778, 0]], [-0.116757, [3, -0.777778, 0], [3, 0.177778, 0]], [-0.350546, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("LAnkleRoll")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 3.13333, 5.46667, 6])
	keys.append([[-0.282235, [3, -0.111111, 0], [3, 0.222222, 0]], [-0.0598056, [3, -0.222222, -0.00511343], [3, 0.2, 0.00460208]], [-0.0552035, [3, -0.2, 0], [3, 0.2, 0]], [-0.139574, [3, -0.2, 0], [3, 0.133333, 0]], [-0.133438, [3, -0.133333, 0], [3, 0.177778, 0]], [-0.134972, [3, -0.177778, 0], [3, 0.777778, 0]], [0.0138264, [3, -0.777778, 0], [3, 0.177778, 0]], [-0.00709866, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("LElbowRoll")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 2.86667, 3.13333, 3.4, 3.66667, 4.4, 4.8, 5.46667, 6])
	keys.append([[-0.748551, [3, -0.111111, 0], [3, 0.222222, 0]], [-0.901949, [3, -0.222222, 0.129986], [3, 0.2, -0.116988]], [-1.48947, [3, -0.2, 0], [3, 0.2, 0]], [-1.05688, [3, -0.2, 0], [3, 0.133333, 0]], [-1.56157, [3, -0.133333, 0], [3, 0.0888889, 0]], [-1.08603, [3, -0.0888889, 0], [3, 0.0888889, 0]], [-1.56464, [3, -0.0888889, 0], [3, 0.0888889, 0]], [-0.866668, [3, -0.0888889, 0], [3, 0.0888889, 0]], [-1.56464, [3, -0.0888889, 0], [3, 0.244444, 0]], [-1.02314, [3, -0.244444, -0.272962], [3, 0.133333, 0.148888]], [-0.299088, [3, -0.133333, 0], [3, 0.222222, 0]], [-0.315962, [3, -0.222222, 0.0168739], [3, 0.177778, -0.0134991]], [-1.007, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("LElbowYaw")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 2.86667, 3.13333, 3.4, 3.66667, 4.4, 4.8, 5.46667, 6])
	keys.append([[0.89428, [3, -0.111111, 0], [3, 0.222222, 0]], [-0.681137, [3, -0.222222, 0], [3, 0.2, 0]], [-0.52467, [3, -0.2, -0.156467], [3, 0.2, 0.156467]], [0.383458, [3, -0.2, 0], [3, 0.133333, 0]], [-0.760906, [3, -0.133333, 0], [3, 0.0888889, 0]], [0.0797261, [3, -0.0888889, 0], [3, 0.0888889, 0]], [-0.83914, [3, -0.0888889, 0], [3, 0.0888889, 0]], [0.329768, [3, -0.0888889, 0], [3, 0.0888889, 0]], [-0.740964, [3, -0.0888889, 0], [3, 0.244444, 0]], [-0.339056, [3, -0.244444, 0], [3, 0.133333, 0]], [-0.932714, [3, -0.133333, 0], [3, 0.222222, 0]], [-0.7471, [3, -0.222222, 0], [3, 0.177778, 0]], [-1.38708, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("LHand")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 3.13333, 5.46667, 6])
	keys.append([[0.920023, [3, -0.111111, 0], [3, 0.222222, 0]], [0.920023, [3, -0.222222, 0], [3, 0.2, 0]], [0.921478, [3, -0.2, 0], [3, 0.2, 0]], [0.921478, [3, -0.2, 0], [3, 0.133333, 0]], [0.921478, [3, -0.133333, 0], [3, 0.177778, 0]], [0.921478, [3, -0.177778, 0], [3, 0.777778, 0]], [0.920387, [3, -0.777778, 0.00109094], [3, 0.177778, -0.000249359]], [0.255661, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("LHipPitch")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 3.13333, 5.46667, 6])
	keys.append([[0.232947, [3, -0.111111, 0], [3, 0.222222, 0]], [-0.224186, [3, -0.222222, 0], [3, 0.2, 0]], [-0.21038, [3, -0.2, 0], [3, 0.2, 0]], [-0.34077, [3, -0.2, 0], [3, 0.133333, 0]], [-0.325429, [3, -0.133333, -0.00115061], [3, 0.177778, 0.00153415]], [-0.323895, [3, -0.177778, -0.00153415], [3, 0.777778, 0.00671189]], [0.0764786, [3, -0.777778, 0], [3, 0.177778, 0]], [-0.44423, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("LHipRoll")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 3.13333, 5.46667, 6])
	keys.append([[0.423192, [3, -0.111111, 0], [3, 0.222222, 0]], [0.31121, [3, -0.222222, 0.0187487], [3, 0.2, -0.0168738]], [0.294336, [3, -0.2, 0.0168738], [3, 0.2, -0.0168738]], [-0.050814, [3, -0.2, 0.0230101], [3, 0.133333, -0.01534]], [-0.0661541, [3, -0.133333, 0], [3, 0.177778, 0]], [-0.0661541, [3, -0.177778, 0], [3, 0.777778, 0]], [-0.0492801, [3, -0.777778, -0.016874], [3, 0.177778, 0.00385692]], [0, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("LHipYawPitch")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 3.13333, 3.66667, 5.46667, 6])
	keys.append([[-0.113559, [3, -0.111111, 0], [3, 0.222222, 0]], [-0.236279, [3, -0.222222, 0], [3, 0.2, 0]], [-0.230144, [3, -0.2, 0], [3, 0.2, 0]], [-0.32065, [3, -0.2, 0], [3, 0.133333, 0]], [-0.311445, [3, -0.133333, 0], [3, 0.177778, 0]], [-0.311445, [3, -0.177778, 0], [3, 0.177778, 0]], [-0.302242, [3, -0.177778, -0.00920312], [3, 0.6, 0.0310605]], [0.0275685, [3, -0.6, 0], [3, 0.177778, 0]], [-0.0028562, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("LKneePitch")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 3.13333, 5.46667, 6])
	keys.append([[0.14541, [3, -0.111111, 0], [3, 0.222222, 0]], [1.11643, [3, -0.222222, -0.0187487], [3, 0.2, 0.0168739]], [1.13331, [3, -0.2, 0], [3, 0.2, 0]], [1.01212, [3, -0.2, 0], [3, 0.133333, 0]], [1.03513, [3, -0.133333, 0], [3, 0.177778, 0]], [1.02899, [3, -0.177778, 0.00613659], [3, 0.777778, -0.0268476]], [0.0871181, [3, -0.777778, 0], [3, 0.177778, 0]], [0.699999, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("LShoulderPitch")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 2.86667, 3.13333, 3.4, 3.66667, 4.4, 4.8, 5.46667, 6])
	keys.append([[0.653443, [3, -0.111111, 0], [3, 0.222222, 0]], [-0.934249, [3, -0.222222, 0], [3, 0.2, 0]], [0.489305, [3, -0.2, -0.0997089], [3, 0.2, 0.0997089]], [0.589014, [3, -0.2, 0], [3, 0.133333, 0]], [0.259204, [3, -0.133333, 0], [3, 0.0888889, 0]], [0.714801, [3, -0.0888889, 0], [3, 0.0888889, 0]], [0.245399, [3, -0.0888889, 0], [3, 0.0888889, 0]], [0.656511, [3, -0.0888889, 0], [3, 0.0888889, 0]], [0.274544, [3, -0.0888889, 0], [3, 0.244444, 0]], [0.720938, [3, -0.244444, 0], [3, 0.133333, 0]], [0.437147, [3, -0.133333, 0], [3, 0.222222, 0]], [1.56004, [3, -0.222222, 0], [3, 0.177778, 0]], [1.39144, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("LShoulderRoll")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 2.86667, 3.13333, 3.4, 3.66667, 4.4, 4.8, 5.46667, 6])
	keys.append([[1.32687, [3, -0.111111, 0], [3, 0.222222, 0]], [1.39743, [3, -0.222222, 0], [3, 0.2, 0]], [0.010696, [3, -0.2, 0], [3, 0.2, 0]], [0.013764, [3, -0.2, 0], [3, 0.133333, 0]], [0, [3, -0.133333, 0], [3, 0.0888889, 0]], [0, [3, -0.0888889, 0], [3, 0.0888889, 0]], [0.013764, [3, -0.0888889, 0], [3, 0.0888889, 0]], [0, [3, -0.0888889, 0], [3, 0.0888889, 0]], [0, [3, -0.0888889, 0], [3, 0.244444, 0]], [0.061318, [3, -0.244444, -0.0613179], [3, 0.133333, 0.0334462]], [1.13052, [3, -0.133333, 0], [3, 0.222222, 0]], [0.302157, [3, -0.222222, 0.00105811], [3, 0.177778, -0.000846486]], [0.30131, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("LWristYaw")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 3.13333, 5.46667, 6])
	keys.append([[-1.02475, [3, -0.111111, 0], [3, 0.222222, 0]], [-1.02475, [3, -0.222222, 0], [3, 0.2, 0]], [-1.02015, [3, -0.2, 0], [3, 0.2, 0]], [-1.02629, [3, -0.2, 0], [3, 0.133333, 0]], [-1.02015, [3, -0.133333, 0], [3, 0.177778, 0]], [-1.02629, [3, -0.177778, 0], [3, 0.777778, 0]], [1.04461, [3, -0.777778, 0], [3, 0.177778, 0]], [-0.00130817, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("RAnklePitch")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 3.13333, 3.66667, 5.46667, 6])
	keys.append([[-0.102805, [3, -0.111111, 0], [3, 0.222222, 0]], [-0.210185, [3, -0.222222, 0.0119322], [3, 0.2, -0.010739]], [-0.220924, [3, -0.2, 0.010739], [3, 0.2, -0.010739]], [-0.405004, [3, -0.2, 0.0115035], [3, 0.133333, -0.00766897]], [-0.412673, [3, -0.133333, 0], [3, 0.177778, 0]], [-0.412673, [3, -0.177778, 0], [3, 0.177778, 0]], [-0.421878, [3, -0.177778, 0], [3, 0.6, 0]], [-0.102805, [3, -0.6, 0], [3, 0.177778, 0]], [-0.34791, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("RAnkleRoll")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 3.13333, 3.66667, 5.46667, 6])
	keys.append([[-0.00456227, [3, -0.111111, 0], [3, 0.222222, 0]], [-0.105806, [3, -0.222222, 0.0017044], [3, 0.2, -0.00153396]], [-0.10734, [3, -0.2, 0], [3, 0.2, 0]], [-0.0229703, [3, -0.2, 0], [3, 0.133333, 0]], [-0.0245042, [3, -0.133333, 0.000438277], [3, 0.177778, -0.00058437]], [-0.0260382, [3, -0.177778, 0.000511323], [3, 0.177778, -0.000511323]], [-0.0275722, [3, -0.177778, 0], [3, 0.6, 0]], [-0.00456227, [3, -0.6, -0.00754438], [3, 0.177778, 0.00223537]], [0.00176708, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("RElbowRoll")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 2.86667, 3.13333, 3.4, 3.66667, 4.4, 4.8, 5.46667, 6])
	keys.append([[0.727158, [3, -0.111111, 0], [3, 0.222222, 0]], [1.10452, [3, -0.222222, 0], [3, 0.2, 0]], [0.176453, [3, -0.2, 0.00613674], [3, 0.2, -0.00613674]], [0.170316, [3, -0.2, 0], [3, 0.133333, 0]], [0.174919, [3, -0.133333, 0], [3, 0.0888889, 0]], [0.174919, [3, -0.0888889, 0], [3, 0.0888889, 0]], [0.173384, [3, -0.0888889, 0.000767101], [3, 0.0888889, -0.000767101]], [0.170316, [3, -0.0888889, 0], [3, 0.0888889, 0]], [0.173384, [3, -0.0888889, -0.00306793], [3, 0.244444, 0.0084368]], [0.280764, [3, -0.244444, -0.10738], [3, 0.133333, 0.058571]], [1.34843, [3, -0.133333, 0], [3, 0.222222, 0]], [0.273093, [3, -0.222222, 0], [3, 0.177778, 0]], [1.00676, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("RElbowYaw")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 2.86667, 3.13333, 3.4, 3.66667, 4.4, 4.8, 5.46667, 6])
	keys.append([[0.946436, [3, -0.111111, 0], [3, 0.222222, 0]], [-0.515466, [3, -0.222222, 0], [3, 0.2, 0]], [0.728609, [3, -0.2, 0], [3, 0.2, 0]], [0.722472, [3, -0.2, 0], [3, 0.133333, 0]], [0.730143, [3, -0.133333, -0.00184063], [3, 0.0888889, 0.00122709]], [0.731675, [3, -0.0888889, 0], [3, 0.0888889, 0]], [0.730143, [3, -0.0888889, 0.00153245], [3, 0.0888889, -0.00153245]], [0.71787, [3, -0.0888889, 0], [3, 0.0888889, 0]], [0.722472, [3, -0.0888889, 0], [3, 0.244444, 0]], [-1.22878, [3, -0.244444, 0], [3, 0.133333, 0]], [-0.0537319, [3, -0.133333, -0.249658], [3, 0.222222, 0.416097]], [0.768491, [3, -0.222222, -0.266814], [3, 0.177778, 0.213451]], [1.38706, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("RHand")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 3.13333, 5.46667, 6])
	keys.append([[0.920387, [3, -0.111111, 0], [3, 0.222222, 0]], [0.920387, [3, -0.222222, 0], [3, 0.2, 0]], [0.922933, [3, -0.2, 0], [3, 0.2, 0]], [0.922933, [3, -0.2, 0], [3, 0.133333, 0]], [0.925478, [3, -0.133333, 0], [3, 0.177778, 0]], [0.922933, [3, -0.177778, 0], [3, 0.777778, 0]], [0.971296, [3, -0.777778, 0], [3, 0.177778, 0]], [0.255665, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("RHipPitch")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 3.13333, 3.66667, 5.46667, 6])
	keys.append([[0.041361, [3, -0.111111, 0], [3, 0.222222, 0]], [-0.24243, [3, -0.222222, 0], [3, 0.2, 0]], [-0.237827, [3, -0.2, 0], [3, 0.2, 0]], [-0.856028, [3, -0.2, 0], [3, 0.133333, 0]], [-0.848359, [3, -0.133333, 0], [3, 0.177778, 0]], [-0.852962, [3, -0.177778, 0], [3, 0.177778, 0]], [-0.851427, [3, -0.177778, -0.00153418], [3, 0.6, 0.00517786]], [0.041361, [3, -0.6, 0], [3, 0.177778, 0]], [-0.45, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("RHipRoll")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 3.13333, 3.66667, 5.46667, 6])
	keys.append([[0.0153604, [3, -0.111111, 0], [3, 0.222222, 0]], [0.210178, [3, -0.222222, -0.00511381], [3, 0.2, 0.00460242]], [0.21478, [3, -0.2, 0], [3, 0.2, 0]], [-0.0889516, [3, -0.2, 0], [3, 0.133333, 0]], [-0.0843497, [3, -0.133333, 0], [3, 0.177778, 0]], [-0.0843497, [3, -0.177778, 0], [3, 0.177778, 0]], [-0.0797476, [3, -0.177778, -0.00460208], [3, 0.6, 0.015532]], [0.0153604, [3, -0.6, 0], [3, 0.177778, 0]], [0.00205951, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("RKneePitch")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 3.13333, 3.66667, 5.46667, 6])
	keys.append([[0.105432, [3, -0.111111, 0], [3, 0.222222, 0]], [0.619321, [3, -0.222222, -0.0238625], [3, 0.2, 0.0214763]], [0.640798, [3, -0.2, -0.0214763], [3, 0.2, 0.0214763]], [1.26974, [3, -0.2, -0.0322144], [3, 0.133333, 0.0214763]], [1.29121, [3, -0.133333, 0], [3, 0.177778, 0]], [1.28968, [3, -0.177778, 0], [3, 0.177778, 0]], [1.31576, [3, -0.177778, 0], [3, 0.6, 0]], [0.105432, [3, -0.6, 0], [3, 0.177778, 0]], [0.699999, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("RShoulderPitch")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 2.86667, 3.13333, 3.4, 3.66667, 4.4, 4.8, 5.46667, 6])
	keys.append([[-0.970981, [3, -0.111111, 0], [3, 0.222222, 0]], [0.782382, [3, -0.222222, 0], [3, 0.2, 0]], [-0.877407, [3, -0.2, 0], [3, 0.2, 0]], [-0.863599, [3, -0.2, -0.0119653], [3, 0.133333, 0.00797686]], [-0.81758, [3, -0.133333, -0.00460244], [3, 0.0888889, 0.00306829]], [-0.814512, [3, -0.0888889, 0], [3, 0.0888889, 0]], [-0.819114, [3, -0.0888889, 0], [3, 0.0888889, 0]], [-0.811444, [3, -0.0888889, 0], [3, 0.0888889, 0]], [-0.81758, [3, -0.0888889, 0], [3, 0.244444, 0]], [-0.085862, [3, -0.244444, -0.264028], [3, 0.133333, 0.144016]], [0.406552, [3, -0.133333, -0.205364], [3, 0.222222, 0.342274]], [1.55705, [3, -0.222222, 0], [3, 0.177778, 0]], [1.39697, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("RShoulderRoll")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 2.86667, 3.13333, 3.4, 3.66667, 4.4, 4.8, 5.46667, 6])
	keys.append([[-1.40519, [3, -0.111111, 0], [3, 0.222222, 0]], [-1.30701, [3, -0.222222, -0.0707792], [3, 0.2, 0.0637013]], [-1.00174, [3, -0.2, 0], [3, 0.2, 0]], [-1.01248, [3, -0.2, 0.00490891], [3, 0.133333, -0.00327261]], [-1.02629, [3, -0.133333, 0], [3, 0.0888889, 0]], [-1.02015, [3, -0.0888889, 0], [3, 0.0888889, 0]], [-1.03856, [3, -0.0888889, 0.00511322], [3, 0.0888889, -0.00511322]], [-1.05083, [3, -0.0888889, 0.00357938], [3, 0.0888889, -0.00357938]], [-1.06004, [3, -0.0888889, 0.00920488], [3, 0.244444, -0.0253134]], [-1.25179, [3, -0.244444, 0], [3, 0.133333, 0]], [-0.00617796, [3, -0.133333, 0], [3, 0.222222, 0]], [-0.296104, [3, -0.222222, 0.00650789], [3, 0.177778, -0.00520631]], [-0.30131, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("RWristYaw")
	times.append([0.333333, 1, 1.6, 2.2, 2.6, 3.13333, 5.46667, 6])
	keys.append([[0.977116, [3, -0.111111, 0], [3, 0.222222, 0]], [0.974047, [3, -0.222222, 0.00215287], [3, 0.2, -0.00193759]], [0.964844, [3, -0.2, 0], [3, 0.2, 0]], [0.966378, [3, -0.2, -0.00153411], [3, 0.133333, 0.00102274]], [0.98632, [3, -0.133333, 0], [3, 0.177778, 0]], [0.966378, [3, -0.177778, 0], [3, 0.777778, 0]], [1.49254, [3, -0.777778, 0], [3, 0.177778, 0]], [0.000547559, [3, -0.177778, 0], [3, 0, 0]]])

	try:
	  motion = ALProxy("ALMotion",robotIP,port)
	  motion.angleInterpolationBezier(names, times, keys)
	except BaseException, err:
	  print err
  
if __name__ == "__main__":

    robotIP = "127.0.0.1"#"192.168.11.3"

    port = 55650 #9559 # Insert NAO port


    if len(sys.argv) <= 1:
        print "(robotIP default: 127.0.0.1)"
    elif len(sys.argv) <= 2:
        robotIP = sys.argv[1]
    else:
        port = int(sys.argv[2])
        robotIP = sys.argv[1]

    main(robotIP, port)