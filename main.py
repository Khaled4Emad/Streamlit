import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Simple Form",
    page_icon=":smiley:",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "Simple Streamlit demo app"
    }
)

st.title("Welcome to my Streamlit App")
st.header("This is the main page")


# page = st.sidebar.selectbox("Select a page", ["Home", "Form"])
# if page == "Home":
#     st.switch_page( page="main.py")
# elif page == "Form":
#     st.switch_page(page="pages/form.py")

# st.title("Hi, I am Turtle code")
# st.header("this is a header")
# st.subheader("This is subheader")
# st.text("This is text")

# ------------------------------------------------------------------

# st.header("Headings")
# st.markdown("# heading 1")
# st.markdown("## heading 1")
# st.markdown("### heading 1")
# st.markdown("#### heading 1")
# st.markdown("##### heading 1")
# st.markdown("###### heading 1")

# ------------------------------------------------------------------

# st.header("formatting elements")
# st.markdown("**bold text**")
# st.markdown("*italic text*")
# st.markdown("***bold italic text***")

# ------------------------------------------------------------------

# st.header("order list")
# st.markdown("1. item 1")
# st.markdown("2. item 2")
# st.markdown("3. item 3")

# ------------------------------------------------------------------

# st.header("Unorder list")
# st.markdown("- item 1")
# st.markdown("- item 2")
# st.markdown("- item 3")

# ------------------------------------------------------------------

# st.header("quotes")
# st.markdown("> Turtle code")

# ------------------------------------------------------------------

# mystr = "print('i love python')"
# st.code(mystr)

# st.header("Horizontal Row")
# st.markdown("---")

# st.header("Links")
# st.markdown("[Google](https://www.google.com)")
# st.markdown("[Youtube](https://www.google.com)")

# ------------------------------------------------------------------

# st.header("Table")
# table = '''
# | Syntax | Description |
# |-------- | ---------- |
# | Header | Title |
# | Paragraph | Text |
# '''

# st.markdown(table)

# json = {
#     "a": "1,2,3",
#     "b": "4,5,6"
# }
# st.json(json)

# st.header("Emojy")
# st.markdown("This is so funny! :joy:")

# ------------------------------------------------------------------

# st.markdown('---')
# st.header("metric")

# st.metric("Accuracy", "95%")
# st.metric(label="Growth",value="25%",delta='3.2')
# st.markdown('---')

# accuracy = 0.95
# previous_accuracy = 0.93

# delta = accuracy - previous_accuracy

# st.metric(
#     label="Model Accuracy",
#     value=f"{accuracy*100:.2f}%",
#     delta=f"{delta*100:.2f}%"
# )
# st.markdown('---')

# col1, col2, col3 = st.columns(3)

# col1.metric("Train Accuracy", "98%")
# col2.metric("Validation Accuracy", "95%", "-1%")
# col3.metric("Loss", "0.12", "-0.03")

# st.markdown('---')

# st.metric(
#     label="Loss",
#     value="0.12",
#     delta="-0.03",
#     delta_color="inverse"
# )

   
# ------------------------------------------------------------------

#todo: Creating Table

# table  = ({
#     "Column1": [1,2,3,4,5],
#     "Column2": [6,7,8,9,10]
# })
# st.table(table)

# st.markdown('---')

# st.dataframe(table)
# st.markdown('---')

# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })

# df

# ------------------------------------------------------------------

#todo: Adding Audio, video, image

# st.image('./venv/media/image.jpg', caption="Beautiful Picture")
# st.audio('./venv/media/audio.oga')
# st.video('./venv/media/video.mp4', loop=True, autoplay=True)

# ------------------------------------------------------------------

#todo: application to create an input object and chack if it is in te list or not

#?: Accepting value from the user

# #! 1- string input
# name = st.text_input(label="Enter your name", placeholder="khaled")
# if name:
#     st.write("Hello", name)
# st.markdown('---')

# #! 2- integer input
# age = st.number_input(label="Enter your age", placeholder="Enter your age", min_value=0, max_value=120, step=1)
# if age:
#     st.write(f"You are {age} years old")
# st.markdown('---')

# #! 3- float input
# height = st.number_input(label="Enter your height", placeholder="Enter your height", min_value=0.0, max_value=2.5, step=0.1)
# if height:
#     st.write(f"You are {height} meters tall")
# st.markdown('---')

# #! 4- Slider input
# value = st.slider("Select", min_value=0, max_value=100, step=1)
# if value:
#     st.write(f"The value is {value}")
# st.markdown("---")

# #! 5- boolean input
# is_student = st.checkbox(label="Are you a student?")
# if is_student:
#     st.write("You are a student")
# else:
#     st.write("You are not a student")
# st.markdown('---')

# #! 6- Radio button input
# favorite_food = st.radio(label="Select your favorite food", options=["Pizza", "Burger", "Pasta"], index=None)
# if favorite_food:
#     st.write(f"Your favorite food is {favorite_food}")
# st.markdown('---')

# #! 7- Select input
# favorite_color = st.selectbox(label="Select your favorite color", options=["Red", "Green", "Blue"])
# if favorite_color:
#     st.write(f"Your favorite color is {favorite_color}")
# st.markdown('---')


# #! 8- Multiselect input
# favorite_fruits = st.multiselect(label="Select your favorite fruits", options=["Apple", "Banana", "Orange"])
# if favorite_fruits:
#     st.write(f"Your favorite fruits are {', '.join(favorite_fruits)}")
# st.markdown('---')

# #! 9- Date input
# favorite_date = st.date_input(label="Select your favorite date")
# if favorite_date:
#     st.write(f"Your favorite date is {favorite_date}")


# st.write("Welcome in my first web page")

