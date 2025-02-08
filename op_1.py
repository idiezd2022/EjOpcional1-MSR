# Importamos librerias.
import pybullet as p
import pybullet_data
import time

# Conectacmos a pybullet y los archivos en cuestion.
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Configuramos la gravedad.
p.setGravity(0, 0, -9.8)

# Carfamos el plano como base de la simulacion.
planeId = p.loadURDF("plane.urdf")

# Definimos la posicion y orientacion inicial del robot en angulos de Euler.
euler_angles = [0,0,0]
startOrientation = p.getQuaternionFromEuler(euler_angles)
startPosition = [0,0,1]

# Cargamos el modelo URDF del robot.
robotId = p.loadURDF("op1.urdf", startPosition, startOrientation)

# Añadimos los parametros de friccion y torque
frictionId = p.addUserDebugParameter("jointFriction", 0, 10, 5)
torqueId = p.addUserDebugParameter("jointTorque", -10, 10, 5)

while (1):
    frictionForce = p.readUserDebugParameter(frictionId)
    jointTorque = p.readUserDebugParameter(torqueId)

    # Los aplicamos al joint correspondiente
    p.setJointMotorControl2(robotId, 1, p.TORQUE_CONTROL, force=jointTorque) 
    p.setJointMotorControl2(robotId, 1, p.VELOCITY_CONTROL, force=frictionForce)

    # Control del tiempo del simulador.
    p.stepSimulation()
    time.sleep(1./240.)


