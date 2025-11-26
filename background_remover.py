import io
import streamlit as st
from rembg import remove
from PIL import Image

# ---------- 스타일(CSS) ----------
CUSTOM_CSS = """
<style>
/* 전체 배경 */
.main {
    background-color: #f7f7f9;
}

/* 중앙 카드 스타일 */
.upload-card {
    background: white;
    padding: 30px 35px;
    border-radius: 18px;
    box-shadow: 0px 4px 16px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

/* 제목 */
.title-text {
    text-align: center;
    font-size: 38px !important;
    color: #333;
    font-weight: 700;
    margin-bottom: 5px;
}

/* 설명 텍스트 */
.sub-text {
    text-align: center;
    font-size: 16px;
    color: #666;
    margin-bottom: 25px;
}

/* 버튼 스타일 */
.stButton button {
    background: linear-gradient(90deg, #6a11cb, #2575fc);
    color: white !important;
    padding: 12px 28px;
    border-radius: 12px;
    border: none;
    font-size: 16px;
    font-weight: 600;
}
.stButton button:hover {
    opacity: 0.92;
}

/* 이미지 구역 */
.section-title {
    font-size: 20px;
    font-weight: 700;
    color: #333;
    margin-bottom: 10px;
}

</style>
"""

# ---------- 메인 코드 ----------
def main():
    st.set_page_config(
        page_title="Image Background Remover",
        page_icon="🪄",
        layout="centered"
    )

    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

    # ---------- 제목 및 설명 ----------
    st.markdown("<h1 class='title-text'>🪄 Image Background Remover</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p class='sub-text'>이미지를 업로드하면 <b>배경이 자동 제거</b>됩니다.<br>"
        "투명 배경 PNG 파일로 바로 다운로드하세요.</p>",
        unsafe_allow_html=True
    )

    # ---------- 업로드 카드 ----------
    with st.container():
        st.markdown("<div class='upload-card'>", unsafe_allow_html=True)

        uploaded_file = st.file_uploader(
            "이미지를 업로드하세요 (PNG / JPG / JPEG)",
            type=["png", "jpg", "jpeg"]
        )

        st.markdown("</div>", unsafe_allow_html=True)

    # ---------- 이미지 처리 ----------
    if uploaded_file is not None:

        input_image = Image.open(uploaded_file).convert("RGBA")

        st.markdown("<p class='section-title'>📌 원본 이미지</p>", unsafe_allow_html=True)
        st.image(input_image, use_column_width=True)

        if st.button("✨ 배경 제거하기"):
            with st.spinner("배경 제거 중입니다… ⏳"):
                output_image = remove(input_image)

            st.markdown("<p class='section-title'>🎉 배경 제거 결과</p>", unsafe_allow_html=True)
            st.image(output_image, use_column_width=True)

            buf = io.BytesIO()
            output_image.save(buf, format="PNG")
            byte_im = buf.getvalue()

            st.download_button(
                label="📥 투명 PNG 다운로드",
                data=byte_im,
                file_name="output_no_bg.png",
                mime="image/png"
            )

            st.info("결과물은 **완전한 투명 배경 PNG**로 저장됩니다. PPT·문서·썸네일 제작에 최적화되어 있습니다.")


if __name__ == "__main__":
    main()
