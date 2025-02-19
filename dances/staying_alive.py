import sys
import time
from naoqi import ALProxy


def main(robotIP, port):
	names = list()
	times = list()
	keys = list()

	try:
		ttsProxy = ALProxy("ALTextToSpeech",robotIP,port)
	except Exception,e:
		print("Could not create a proxy to ALTextToSpeech")

	#ttsProxy.say("...")

	names.append("HeadPitch")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[-0.00847434, [3, -0.333333, 0], [3, 0.2, 0]], [-0.00847434, [3, -0.2, 0], [3, 0.2, 0]], [-0.00847434, [3, -0.2, 0], [3, 0.2, 0]], [-0.00847434, [3, -0.2, 0], [3, 0.2, 0]], [-0.00847434, [3, -0.2, 0], [3, 0.2, 0]], [-0.00847434, [3, -0.2, 0], [3, 0.2, 0]], [-0.00847434, [3, -0.2, 0], [3, 0.2, 0]], [-0.00847434, [3, -0.2, 0], [3, 0.2, 0]], [-0.00847434, [3, -0.2, 0], [3, 0, 0]]])

	names.append("HeadYaw")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[1.19972, [3, -0.333333, 0], [3, 0.2, 0]], [0, [3, -0.2, 0], [3, 0.2, 0]], [1.19972, [3, -0.2, 0], [3, 0.2, 0]], [0, [3, -0.2, 0.399908], [3, 0.2, -0.399908]], [-1.19972, [3, -0.2, 0], [3, 0.2, 0]], [0, [3, -0.2, 0], [3, 0.2, 0]], [-1.19972, [3, -0.2, 0], [3, 0.2, 0]], [0, [3, -0.2, 0], [3, 0.2, 0]], [-0.00464368, [3, -0.2, 0], [3, 0, 0]]])

	names.append("LAnklePitch")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[-0.242601, [3, -0.333333, 0], [3, 0.2, 0]], [-0.342535, [3, -0.2, 0], [3, 0.2, 0]], [-0.342535, [3, -0.2, 0], [3, 0.2, 0]], [-0.342535, [3, -0.2, 0], [3, 0.2, 0]], [-0.242428, [3, -0.2, -0.00764976], [3, 0.2, 0.00764976]], [-0.234778, [3, -0.2, 0], [3, 0.2, 0]], [-0.234778, [3, -0.2, 0], [3, 0.2, 0]], [-0.234778, [3, -0.2, 0], [3, 0.2, 0]], [-0.340758, [3, -0.2, 0], [3, 0, 0]]])

	names.append("LAnkleRoll")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[0.00872665, [3, -0.333333, 0], [3, 0.2, 0]], [-0.00242534, [3, -0.2, 0], [3, 0.2, 0]], [-0.00242534, [3, -0.2, 0], [3, 0.2, 0]], [-0.00242534, [3, -0.2, 0], [3, 0.2, 0]], [-0.00949218, [3, -0.2, 0], [3, 0.2, 0]], [-0.00242534, [3, -0.2, 0], [3, 0.2, 0]], [-0.00242534, [3, -0.2, 0], [3, 0.2, 0]], [-0.00242534, [3, -0.2, 0], [3, 0.2, 0]], [-0.00242534, [3, -0.2, 0], [3, 0, 0]]])

	names.append("LElbowRoll")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[-0.138215, [3, -0.333333, 0], [3, 0.2, 0]], [-0.445724, [3, -0.2, 0], [3, 0.2, 0]], [-0.138215, [3, -0.2, 0], [3, 0.2, 0]], [-0.445724, [3, -0.2, 0], [3, 0.2, 0]], [-0.381585, [3, -0.2, 0], [3, 0.2, 0]], [-0.381585, [3, -0.2, 0], [3, 0.2, 0]], [-0.381585, [3, -0.2, 0], [3, 0.2, 0]], [-0.381585, [3, -0.2, 0], [3, 0.2, 0]], [-1.00367, [3, -0.2, 0], [3, 0, 0]]])

	names.append("LElbowYaw")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[-1.30029, [3, -0.333333, 0], [3, 0.2, 0]], [-0.657336, [3, -0.2, 0], [3, 0.2, 0]], [-1.30029, [3, -0.2, 0], [3, 0.2, 0]], [-0.657336, [3, -0.2, 0], [3, 0.2, 0]], [-0.65816, [3, -0.2, 0], [3, 0.2, 0]], [-0.65816, [3, -0.2, 0], [3, 0.2, 0]], [-0.65816, [3, -0.2, 0], [3, 0.2, 0]], [-0.65816, [3, -0.2, 0], [3, 0.2, 0]], [-1.38323, [3, -0.2, 0], [3, 0, 0]]])

	names.append("LHand")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[0.994649, [3, -0.333333, 0], [3, 0.2, 0]], [0.4, [3, -0.2, 0], [3, 0.2, 0]], [0.994649, [3, -0.2, 0], [3, 0.2, 0]], [0.4, [3, -0.2, 0.122569], [3, 0.2, -0.122569]], [0.259234, [3, -0.2, 0], [3, 0.2, 0]], [0.259234, [3, -0.2, 0], [3, 0.2, 0]], [0.259234, [3, -0.2, 0], [3, 0.2, 0]], [0.259234, [3, -0.2, 0], [3, 0.2, 0]], [0.259234, [3, -0.2, 0], [3, 0, 0]]])

	names.append("LHipPitch")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[-0.588176, [3, -0.333333, 0], [3, 0.2, 0]], [-0.455433, [3, -0.2, 0], [3, 0.2, 0]], [-0.455433, [3, -0.2, 0], [3, 0.2, 0]], [-0.455433, [3, -0.2, 0], [3, 0.2, 0]], [-0.58434, [3, -0.2, 0.00262321], [3, 0.2, -0.00262321]], [-0.586963, [3, -0.2, 0], [3, 0.2, 0]], [-0.586963, [3, -0.2, 0], [3, 0.2, 0]], [-0.586963, [3, -0.2, 0], [3, 0.2, 0]], [-0.45, [3, -0.2, 0], [3, 0, 0]]])

	names.append("LHipRoll")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[-0.0913434, [3, -0.333333, 0], [3, 0.2, 0]], [0.00498489, [3, -0.2, 0], [3, 0.2, 0]], [0.00498489, [3, -0.2, 0], [3, 0.2, 0]], [0.00498489, [3, -0.2, 0], [3, 0.2, 0]], [0.0964097, [3, -0.2, -0.00936212], [3, 0.2, 0.00936212]], [0.105772, [3, -0.2, 0], [3, 0.2, 0]], [0.105772, [3, -0.2, 0], [3, 0.2, 0]], [0.105772, [3, -0.2, 0], [3, 0.2, 0]], [0.00848469, [3, -0.2, 0], [3, 0, 0]]])

	names.append("LHipYawPitch")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[-0.00730551, [3, -0.333333, 0], [3, 0.2, 0]], [-0.00847434, [3, -0.2, 0], [3, 0.2, 0]], [-0.00847434, [3, -0.2, 0], [3, 0.2, 0]], [-0.00847434, [3, -0.2, 0], [3, 0.2, 0]], [-0.00730551, [3, -0.2, 0], [3, 0.2, 0]], [-0.00847434, [3, -0.2, 0], [3, 0.2, 0]], [-0.00847434, [3, -0.2, 0], [3, 0.2, 0]], [-0.00847434, [3, -0.2, 0], [3, 0.2, 0]], [-0.00847434, [3, -0.2, 0], [3, 0, 0]]])

	names.append("LKneePitch")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[0.708487, [3, -0.333333, 0], [3, 0.2, 0]], [0.701287, [3, -0.2, 0], [3, 0.2, 0]], [0.701287, [3, -0.2, 0], [3, 0.2, 0]], [0.701287, [3, -0.2, 0], [3, 0.2, 0]], [0.709886, [3, -0.2, -0.0015935], [3, 0.2, 0.0015935]], [0.71148, [3, -0.2, 0], [3, 0.2, 0]], [0.71148, [3, -0.2, 0], [3, 0.2, 0]], [0.71148, [3, -0.2, 0], [3, 0.2, 0]], [0.700921, [3, -0.2, 0], [3, 0, 0]]])

	names.append("LShoulderPitch")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[-0.608631, [3, -0.333333, 0], [3, 0.2, 0]], [0.919783, [3, -0.2, 0], [3, 0.2, 0]], [-0.608631, [3, -0.2, 0], [3, 0.2, 0]], [0.919783, [3, -0.2, -0.00474029], [3, 0.2, 0.00474029]], [0.924524, [3, -0.2, 0], [3, 0.2, 0]], [0.924524, [3, -0.2, 0], [3, 0.2, 0]], [0.924524, [3, -0.2, 0], [3, 0.2, 0]], [0.924524, [3, -0.2, 0], [3, 0.2, 0]], [1.39334, [3, -0.2, 0], [3, 0, 0]]])

	names.append("LShoulderRoll")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[0.815868, [3, -0.333333, 0], [3, 0.2, 0]], [-0.0711377, [3, -0.2, 0], [3, 0.2, 0]], [0.815868, [3, -0.2, 0], [3, 0.2, 0]], [-0.0711377, [3, -0.2, 0.0592056], [3, 0.2, -0.0592056]], [-0.130343, [3, -0.2, 0], [3, 0.2, 0]], [-0.118499, [3, -0.2, 0], [3, 0.2, 0]], [-0.130343, [3, -0.2, 0], [3, 0.2, 0]], [-0.118499, [3, -0.2, -0.0118445], [3, 0.2, 0.0118445]], [0.294489, [3, -0.2, 0], [3, 0, 0]]])

	names.append("LWristYaw")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[1.81842, [3, -0.333333, 0], [3, 0.2, 0]], [-0.0671777, [3, -0.2, 0], [3, 0.2, 0]], [1.81842, [3, -0.2, 0], [3, 0.2, 0]], [-0.0671777, [3, -0.2, 0], [3, 0.2, 0]], [-0.0663408, [3, -0.2, 0], [3, 0.2, 0]], [-0.0663408, [3, -0.2, 0], [3, 0.2, 0]], [-0.0663408, [3, -0.2, 0], [3, 0.2, 0]], [-0.0663408, [3, -0.2, 0], [3, 0.2, 0]], [-0.00262915, [3, -0.2, 0], [3, 0, 0]]])

	names.append("RAnklePitch")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[-0.242428, [3, -0.333333, 0], [3, 0.2, 0]], [-0.234778, [3, -0.2, 0], [3, 0.2, 0]], [-0.234778, [3, -0.2, 0], [3, 0.2, 0]], [-0.234778, [3, -0.2, 0], [3, 0.2, 0]], [-0.242601, [3, -0.2, 0.00782255], [3, 0.2, -0.00782255]], [-0.342535, [3, -0.2, 0], [3, 0.2, 0]], [-0.342535, [3, -0.2, 0], [3, 0.2, 0]], [-0.342535, [3, -0.2, 0], [3, 0.2, 0]], [-0.342535, [3, -0.2, 0], [3, 0, 0]]])

	names.append("RAnkleRoll")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[0.00949218, [3, -0.333333, 0], [3, 0.2, 0]], [0.00242534, [3, -0.2, 0], [3, 0.2, 0]], [0.00242534, [3, -0.2, 0], [3, 0.2, 0]], [0.00242534, [3, -0.2, 0], [3, 0.2, 0]], [-0.00872665, [3, -0.2, 0], [3, 0.2, 0]], [0.00242534, [3, -0.2, 0], [3, 0.2, 0]], [0.00242534, [3, -0.2, 0], [3, 0.2, 0]], [0.00242534, [3, -0.2, 0], [3, 0.2, 0]], [0.00242534, [3, -0.2, 0], [3, 0, 0]]])

	names.append("RElbowRoll")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[0.381585, [3, -0.333333, 0], [3, 0.2, 0]], [0.381585, [3, -0.2, 0], [3, 0.2, 0]], [0.381585, [3, -0.2, 0], [3, 0.2, 0]], [0.381585, [3, -0.2, 0], [3, 0.2, 0]], [0.138215, [3, -0.2, 0], [3, 0.2, 0]], [0.445724, [3, -0.2, 0], [3, 0.2, 0]], [0.138215, [3, -0.2, 0], [3, 0.2, 0]], [0.445724, [3, -0.2, -0.144335], [3, 0.2, 0.144335]], [1.00422, [3, -0.2, 0], [3, 0, 0]]])

	names.append("RElbowYaw")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[0.65816, [3, -0.333333, 0], [3, 0.2, 0]], [0.65816, [3, -0.2, 0], [3, 0.2, 0]], [0.65816, [3, -0.2, 0], [3, 0.2, 0]], [0.65816, [3, -0.2, 0], [3, 0.2, 0]], [1.30029, [3, -0.2, 0], [3, 0.2, 0]], [0.657336, [3, -0.2, 0], [3, 0.2, 0]], [1.30029, [3, -0.2, 0], [3, 0.2, 0]], [0.657336, [3, -0.2, 0], [3, 0.2, 0]], [1.38304, [3, -0.2, 0], [3, 0, 0]]])

	names.append("RHand")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[0.259234, [3, -0.333333, 0], [3, 0.2, 0]], [0.259234, [3, -0.2, 0], [3, 0.2, 0]], [0.259234, [3, -0.2, 0], [3, 0.2, 0]], [0.259234, [3, -0.2, 0], [3, 0.2, 0]], [0.994649, [3, -0.2, 0], [3, 0.2, 0]], [0.4, [3, -0.2, 0], [3, 0.2, 0]], [0.994649, [3, -0.2, 0], [3, 0.2, 0]], [0.4, [3, -0.2, 0.124108], [3, 0.2, -0.124108]], [0.25, [3, -0.2, 0], [3, 0, 0]]])

	names.append("RHipPitch")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[-0.58434, [3, -0.333333, 0], [3, 0.2, 0]], [-0.586963, [3, -0.2, 0], [3, 0.2, 0]], [-0.586963, [3, -0.2, 0], [3, 0.2, 0]], [-0.586963, [3, -0.2, 0], [3, 0.2, 0]], [-0.588176, [3, -0.2, 0], [3, 0.2, 0]], [-0.455433, [3, -0.2, 0], [3, 0.2, 0]], [-0.455433, [3, -0.2, 0], [3, 0.2, 0]], [-0.455433, [3, -0.2, 0], [3, 0.2, 0]], [-0.455433, [3, -0.2, 0], [3, 0, 0]]])

	names.append("RHipRoll")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[-0.0964097, [3, -0.333333, 0], [3, 0.2, 0]], [-0.105772, [3, -0.2, 0], [3, 0.2, 0]], [-0.105772, [3, -0.2, 0], [3, 0.2, 0]], [-0.105772, [3, -0.2, 0], [3, 0.2, 0]], [0.0913434, [3, -0.2, 0], [3, 0.2, 0]], [-0.00498489, [3, -0.2, 0], [3, 0.2, 0]], [-0.00498489, [3, -0.2, 0], [3, 0.2, 0]], [-0.00498489, [3, -0.2, 0], [3, 0.2, 0]], [-0.00498489, [3, -0.2, 0], [3, 0, 0]]])

	names.append("RHipYawPitch")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[-0.00847434, [3, -0.333333, 0], [3, 0.2, 0]], [-0.00847434, [3, -0.2, 0], [3, 0.2, 0]], [-0.00847434, [3, -0.2, 0], [3, 0.2, 0]], [-0.00847434, [3, -0.2, 0], [3, 0.2, 0]], [-0.00847434, [3, -0.2, 0], [3, 0.2, 0]], [-0.00847434, [3, -0.2, 0], [3, 0.2, 0]], [-0.00847434, [3, -0.2, 0], [3, 0.2, 0]], [-0.00847434, [3, -0.2, 0], [3, 0.2, 0]], [-0.00847434, [3, -0.2, 0], [3, 0, 0]]])

	names.append("RKneePitch")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[0.709886, [3, -0.333333, 0], [3, 0.2, 0]], [0.71148, [3, -0.2, 0], [3, 0.2, 0]], [0.71148, [3, -0.2, 0], [3, 0.2, 0]], [0.71148, [3, -0.2, 0], [3, 0.2, 0]], [0.708487, [3, -0.2, 0.00169879], [3, 0.2, -0.00169879]], [0.701287, [3, -0.2, 0], [3, 0.2, 0]], [0.701287, [3, -0.2, 0], [3, 0.2, 0]], [0.701287, [3, -0.2, 0], [3, 0.2, 0]], [0.701287, [3, -0.2, 0], [3, 0, 0]]])

	names.append("RShoulderPitch")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[0.924524, [3, -0.333333, 0], [3, 0.2, 0]], [0.924524, [3, -0.2, 0], [3, 0.2, 0]], [0.924524, [3, -0.2, 0], [3, 0.2, 0]], [0.924524, [3, -0.2, 0], [3, 0.2, 0]], [-0.608631, [3, -0.2, 0], [3, 0.2, 0]], [0.919783, [3, -0.2, 0], [3, 0.2, 0]], [-0.608631, [3, -0.2, 0], [3, 0.2, 0]], [0.919783, [3, -0.2, -0.333765], [3, 0.2, 0.333765]], [1.39396, [3, -0.2, 0], [3, 0, 0]]])

	names.append("RShoulderRoll")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[0.130343, [3, -0.333333, 0], [3, 0.2, 0]], [0.118499, [3, -0.2, 0], [3, 0.2, 0]], [0.130343, [3, -0.2, 0], [3, 0.2, 0]], [0.118499, [3, -0.2, 0.0118445], [3, 0.2, -0.0118445]], [-0.815868, [3, -0.2, 0], [3, 0.2, 0]], [0.0711377, [3, -0.2, 0], [3, 0.2, 0]], [-0.815868, [3, -0.2, 0], [3, 0.2, 0]], [0.0711377, [3, -0.2, 0], [3, 0.2, 0]], [-0.295554, [3, -0.2, 0], [3, 0, 0]]])

	names.append("RWristYaw")
	times.append([1, 1.6, 2.2, 2.8, 3.4, 4, 4.6, 5.2, 5.8])
	keys.append([[0.0663408, [3, -0.333333, 0], [3, 0.2, 0]], [0.0663408, [3, -0.2, 0], [3, 0.2, 0]], [0.0663408, [3, -0.2, 0], [3, 0.2, 0]], [0.0663408, [3, -0.2, 0], [3, 0.2, 0]], [-1.81842, [3, -0.2, 0], [3, 0.2, 0]], [0.0671777, [3, -0.2, 0], [3, 0.2, 0]], [-1.81842, [3, -0.2, 0], [3, 0.2, 0]], [0.0671777, [3, -0.2, 0], [3, 0.2, 0]], [0.00266231, [3, -0.2, 0], [3, 0, 0]]])

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