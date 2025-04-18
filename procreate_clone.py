import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
from io import BytesIO
import base64

# Page setup
st.set_page_config(page_title="Procreate Clone", layout="wide")
st.title("🎨 Procreate-like Drawing App")

# Sidebar options
st.sidebar.header("🛠️ Tool Settings")
stroke_width = st.sidebar.slider("✏️ Brush width", 1, 25, 5)
stroke_color = st.sidebar.color_picker("🎨 Brush color", "#000000")
bg_color = st.sidebar.color_picker("🧱 Background color", "#ffffff")
drawing_mode = st.sidebar.selectbox("✍️ Drawing tool", ["freedraw", "line", "rect", "circle", "transform"])
realtime_update = st.sidebar.checkbox("Update in realtime", True)

# Canvas
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Transparent fill
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    update_streamlit=realtime_update,
    height=600,
    width=1200,
    drawing_mode=drawing_mode,
    key="canvas",
)

# Save drawing
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data, caption="Your Drawing", use_column_width=True)
    img = Image.fromarray(canvas_result.image_data.astype("uint8"))

    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()
    b64 = base64.b64encode(img_bytes).decode()

    href = f'<a href="data:file/png;base64,{b64}" download="drawing.png">📥 Download Drawing</a>'
    st.markdown(href, unsafe_allow_html=True)
