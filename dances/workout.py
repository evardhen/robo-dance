from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[-0.15651, [3, -0.333333, 0], [3, 0.253333, 0]], [-0.136568, [3, -0.253333, 0], [3, 0.28, 0]], [-0.136568, [3, -0.28, 0], [3, 0.266667, 0]], [-0.136568, [3, -0.266667, 0], [3, 0.32, 0]], [-0.136568, [3, -0.32, 0], [3, 0.173333, 0]], [-0.136568, [3, -0.173333, 0], [3, 0.186667, 0]], [-0.136568, [3, -0.186667, 0], [3, 0.2, 0]], [-0.136568, [3, -0.2, 0], [3, 0.2, 0]], [-0.136568, [3, -0.2, 0], [3, 0.186667, 0]], [-0.136568, [3, -0.186667, 0], [3, 0.213333, 0]], [-0.136568, [3, -0.213333, 0], [3, 0.186667, 0]], [-0.136568, [3, -0.186667, 0], [3, 0.2, 0]], [-0.136568, [3, -0.2, 0], [3, 0.186667, 0]], [-0.136568, [3, -0.186667, 0], [3, 0.133333, 0]], [-0.136568, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.136568, [3, -0.146667, 0], [3, 0.146667, 0]], [-0.136568, [3, -0.146667, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[-0.019984, [3, -0.333333, 0], [3, 0.253333, 0]], [-0.00617791, [3, -0.253333, -0.00138789], [3, 0.28, 0.00153399]], [-0.00464392, [3, -0.28, 0], [3, 0.266667, 0]], [-0.00617791, [3, -0.266667, 0], [3, 0.32, 0]], [-0.00464392, [3, -0.32, 0], [3, 0.173333, 0]], [-0.00464392, [3, -0.173333, 0], [3, 0.186667, 0]], [-0.00617791, [3, -0.186667, 0], [3, 0.2, 0]], [-0.00617791, [3, -0.2, 0], [3, 0.2, 0]], [-0.00464392, [3, -0.2, 0], [3, 0.186667, 0]], [-0.00617791, [3, -0.186667, 0], [3, 0.213333, 0]], [-0.00617791, [3, -0.213333, 0], [3, 0.186667, 0]], [-0.00617791, [3, -0.186667, 0], [3, 0.2, 0]], [-0.00617791, [3, -0.2, 0], [3, 0.186667, 0]], [-0.00617791, [3, -0.186667, 0], [3, 0.133333, 0]], [-0.00617791, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.00617791, [3, -0.146667, 0], [3, 0.146667, 0]], [-0.00617791, [3, -0.146667, 0], [3, 0, 0]]])

names.append("LAnklePitch")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[-1.18944, [3, -0.333333, 0], [3, 0.253333, 0]], [-1.18889, [3, -0.253333, -0.00054981], [3, 0.28, 0.000607684]], [0.095066, [3, -0.28, 0], [3, 0.266667, 0]], [0.095066, [3, -0.266667, 0], [3, 0.32, 0]], [0.0966001, [3, -0.32, 0], [3, 0.173333, 0]], [0.095066, [3, -0.173333, 0], [3, 0.186667, 0]], [0.0966001, [3, -0.186667, 0], [3, 0.2, 0]], [0.0966001, [3, -0.2, 0], [3, 0.2, 0]], [0.0966001, [3, -0.2, 0], [3, 0.186667, 0]], [0.0966001, [3, -0.186667, 0], [3, 0.213333, 0]], [0.0966001, [3, -0.213333, 0], [3, 0.186667, 0]], [0.095066, [3, -0.186667, 0], [3, 0.2, 0]], [0.0966001, [3, -0.2, 0], [3, 0.186667, 0]], [0.0966001, [3, -0.186667, 0], [3, 0.133333, 0]], [-1.18889, [3, -0.133333, 0.000499827], [3, 0.146667, -0.00054981]], [-1.18944, [3, -0.146667, 0], [3, 0.146667, 0]], [0.0966001, [3, -0.146667, 0], [3, 0, 0]]])

