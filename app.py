f = st.file_uploader("Upload file")
if f is not None:
    file_details = {"FileName":f.name,"FileType":f.type}
    st.write(file_details)       
with open(f.name,"wb") as ff: 
      ff.write(f.getbuffer())         
st.success("Saved File")

tfile = tempfile.NamedTemporaryFile(delete=False) 
tfile.write(f.read())


vf = cv2.VideoCapture(tfile.name)

stframe = st.empty()

while vf.isOpened():
    ret, frame = vf.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    stframe.image(gray)
    
video_file = open('output.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
