from piece import Piece, Type

class Bishop(Piece):
    def __init__(self, color):
        super(Bishop, self).__init__(Type.BISHOP, color)