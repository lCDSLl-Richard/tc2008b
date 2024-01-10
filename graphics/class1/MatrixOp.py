import math
import numpy as np


class MatrixOp:
    def __init__(self):
        self.T = np.identity(4)
        self.R = np.identity(4)
        self.A = np.identity(4)

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

    def apply(self, points: np.ndarray[float]):
        res = (self.A @ points.T).T
        for i in range(0, res.shape[1] + 1):
            for j in range(0, 4):
                points[i][j] = res[i][j]
