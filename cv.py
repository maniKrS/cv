import streamlit as st
import cv2
import numpy as np

# Function to capture video frames
def capture_video_frame():
    cap = cv2.VideoCapture(1)
    _, frame = cap.read()
    cap.release()
    return frame

# Streamlit UI
st.title("OpenCV Video Display")

# Button to capture and display a video frame
if st.button("Show Frame"):
    frame = capture_video_frame()
    st.image(frame, channels="BGR", caption="Live Video Frame", use_column_width=True)