names.append("LAnkleRoll")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[-0.05058, [3, -0.333333, 0], [3, 0.253333, 0]], [-0.049046, [3, -0.253333, 0], [3, 0.28, 0]], [-0.115008, [3, -0.28, 0], [3, 0.266667, 0]], [-0.115008, [3, -0.266667, 0], [3, 0.32, 0]], [-0.116542, [3, -0.32, 0], [3, 0.173333, 0]], [-0.116542, [3, -0.173333, 0], [3, 0.186667, 0]], [-0.116542, [3, -0.186667, 0], [3, 0.2, 0]], [-0.116542, [3, -0.2, 0], [3, 0.2, 0]], [-0.116542, [3, -0.2, 0], [3, 0.186667, 0]], [-0.115008, [3, -0.186667, 0], [3, 0.213333, 0]], [-0.115008, [3, -0.213333, 0], [3, 0.186667, 0]], [-0.116542, [3, -0.186667, 0], [3, 0.2, 0]], [-0.116542, [3, -0.2, 0], [3, 0.186667, 0]], [-0.115008, [3, -0.186667, -0.00153397], [3, 0.133333, 0.00109569]], [-0.049046, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.05058, [3, -0.146667, 0.00153397], [3, 0.146667, -0.00153397]], [-0.116542, [3, -0.146667, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[-0.397265, [3, -0.333333, 0], [3, 0.253333, 0]], [-0.398797, [3, -0.253333, 0], [3, 0.28, 0]], [-0.384992, [3, -0.28, 0], [3, 0.266667, 0]], [-1.52936, [3, -0.266667, 0], [3, 0.32, 0]], [-0.397265, [3, -0.32, 0], [3, 0.173333, 0]], [-1.52936, [3, -0.173333, 0], [3, 0.186667, 0]], [-0.237728, [3, -0.186667, 0], [3, 0.2, 0]], [-1.39283, [3, -0.2, 0], [3, 0.2, 0]], [-0.37272, [3, -0.2, 0], [3, 0.186667, 0]], [-0.929562, [3, -0.186667, 0], [3, 0.213333, 0]], [-0.174835, [3, -0.213333, 0], [3, 0.186667, 0]], [-1.37442, [3, -0.186667, 0], [3, 0.2, 0]], [-1.36675, [3, -0.2, -0.0076707], [3, 0.186667, 0.00715932]], [-0.44175, [3, -0.186667, 0], [3, 0.133333, 0]], [-0.444818, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.444818, [3, -0.146667, 0], [3, 0.146667, 0]], [-0.418739, [3, -0.146667, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[-1.34996, [3, -0.333333, 0], [3, 0.253333, 0]], [-1.37144, [3, -0.253333, 0.0214763], [3, 0.28, -0.0237369]], [-1.72272, [3, -0.28, 0], [3, 0.266667, 0]], [-1.52177, [3, -0.266667, -0.0392797], [3, 0.32, 0.0471357]], [-1.46348, [3, -0.32, -0.0141581], [3, 0.173333, 0.00766897]], [-1.45581, [3, -0.173333, -0.00590873], [3, 0.186667, 0.00636325]], [-1.42666, [3, -0.186667, 0], [3, 0.2, 0]], [-1.47115, [3, -0.2, 0], [3, 0.2, 0]], [-0.124296, [3, -0.2, 0], [3, 0.186667, 0]], [-0.128898, [3, -0.186667, 0], [3, 0.213333, 0]], [-0.07214, [3, -0.213333, 0], [3, 0.186667, 0]], [-1.61841, [3, -0.186667, 0], [3, 0.2, 0]], [-1.60614, [3, -0.2, 0], [3, 0.186667, 0]], [-1.67517, [3, -0.186667, 0], [3, 0.133333, 0]], [-1.67517, [3, -0.133333, 0], [3, 0.146667, 0]], [-1.67517, [3, -0.146667, 0], [3, 0.146667, 0]], [-1.21037, [3, -0.146667, 0], [3, 0, 0]]])

names.append("LHand")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[0.9576, [3, -0.333333, 0], [3, 0.253333, 0]], [0.0352, [3, -0.253333, 0.0173714], [3, 0.28, -0.0192]], [0.016, [3, -0.28, 0], [3, 0.266667, 0]], [0.0268, [3, -0.266667, 0], [3, 0.32, 0]], [0.0268, [3, -0.32, 0], [3, 0.173333, 0]], [0.0268, [3, -0.173333, 0], [3, 0.186667, 0]], [0.0268, [3, -0.186667, 0], [3, 0.2, 0]], [0.0268, [3, -0.2, 0], [3, 0.2, 0]], [0.0268, [3, -0.2, 0], [3, 0.186667, 0]], [0.0268, [3, -0.186667, 0], [3, 0.213333, 0]], [0.0268, [3, -0.213333, 0], [3, 0.186667, 0]], [0.0268, [3, -0.186667, 0], [3, 0.2, 0]], [0.0316, [3, -0.2, 0], [3, 0.186667, 0]], [0.0316, [3, -0.186667, 0], [3, 0.133333, 0]], [0.0316, [3, -0.133333, 0], [3, 0.146667, 0]], [0.9616, [3, -0.146667, 0], [3, 0.146667, 0]], [0.6208, [3, -0.146667, 0], [3, 0, 0]]])

