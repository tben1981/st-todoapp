import streamlit as st
from PIL import Image
from streamlit import session_state


def getimage():
	file=session_state['uploader']
	print(type(file))


st.subheader("Color to Grayscale Converter")

uploaded_image=st.file_uploader("Drag and drop file here" )

with st.expander("Start camera"):
	camera_image=st.camera_input("camera")

#if session_state["uploader"]!='NULL':#
#	uploaded_file=session_state["uploader"]
#	img=Image.open(camera_image)
#	grayimg= img.convert("L") #convert to grayscale
#	st.image(grayimg)


# Create pillow image item, convert go grayscale print )
if camera_image:   #if image is not taken, it will be False
	img = Image.open(camera_image)
	grayimg= img.convert("L") #convert to grayscale
	st.image(grayimg)

# Create pillow image item, convert go grayscale print )
if uploaded_image:   #if image is not taken, it will be False
	img = Image.open(uploaded_image)
	grayimg= img.convert("L") #convert to grayscale
	st.image(grayimg)