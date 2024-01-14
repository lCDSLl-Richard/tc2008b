import math
import numpy as np


class MatrixOp:
    def __init__(self):
        self.T = np.identity(4)
        self.R = np.identity(4)
        self.A = np.identity(4)
        self.S = np.identity(4)

    def translate(self, tx: float, ty: float, tz: float):
        self.T = np.identity(4)
        self.T[0][3] = tx
        self.T[1][3] = ty
        self.T[2][3] = tz
        self.A = self.T @ self.A

    def rotateX(self, angle: float):
        self.R = np.identity(4)
        rad = math.radians(angle)
        self.R[1][1] = math.cos(rad)
        self.R[1][2] = -math.sin(rad)
        self.R[2][1] = math.sin(rad)
        self.R[2][2] = math.cos(rad)
        self.A = self.R @ self.A

    def rotateY(self, angle: float):
        self.R = np.identity(4)
        rad = math.radians(angle)
        self.R[0][0] = math.cos(rad)
        self.R[0][2] = -math.sin(rad)
        self.R[2][0] = math.sin(rad)
        self.R[2][2] = math.cos(rad)
        self.A = self.R @ self.A

    def rotateZ(self, angle: float):
        self.R = np.identity(4)
        rad = math.radians(angle)
        self.R[0][0] = math.cos(rad)
        self.R[0][1] = -math.sin(rad)
        self.R[1][0] = math.sin(rad)
        self.R[1][1] = math.cos(rad)
        self.A = self.R @ self.A

    def rotate(self, angle: float, x: float, y: float, z: float):
        if y == 0 and z == 0:
            self.rotateX(angle)
            return

        v = math.sqrt(x**2 + y**2 + z**2)
        a = x / v
        b = y / v
        c = z / v
        d = math.sqrt(b**2 + c**2)

        rx = np.identity(4)
        rx[1][1] = c / d
        rx[1][2] = -b / d
        rx[2][1] = b / d
        rx[2][2] = c / d

        ry = np.identity(4)
        ry[0][0] = d
        ry[0][2] = -a
        ry[2][0] = a
        ry[2][2] = d

        # Apply rotations in the order of X, Y, and Z
        self.A = rx @ self.A
        self.A = ry @ self.A
        self.rotateZ(angle)

        # rx[1][2] = b / d
        # rx[2][1] = -b / d

        # ry[0][2] = -a
        # ry[2][0] = a

        print(rx)

        self.A = np.linalg.inv(ry) @ self.A
        self.A = np.linalg.inv(rx) @ self.A

    def scale(self, sx: float, sy: float, sz: float):
        self.S = np.diag([sx, sy, sz, 1])
        self.A = self.S @ self.A

    def apply(self, points: np.ndarray[float]):
        res = (self.A @ points.T).T
        for i in range(0, res.shape[1] + 1):
            for j in range(0, 4):
                points[i][j] = res[i][j]

    def loadIdentity(self):
        self.A = np.identity(4)