names.append("LHipPitch")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[-0.559868, [3, -0.333333, 0], [3, 0.253333, 0]], [-0.559868, [3, -0.253333, 0], [3, 0.28, 0]], [0.135034, [3, -0.28, 0], [3, 0.266667, 0]], [0.135034, [3, -0.266667, 0], [3, 0.32, 0]], [0.135034, [3, -0.32, 0], [3, 0.173333, 0]], [0.135034, [3, -0.173333, 0], [3, 0.186667, 0]], [0.135034, [3, -0.186667, 0], [3, 0.2, 0]], [0.135034, [3, -0.2, 0], [3, 0.2, 0]], [0.135034, [3, -0.2, 0], [3, 0.186667, 0]], [0.135034, [3, -0.186667, 0], [3, 0.213333, 0]], [0.135034, [3, -0.213333, 0], [3, 0.186667, 0]], [0.135034, [3, -0.186667, 0], [3, 0.2, 0]], [0.135034, [3, -0.2, 0], [3, 0.186667, 0]], [0.135034, [3, -0.186667, 0], [3, 0.133333, 0]], [-0.619695, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.618161, [3, -0.146667, -0.00153418], [3, 0.146667, 0.00153418]], [0.135034, [3, -0.146667, 0], [3, 0, 0]]])

names.append("LHipRoll")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[0.16418, [3, -0.333333, 0], [3, 0.253333, 0]], [0.16418, [3, -0.253333, 0], [3, 0.28, 0]], [0.115092, [3, -0.28, 0], [3, 0.266667, 0]], [0.115092, [3, -0.266667, 0], [3, 0.32, 0]], [0.115092, [3, -0.32, 0], [3, 0.173333, 0]], [0.115092, [3, -0.173333, 0], [3, 0.186667, 0]], [0.115092, [3, -0.186667, 0], [3, 0.2, 0]], [0.115092, [3, -0.2, 0], [3, 0.2, 0]], [0.115092, [3, -0.2, 0], [3, 0.186667, 0]], [0.115092, [3, -0.186667, 0], [3, 0.213333, 0]], [0.115092, [3, -0.213333, 0], [3, 0.186667, 0]], [0.115092, [3, -0.186667, 0], [3, 0.2, 0]], [0.116626, [3, -0.2, 0], [3, 0.186667, 0]], [0.116626, [3, -0.186667, 0], [3, 0.133333, 0]], [0.124296, [3, -0.133333, 0], [3, 0.146667, 0]], [0.124296, [3, -0.146667, 0], [3, 0.146667, 0]], [0.116626, [3, -0.146667, 0], [3, 0, 0]]])

names.append("LHipYawPitch")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[-0.504645, [3, -0.333333, 0], [3, 0.253333, 0]], [-0.504645, [3, -0.253333, 0], [3, 0.28, 0]], [-0.1733, [3, -0.28, 0], [3, 0.266667, 0]], [-0.1733, [3, -0.266667, 0], [3, 0.32, 0]], [-0.1733, [3, -0.32, 0], [3, 0.173333, 0]], [-0.174835, [3, -0.173333, 0], [3, 0.186667, 0]], [-0.1733, [3, -0.186667, 0], [3, 0.2, 0]], [-0.1733, [3, -0.2, 0], [3, 0.2, 0]], [-0.1733, [3, -0.2, 0], [3, 0.186667, 0]], [-0.1733, [3, -0.186667, 0], [3, 0.213333, 0]], [-0.1733, [3, -0.213333, 0], [3, 0.186667, 0]], [-0.1733, [3, -0.186667, 0], [3, 0.2, 0]], [-0.1733, [3, -0.2, 0], [3, 0.186667, 0]], [-0.1733, [3, -0.186667, 0], [3, 0.133333, 0]], [-0.408002, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.408002, [3, -0.146667, 0], [3, 0.146667, 0]], [-0.1733, [3, -0.146667, 0], [3, 0, 0]]])

