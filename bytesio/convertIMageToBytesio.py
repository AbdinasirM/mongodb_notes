from io import BytesIO
from PIL import Image

# Create a sample image in BytesIO
image = Image.new('RGB', (100, 100), 'red')
bytes_io = BytesIO()
image.save(bytes_io, format='PNG')

# Convert BytesIO to bytes
image_bytes = bytes_io.getvalue()

# # Check the type
# print(type(image_bytes))  # <class 'bytes'>


buffer = BytesIO(image_bytes)


image = Image.open(buffer)

image.show(command="display")  # if 'display' (from ImageMagick) is installed
