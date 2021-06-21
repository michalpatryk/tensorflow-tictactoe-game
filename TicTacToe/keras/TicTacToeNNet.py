from keras.models import *
from keras.layers import *
from keras.optimizers import *

class TicTacToeNNet():
    def __init__(self, game, args):
        self.board_x, self.board_y = game.getBoardSize()
        self.action_size = game.getActionSize()
        self.args = args

        # Instantiate a Keras tensor with shape of our board
        self.input_boards = Input(shape=(self.board_x, self.board_y))
        # Reshape our data to be board_x * board_y * 1
        x_image = Reshape((self.board_x, self.board_y, 1))(self.input_boards)
        # Activation layers with rectified linear unit activation
        h_conv1 = Activation('relu')(BatchNormalization(axis=3)(
            Conv2D(args.num_channels, 3, padding='same')(x_image)))
        h_conv2 = Activation('relu')(BatchNormalization(axis=3)(
            Conv2D(args.num_channels, 3, padding='same')(h_conv1)))
        h_conv3 = Activation('relu')(BatchNormalization(axis=3)(
            Conv2D(args.num_channels, 3, padding='same')(h_conv2)))
        h_conv4 = Activation('relu')(BatchNormalization(axis=3)(
            Conv2D(args.num_channels, 3, padding='same')(h_conv3)))
        # Flatten the input -> make 1 axis from 3 axis
        h_conv4_flat = Flatten()(h_conv4)

        s_fc1 = Dropout(args.dropout)(Activation('relu')(BatchNormalization(axis=1)(Dense(1024)(h_conv4_flat))))
        s_fc2 = Dropout(args.dropout)(Activation('relu')(BatchNormalization(axis=1)(Dense(512)(s_fc1))))
        # pi -> estimate of the policy from state s
        self.pi = Dense(self.action_size, activation='softmax', name='pi')(s_fc2)
        self.v = Dense(1, activation='tanh', name='v')(s_fc2)

        self.model = Model(inputs=self.input_boards, outputs=[self.pi, self.v])
        self.model.compile(loss=['categorical_crossentropy', 'mean_squared_error'], optimizer=Adam(args.lr))