names.append("LKneePitch")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[2.11255, [3, -0.333333, 0], [3, 0.253333, 0]], [2.11255, [3, -0.253333, 0], [3, 0.28, 0]], [-0.090548, [3, -0.28, 0], [3, 0.266667, 0]], [-0.090548, [3, -0.266667, 0], [3, 0.32, 0]], [-0.090548, [3, -0.32, 0], [3, 0.173333, 0]], [-0.092082, [3, -0.173333, 0], [3, 0.186667, 0]], [-0.090548, [3, -0.186667, 0], [3, 0.2, 0]], [-0.090548, [3, -0.2, 0], [3, 0.2, 0]], [-0.090548, [3, -0.2, 0], [3, 0.186667, 0]], [-0.090548, [3, -0.186667, 0], [3, 0.213333, 0]], [-0.090548, [3, -0.213333, 0], [3, 0.186667, 0]], [-0.092082, [3, -0.186667, 0], [3, 0.2, 0]], [-0.090548, [3, -0.2, 0], [3, 0.186667, 0]], [-0.090548, [3, -0.186667, 0], [3, 0.133333, 0]], [2.11255, [3, -0.133333, 0], [3, 0.146667, 0]], [2.11255, [3, -0.146667, 0], [3, 0.146667, 0]], [-0.090548, [3, -0.146667, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[1.70116, [3, -0.333333, 0], [3, 0.253333, 0]], [1.86684, [3, -0.253333, 0], [3, 0.28, 0]], [1.71957, [3, -0.28, 0.146404], [3, 0.266667, -0.139432]], [1.00933, [3, -0.266667, 0], [3, 0.32, 0]], [1.49407, [3, -0.32, 0], [3, 0.173333, 0]], [1.09063, [3, -0.173333, 0], [3, 0.186667, 0]], [1.36368, [3, -0.186667, 0], [3, 0.2, 0]], [1.04308, [3, -0.2, 0.320605], [3, 0.2, -0.320605]], [-1.55245, [3, -0.2, 0], [3, 0.186667, 0]], [-1.54631, [3, -0.186667, -0.00262481], [3, 0.213333, 0.00299978]], [-1.53558, [3, -0.213333, -0.0107389], [3, 0.186667, 0.00939657]], [-0.130432, [3, -0.186667, -0.493207], [3, 0.2, 0.528436]], [1.52936, [3, -0.2, -0.295841], [3, 0.186667, 0.276118]], [1.80547, [3, -0.186667, -0.0322293], [3, 0.133333, 0.0230209]], [1.82849, [3, -0.133333, 0], [3, 0.146667, 0]], [1.82696, [3, -0.146667, 0.00153584], [3, 0.146667, -0.00153584]], [1.53856, [3, -0.146667, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[0.395731, [3, -0.333333, 0], [3, 0.253333, 0]], [0.292952, [3, -0.253333, 0.0264743], [3, 0.28, -0.0292611]], [0.228525, [3, -0.28, 0.0515947], [3, 0.266667, -0.0491378]], [-0.00924586, [3, -0.266667, 0], [3, 0.32, 0]], [0.00916195, [3, -0.32, 0], [3, 0.173333, 0]], [-0.00771189, [3, -0.173333, 0], [3, 0.186667, 0]], [0.00762796, [3, -0.186667, 0], [3, 0.2, 0]], [-0.038392, [3, -0.2, 0], [3, 0.2, 0]], [0.34971, [3, -0.2, -0.186196], [3, 0.186667, 0.173783]], [1.04154, [3, -0.186667, 0], [3, 0.213333, 0]], [0.078192, [3, -0.213333, 0], [3, 0.186667, 0]], [0.177901, [3, -0.186667, 0], [3, 0.2, 0]], [0.136484, [3, -0.2, 0], [3, 0.186667, 0]], [0.207048, [3, -0.186667, 0], [3, 0.133333, 0]], [0.196309, [3, -0.133333, 0], [3, 0.146667, 0]], [0.196309, [3, -0.146667, 0], [3, 0.146667, 0]], [0.136484, [3, -0.146667, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[-0.352862, [3, -0.333333, 0], [3, 0.253333, 0]], [-0.40962, [3, -0.253333, 0], [3, 0.28, 0]], [0.0843279, [3, -0.28, 0], [3, 0.266667, 0]], [-1.62915, [3, -0.266667, 0.00767068], [3, 0.32, -0.00920482]], [-1.63835, [3, -0.32, 0], [3, 0.173333, 0]], [-1.61228, [3, -0.173333, 0], [3, 0.186667, 0]], [-1.61688, [3, -0.186667, 0.00460234], [3, 0.2, -0.00493108]], [-1.70278, [3, -0.2, 0], [3, 0.2, 0]], [-0.47865, [3, -0.2, 0], [3, 0.186667, 0]], [-0.47865, [3, -0.186667, 0], [3, 0.213333, 0]], [-0.581429, [3, -0.213333, 0], [3, 0.186667, 0]], [0.021434, [3, -0.186667, 0], [3, 0.2, 0]], [0.0199001, [3, -0.2, 0], [3, 0.186667, 0]], [0.022968, [3, -0.186667, 0], [3, 0.133333, 0]], [0.021434, [3, -0.133333, 0], [3, 0.146667, 0]], [0.022968, [3, -0.146667, -0.00153397], [3, 0.146667, 0.00153397]], [0.076658, [3, -0.146667, 0], [3, 0, 0]]])

names.append("RAnklePitch")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[-1.18421, [3, -0.333333, 0], [3, 0.253333, 0]], [-1.18574, [3, -0.253333, 0], [3, 0.28, 0]], [0.101286, [3, -0.28, 0], [3, 0.266667, 0]], [0.099752, [3, -0.266667, 0], [3, 0.32, 0]], [0.101286, [3, -0.32, 0], [3, 0.173333, 0]], [0.099752, [3, -0.173333, 0], [3, 0.186667, 0]], [0.101286, [3, -0.186667, 0], [3, 0.2, 0]], [0.101286, [3, -0.2, 0], [3, 0.2, 0]], [0.10282, [3, -0.2, 0], [3, 0.186667, 0]], [0.099752, [3, -0.186667, 0], [3, 0.213333, 0]], [0.101286, [3, -0.213333, 0], [3, 0.186667, 0]], [0.0982179, [3, -0.186667, 0], [3, 0.2, 0]], [0.101286, [3, -0.2, 0], [3, 0.186667, 0]], [0.101286, [3, -0.186667, 0], [3, 0.133333, 0]], [-1.1863, [3, -0.133333, 0], [3, 0.146667, 0]], [-1.1863, [3, -0.146667, 0], [3, 0.146667, 0]], [0.101286, [3, -0.146667, 0], [3, 0, 0]]])

names.append("RAnkleRoll")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[0.0429941, [3, -0.333333, 0], [3, 0.253333, 0]], [0.0429941, [3, -0.253333, 0], [3, 0.28, 0]], [0.073674, [3, -0.28, 0], [3, 0.266667, 0]], [0.073674, [3, -0.266667, 0], [3, 0.32, 0]], [0.073674, [3, -0.32, 0], [3, 0.173333, 0]], [0.073674, [3, -0.173333, 0], [3, 0.186667, 0]], [0.073674, [3, -0.186667, 0], [3, 0.2, 0]], [0.073674, [3, -0.2, 0], [3, 0.2, 0]], [0.073674, [3, -0.2, 0], [3, 0.186667, 0]], [0.073674, [3, -0.186667, 0], [3, 0.213333, 0]], [0.073674, [3, -0.213333, 0], [3, 0.186667, 0]], [0.073674, [3, -0.186667, 0], [3, 0.2, 0]], [0.073674, [3, -0.2, 0], [3, 0.186667, 0]], [0.073674, [3, -0.186667, 0], [3, 0.133333, 0]], [0.0521979, [3, -0.133333, 0.00139452], [3, 0.146667, -0.00153397]], [0.0506639, [3, -0.146667, 0], [3, 0.146667, 0]], [0.073674, [3, -0.146667, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[0.346725, [3, -0.333333, 0], [3, 0.253333, 0]], [0.441834, [3, -0.253333, 0], [3, 0.28, 0]], [0.441834, [3, -0.28, 0], [3, 0.266667, 0]], [1.5233, [3, -0.266667, -0.00127843], [3, 0.32, 0.00153411]], [1.52484, [3, -0.32, 0], [3, 0.173333, 0]], [0.159578, [3, -0.173333, 0], [3, 0.186667, 0]], [1.50029, [3, -0.186667, 0], [3, 0.2, 0]], [1.50029, [3, -0.2, 0], [3, 0.2, 0]], [0.309909, [3, -0.2, 0], [3, 0.186667, 0]], [1.07691, [3, -0.186667, 0], [3, 0.213333, 0]], [0.038392, [3, -0.213333, 0], [3, 0.186667, 0]], [1.50029, [3, -0.186667, 0], [3, 0.2, 0]], [1.36684, [3, -0.2, 0.133458], [3, 0.186667, -0.124561]], [0.227074, [3, -0.186667, 0], [3, 0.133333, 0]], [0.230143, [3, -0.133333, -0.000730269], [3, 0.146667, 0.000803296]], [0.231675, [3, -0.146667, -0.0015324], [3, 0.146667, 0.0015324]], [0.389678, [3, -0.146667, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[1.52169, [3, -0.333333, 0], [3, 0.253333, 0]], [1.5447, [3, -0.253333, 0], [3, 0.28, 0]], [1.26704, [3, -0.28, 0], [3, 0.266667, 0]], [1.30539, [3, -0.266667, -0.00127699], [3, 0.32, 0.00153238]], [1.30693, [3, -0.32, -0.00153238], [3, 0.173333, 0.000830041]], [1.61679, [3, -0.173333, 0], [3, 0.186667, 0]], [1.57691, [3, -0.186667, 0], [3, 0.2, 0]], [1.57691, [3, -0.2, 0], [3, 0.2, 0]], [0.754686, [3, -0.2, 0.223223], [3, 0.186667, -0.208342]], [0.282215, [3, -0.186667, 0], [3, 0.213333, 0]], [0.314428, [3, -0.213333, -0.0322135], [3, 0.186667, 0.0281868]], [1.57077, [3, -0.186667, 0], [3, 0.2, 0]], [1.4818, [3, -0.2, 0], [3, 0.186667, 0]], [1.57998, [3, -0.186667, -0.00214776], [3, 0.133333, 0.00153411]], [1.58151, [3, -0.133333, -0.000973787], [3, 0.146667, 0.00107117]], [1.58611, [3, -0.146667, 0], [3, 0.146667, 0]], [1.1796, [3, -0.146667, 0], [3, 0, 0]]])

names.append("RHand")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[0.9432, [3, -0.333333, 0], [3, 0.253333, 0]], [0.0176001, [3, -0.253333, 0.000361995], [3, 0.28, -0.0004001]], [0.0172, [3, -0.28, 0], [3, 0.266667, 0]], [0.1056, [3, -0.266667, 0], [3, 0.32, 0]], [0.1056, [3, -0.32, 0], [3, 0.173333, 0]], [0.1056, [3, -0.173333, 0], [3, 0.186667, 0]], [0.1056, [3, -0.186667, 0], [3, 0.2, 0]], [0.1056, [3, -0.2, 0], [3, 0.2, 0]], [0.1056, [3, -0.2, 0], [3, 0.186667, 0]], [0.1056, [3, -0.186667, 0], [3, 0.213333, 0]], [0.1056, [3, -0.213333, 0], [3, 0.186667, 0]], [0.1056, [3, -0.186667, 0], [3, 0.2, 0]], [0.1056, [3, -0.2, 0], [3, 0.186667, 0]], [0.1056, [3, -0.186667, 0], [3, 0.133333, 0]], [0, [3, -0.133333, 0], [3, 0.146667, 0]], [0.9484, [3, -0.146667, 0], [3, 0.146667, 0]], [0.4912, [3, -0.146667, 0], [3, 0, 0]]])

names.append("RHipPitch")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[-0.564555, [3, -0.333333, 0], [3, 0.253333, 0]], [-0.575959, [3, -0.253333, 0], [3, 0.28, 0]], [0.131882, [3, -0.28, 0], [3, 0.266667, 0]], [0.131882, [3, -0.266667, 0], [3, 0.32, 0]], [0.131882, [3, -0.32, 0], [3, 0.173333, 0]], [0.131882, [3, -0.173333, 0], [3, 0.186667, 0]], [0.130348, [3, -0.186667, 0], [3, 0.2, 0]], [0.131882, [3, -0.2, 0], [3, 0.2, 0]], [0.131882, [3, -0.2, 0], [3, 0.186667, 0]], [0.131882, [3, -0.186667, 0], [3, 0.213333, 0]], [0.131882, [3, -0.213333, 0], [3, 0.186667, 0]], [0.131882, [3, -0.186667, 0], [3, 0.2, 0]], [0.131882, [3, -0.2, 0], [3, 0.186667, 0]], [0.131882, [3, -0.186667, 0], [3, 0.133333, 0]], [-0.622845, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.622845, [3, -0.146667, 0], [3, 0.146667, 0]], [0.130348, [3, -0.146667, 0], [3, 0, 0]]])

