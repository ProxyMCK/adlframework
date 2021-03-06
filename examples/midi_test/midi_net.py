from keras.models import Sequential
from keras.layers import Dense, LSTM, Reshape
from adlframework.nets.net import Net


class midi_test(Net):
	@Net.build_model_wrapper
	def build_model(self):
		model = Sequential()
		model.add(Reshape((100, -1), input_shape=self.input_shape, name='Reshape_1'))
		model.add(LSTM(120, activation='relu',
							return_sequences=True))
		model.add(LSTM(120, activation='relu', return_sequences=True))
		model.add(LSTM(120, activation='relu'))
		model.add(Dense(self.target_shape))
		return model