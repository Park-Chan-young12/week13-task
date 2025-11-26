import io
import streamlit as st
from rembg import remove
from PIL import Image


# ---- 최소 다크 스타일 적용 ----
DARK_CSS = """
<style>
body, .main, .block-container {
    background-color: #222 !important;
    color: #eee !important;
}

/* 파일 업로드 박스 배경만 살짝 진하게 */
.stFileUploader {
    background-color: #333 !important;
    padding: 12px !important;
    border-radius: 8px !important;
}

/* 버튼만 약간 어둡게 */
.stButton button {
    background-color: #444 !important;
    color: #fff !important;
    border-radius: 6px;
    border: 1px solid #555;
}
.stButton button:hover {
    background-color: #555 !important;
}
</style>
"""


def main():
    st.set_page_config(
        page_title="Image Background Remover",
        page_icon="🪄",
        layout="centered"
    )

    st.markdown(DARK_CSS, unsafe_allow_html=True)

    st.title("🪄 Image Background Remover")
    st.write("이미지를 업로드하면 **배경을 자동으로 제거**합니다.")

    uploaded_file = st.file_uploader(
        "이미지를 업로드하세요 (PNG / JPG / JPEG)",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:
        input_image = Image.open(uploaded_file).convert("RGBA")

        st.subheader("📌 원본 이미지")
        st.image(input_image, use_column_width=True)

        if st.button("✨ 배경 제거하기"):
            with st.spinner("배경 제거 중입니다..."):
                output_image = remove(input_image)

            st.subheader("🎉 배경 제거 결과")
            st.image(output_image, use_column_width=True)

            buf = io.BytesIO()
            output_image.save(buf, format="PNG")
            byte_im = buf.getvalue()

            st.download_button(
                label="📥 PNG 다운로드",
                data=byte_im,
                file_name="output_no_bg.png",
                mime="image/png"
            )


if __name__ == "__main__":
    main()