names.append("RHipRoll")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[-0.115008, [3, -0.333333, 0], [3, 0.253333, 0]], [-0.116542, [3, -0.253333, 0], [3, 0.28, 0]], [-0.0643861, [3, -0.28, 0], [3, 0.266667, 0]], [-0.0643861, [3, -0.266667, 0], [3, 0.32, 0]], [-0.0643861, [3, -0.32, 0], [3, 0.173333, 0]], [-0.0643861, [3, -0.173333, 0], [3, 0.186667, 0]], [-0.0643861, [3, -0.186667, 0], [3, 0.2, 0]], [-0.0643861, [3, -0.2, 0], [3, 0.2, 0]], [-0.0643861, [3, -0.2, 0], [3, 0.186667, 0]], [-0.0643861, [3, -0.186667, 0], [3, 0.213333, 0]], [-0.0643861, [3, -0.213333, 0], [3, 0.186667, 0]], [-0.0643861, [3, -0.186667, 0], [3, 0.2, 0]], [-0.0643861, [3, -0.2, 0], [3, 0.186667, 0]], [-0.0643861, [3, -0.186667, 0], [3, 0.133333, 0]], [-0.11961, [3, -0.133333, 0.00139452], [3, 0.146667, -0.00153397]], [-0.121144, [3, -0.146667, 0], [3, 0.146667, 0]], [-0.0643861, [3, -0.146667, 0], [3, 0, 0]]])