# car_types = ['bmw', 'fiat', 'ford','toyota']
# car = st.text_input("Enter a car")
# button = st.button("check Availability")

# if button:
#     have_it = car.lower() in car_types
#     if have_it:
#         st.write("We have that car")
#     else:
#         st.write("we do not have that car")

#! Ordinary way to create a counter
# count = 0
# if st.button("Check !!"):
#     count+=1
# st.write(f"The count is {count}")

#! Using Session_State to create a counter
# if "count" not in st.session_state:
#     st.session_state.count = 0

# btn = st.button("Check !!")
# if btn:
#     st.session_state.count += 1
# st.write(f"The count is {st.session_state.count}")


# ------------------------------------------------------------------

#todo: creating image downloader

# st.image('./venv/media/image.jpg', caption="This is an image")
# file_name = st.text_input("Enter the name")
# st.write(file_name)

# with open('./venv/media/image.jpg', 'rb') as file: # rb: means binary mode
#     btn = st.download_button(
#         label = "Download image",
#         data = file,
#         file_name=file_name,
#         mime="image/png"
#     )

# st.subheader("📤 Upload → 👀 Preview → ⬇️ Download")

# #! 1. Upload file
# uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:

#     #! 2. Preview image
#     st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

#     #! 3. Get custom file name
#     file_name = st.text_input("Enter download file name", placeholder="downloaded_image.jpg")

#     #! 4. Download button
#     st.download_button(
#         label="Download Image",
#         data=uploaded_file,
#         file_name=file_name,
#         mime="image/jpeg"
#     )


#! Application to select an image from a list of images and download it

# if "selected_image" not in st.session_state:
#     st.session_state.selected_image = None

# image_list = ["./venv/media/basketball.jpg", "./venv/media/football.jpg", "./venv/media/microsoft.png", "./venv/media/python.png", "./venv/media/tennis.jpg", "./venv/media/image.jpg"]
# cols = st.columns(len(image_list))

# for col, img in zip(cols, image_list):
#     col.image(img, width=100, caption= img.split("/")[-1])
#     if col.button("Select", key=img):
#         st.session_state.selected_image = img
# if st.session_state.selected_image:

#     st.image(
#         st.session_state.selected_image,
#         caption="Selected Image",
#         use_container_width=True
#     )

#     if st.download_button(
#         label="Download Selected Image",
#         data=open(st.session_state.selected_image, "rb").read(),
#         file_name=st.session_state.selected_image.split("/")[-1],
#         mime="image/jpeg"
#     ):
#         st.success("Image downloaded successfully!")
# ------------------------------------------------------------------

#todo: Go to spacific website

# st.title("Welcome in my Website")

# image_list = ["../Streamlit/venv/media/amblem.png", "../Streamlit/venv/media/youtube.png"]
# caption_list = ["Amblem","Youtube"]
# st.header("Welcome to Turtle code")
# st.image(image=image_list, caption=caption_list, width=100)
# st.subheader("Turtle code is a youtube channel shares educational videos about computer science")
# st.link_button("Go To Youtube Channel","https://www.youtube.com")

# ------------------------------------------------------------------

# todo: Check Box

# image_list = ["../Streamlit/venv/media/amblem.png", "../Streamlit/venv/media/youtube.png"]
# caption_list = ["Amblem","Youtube"]
# st.header("Welcome to Turtle code")

# cols = st.columns(2)

# with cols[0]:
#     images = st.checkbox("Do You want see photoes?")

# with cols[1]:
#     codes = st.checkbox("Do You Need To show code?")

# col1, col2 = st.columns(2)

# with col1:
#     if images:
#         st.image(image=image_list, caption=caption_list, width=80)

# with col2:
#     if codes:
#         st.code("print('Hello world!!')")



# ------------------------------------------------------------------


#todo: Toggle Object

# st.header("Welcome to Toggle Object")

# col1, col2, col3 = st.columns(3)

# with col1:
#     toggle_image = st.toggle("Enable Image")

# with col2:
#     toggle_audio = st.toggle("Enable Audio")

# with col3:
#     toggle_video = st.toggle("Enable Vodio")

# if toggle_image:
#     st.image("../Streamlit/venv/media/youtube.png", width=80, caption="Youtube")

# if toggle_audio:
#     st.audio("../Streamlit/venv/media/audio.oga")

# if toggle_video:
#     st.video("../Streamlit/venv/media/video.mp4")

# ------------------------------------------------------------------

#todo: creating radio button

# if "disabled" not in st.session_state:
#     st.session_state.disabled = False

# radio_button = st.radio("Choose The Course",
#                         ["HTML | CSS :lying_face:","JS :sweat:","Python :alien:"],
#                         index= None,
#                         key="visibility",
#                         disabled=st.session_state.disabled)



# if radio_button:
#     st.write(radio_button)

# if radio_button == "HTML | CSS :lying_face:":
#     st.write("HTML | CSS :lying_face:")
#     st.session_state.disabled = True

# if radio_button == "JS :sweat:":
#     st.write("JS :sweat:")
#     st.session_state.disabled = True

# if radio_button == "Python :alien:":
#     st.write("Python :alien:")
#     st.session_state.disabled = True



#? Session_State Explain
# if "count" not in st.session_state:
#     st.session_state.count = 0

# if st.button("Click me"):
#     st.session_state.count += 1

# st.write("Count:", st.session_state.count)



# if "count2" not in st.session_state:
#     st.session_state.count2 = 0 

# if st.button("Click me 2"):
#     st.session_state.count2 += 1

# st.write("Count:", st.session_state.count2)



# if "count3" not in st.session_state:
#     st.session_state.count3 = 0

# if st.button("Click me 3"):
#     st.session_state.count3 += 1

# st.write("Count:", st.session_state.count3)


# ------------------------------------------------------------------































































