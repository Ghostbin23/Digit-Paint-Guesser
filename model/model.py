# -- IMPORTS AND DATA SPLIT --
import tensorflow as tf

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data() # x is image itself and y is its labels

x_train = tf.keras.utils.normalize(x_train, axis = 1) # normalising data, normalising the NumPy array to an axis
x_test = tf.keras.utils.normalize(x_test, axis = 1) # normalising data, normalising the NumPy array to an axis

# -- GLOBAL STRUCTURE VARIABLES

ROWS = 28
COLS = 28
CHANNELS = 1
NUM_CLASSES = 10

# -- DEFINING SEQUENTIAL MODEL

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu',
                           input_shape=(28,28,1)),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.compile(optimizer = 'adam', loss='sparse_categorical_crossentropy', metrics = ['accuracy'])
model.summary()

model.fit(x_train,y_train,epochs = 10)

model.save('digit_model.keras')

# -- EVALUATING MODEL
#model  = tf.keras.models.load_model('newmodel.keras')
#loss, accuracy = model.evaluate(x_test,y_test)
#print(f'Loss: {loss} \nAccuracy: {accuracy}')

#image_number = 1
#while os.path.isfile(f"digits/digit{image_number}.png"):
#    try:
#        img = cv2.imread(f"digits/digit{image_number}.png")[:,:,0] # no shape, no colour, just pixels
#        img = np.invert(np.array([img])) # by default, is white on black, so we inver to black on white
#        pred = model.predict(img)
#        print(f"This digit is probably a {np.argmax(pred)}") # highest confidence prediction
#        plt.imshow(img[0], cmap = plt.cm.binary)
#        plt.show()
#    except:
#        print("Error!") # TODO: handle possible errors
#    finally:
#        image_number += 1