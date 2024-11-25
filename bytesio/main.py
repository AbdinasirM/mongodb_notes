from io import BytesIO


'''
Creating a BytesIO Object

To create an empty in-memory binary stream, you simply initialize BytesIO:
'''

buffer = BytesIO()


'''
Writing Data to BytesIO

You can write binary data to this in-memory "file" using the .write() method. Data must be in bytes (not a string, so it often needs to be encoded first):

'''

# buffer.write(b"Hello, world") # Wrigting bytes directly

#Or, if you have a string:

buffer.write("Hello, world!".encode())  # Encoding a string to bytes

#Reading Data from BytesIO

'''

To read the data you wrote, first move the cursor back to the beginning of the buffer using .seek(0):

'''
buffer.seek(0) # Go back to the beggining of the buffer

data = buffer.read() # read all data

print(data) # Outputs: b'Hello, world!'


