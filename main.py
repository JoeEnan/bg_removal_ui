from io import BytesIO

import numpy as np
import streamlit as st
from PIL import Image

from src.rmbg.remove_bg import RemoveBG
from src.utils.img_utils import convert_alpha_to_white, reduce_image_size

remove_bg_model = RemoveBG()


def remove_background(image: Image.Image) -> Image.Image:
    return Image.fromarray(remove_bg_model.gen_image(np.array(image)), "RGBA")


def main():
    st.title("Background Removal App")

    uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        # Open uploaded file as a PIL image
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image", use_container_width=True)

        # Always remove background by default
        st.write("Removing background...")
        processed_image = remove_background(image)

        # Two additional processing options
        reduce_size = st.checkbox("Reduce Image Size")
        convert_alpha = st.checkbox("Convert Alpha Values to White")

        if convert_alpha:
            processed_image = convert_alpha_to_white(processed_image)

        if reduce_size:
            quality = st.slider(
                "Select image quality", min_value=10, max_value=100, value=100
            )
            processed_image = reduce_image_size(
                processed_image, quality=quality
            )

        st.image(processed_image, caption="Processed Image", use_container_width=True)

        # Provide a download button for the processed image
        buf = BytesIO()
        processed_image.save(buf, format="PNG")
        byte_im = buf.getvalue()
        st.download_button(
            "Download Processed Image",
            data=byte_im,
            file_name="processed.png",
            mime="image/png",
        )


if __name__ == "__main__":
    main()
