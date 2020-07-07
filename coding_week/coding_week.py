
import face_recognition

image = face_recognition.load_image_file("PersonalsausweisMieterVorne.jpeg")
face_locations = face_recognition.face_locations(image)

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

@app.route('/')
@app.route('/hello')
def hello():
    # Render the page
    return "Hello Python!"

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)