names.append("RHipYawPitch")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[-0.504645, [3, -0.333333, 0], [3, 0.253333, 0]], [-0.504645, [3, -0.253333, 0], [3, 0.28, 0]], [-0.1733, [3, -0.28, 0], [3, 0.266667, 0]], [-0.1733, [3, -0.266667, 0], [3, 0.32, 0]], [-0.1733, [3, -0.32, 0], [3, 0.173333, 0]], [-0.174835, [3, -0.173333, 0], [3, 0.186667, 0]], [-0.1733, [3, -0.186667, 0], [3, 0.2, 0]], [-0.1733, [3, -0.2, 0], [3, 0.2, 0]], [-0.1733, [3, -0.2, 0], [3, 0.186667, 0]], [-0.1733, [3, -0.186667, 0], [3, 0.213333, 0]], [-0.1733, [3, -0.213333, 0], [3, 0.186667, 0]], [-0.1733, [3, -0.186667, 0], [3, 0.2, 0]], [-0.1733, [3, -0.2, 0], [3, 0.186667, 0]], [-0.1733, [3, -0.186667, 0], [3, 0.133333, 0]], [-0.408002, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.408002, [3, -0.146667, 0], [3, 0.146667, 0]], [-0.1733, [3, -0.146667, 0], [3, 0, 0]]])

names.append("RKneePitch")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[2.11255, [3, -0.333333, 0], [3, 0.253333, 0]], [2.11255, [3, -0.253333, 0], [3, 0.28, 0]], [-0.091998, [3, -0.28, 0], [3, 0.266667, 0]], [-0.091998, [3, -0.266667, 0], [3, 0.32, 0]], [-0.0923279, [3, -0.32, 0], [3, 0.173333, 0]], [-0.0923279, [3, -0.173333, 0], [3, 0.186667, 0]], [-0.0923279, [3, -0.186667, 0], [3, 0.2, 0]], [-0.091998, [3, -0.2, 0], [3, 0.2, 0]], [-0.091998, [3, -0.2, 0], [3, 0.186667, 0]], [-0.0904641, [3, -0.186667, 0], [3, 0.213333, 0]], [-0.091998, [3, -0.213333, 0.000331349], [3, 0.186667, -0.00028993]], [-0.0923279, [3, -0.186667, 0], [3, 0.2, 0]], [-0.091998, [3, -0.2, 0], [3, 0.186667, 0]], [-0.091998, [3, -0.186667, 0], [3, 0.133333, 0]], [2.11255, [3, -0.133333, 0], [3, 0.146667, 0]], [2.11255, [3, -0.146667, 0], [3, 0.146667, 0]], [-0.091998, [3, -0.146667, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[1.67824, [3, -0.333333, 0], [3, 0.253333, 0]], [1.69818, [3, -0.253333, 0], [3, 0.28, 0]], [1.55859, [3, -0.28, 0.104499], [3, 0.266667, -0.0995232]], [1.08611, [3, -0.266667, 0], [3, 0.32, 0]], [1.08765, [3, -0.32, -0.00153418], [3, 0.173333, 0.000831014]], [1.26252, [3, -0.173333, 0], [3, 0.186667, 0]], [1.11526, [3, -0.186667, 0], [3, 0.2, 0]], [1.11679, [3, -0.2, 0], [3, 0.2, 0]], [-1.37135, [3, -0.2, 0], [3, 0.186667, 0]], [-1.35908, [3, -0.186667, 0], [3, 0.213333, 0]], [-1.4818, [3, -0.213333, 0], [3, 0.186667, 0]], [0.07214, [3, -0.186667, -0.482593], [3, 0.2, 0.517064]], [1.51717, [3, -0.2, -0.131485], [3, 0.186667, 0.122719]], [1.63989, [3, -0.186667, 0], [3, 0.133333, 0]], [1.63375, [3, -0.133333, 0.0012173], [3, 0.146667, -0.00133903]], [1.63222, [3, -0.146667, 0.00153411], [3, 0.146667, -0.00153411]], [1.53558, [3, -0.146667, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[-0.262356, [3, -0.333333, 0], [3, 0.253333, 0]], [-0.506262, [3, -0.253333, 0], [3, 0.28, 0]], [-0.219404, [3, -0.28, -0.116285], [3, 0.266667, 0.110748]], [0.174835, [3, -0.266667, 0], [3, 0.32, 0]], [0.168698, [3, -0.32, 0.00613674], [3, 0.173333, -0.00332407]], [0.06592, [3, -0.173333, 0], [3, 0.186667, 0]], [0.15029, [3, -0.186667, 0], [3, 0.2, 0]], [0.15029, [3, -0.2, 0], [3, 0.2, 0]], [-0.236277, [3, -0.2, 0.215289], [3, 0.186667, -0.200936]], [-1.09839, [3, -0.186667, 0], [3, 0.213333, 0]], [0.0735901, [3, -0.213333, 0], [3, 0.186667, 0]], [-0.260822, [3, -0.186667, 0], [3, 0.2, 0]], [-0.108956, [3, -0.2, 0], [3, 0.186667, 0]], [-0.16418, [3, -0.186667, 0], [3, 0.133333, 0]], [-0.162646, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.16418, [3, -0.146667, 0], [3, 0.146667, 0]], [-0.104354, [3, -0.146667, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([1, 1.76, 2.6, 3.4, 4.36, 4.88, 5.44, 6.04, 6.64, 7.2, 7.84, 8.4, 9, 9.56, 9.96, 10.4, 10.84])
keys.append([[0.0168321, [3, -0.333333, 0], [3, 0.253333, 0]], [0.151824, [3, -0.253333, -0.0352181], [3, 0.28, 0.0389252]], [0.239262, [3, -0.28, -0.087438], [3, 0.266667, 0.0832743]], [1.58458, [3, -0.266667, 0], [3, 0.32, 0]], [1.58458, [3, -0.32, 0], [3, 0.173333, 0]], [1.6306, [3, -0.173333, 0], [3, 0.186667, 0]], [1.53396, [3, -0.186667, 0], [3, 0.2, 0]], [1.53396, [3, -0.2, 0], [3, 0.2, 0]], [0.154892, [3, -0.2, 0], [3, 0.186667, 0]], [0.154892, [3, -0.186667, 0], [3, 0.213333, 0]], [0.259204, [3, -0.213333, -0.053724], [3, 0.186667, 0.0470085]], [0.45709, [3, -0.186667, 0], [3, 0.2, 0]], [0.176367, [3, -0.2, 0.0809316], [3, 0.186667, -0.0755362]], [-0.0123138, [3, -0.186667, 0], [3, 0.133333, 0]], [0.05058, [3, -0.133333, 0], [3, 0.146667, 0]], [0.0152981, [3, -0.146667, 0], [3, 0.146667, 0]], [0.0735901, [3, -0.146667, 0], [3, 0, 0]]])

def main(IP, port):
    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        motion = ALProxy("ALMotion", IP, port)
        #motion = ALProxy("ALMotion")
        motion.angleInterpolationBezier(names, times, keys)
    except BaseException, err:
        print err