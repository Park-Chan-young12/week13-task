import io
import streamlit as st
from rembg import remove
from PIL import Image

# ---------- 강제 다크모드 CSS ----------
DARK_MODE_CSS = """
<style>
/* 전체 배경 */
body, .main, .block-container {
    background-color: #1a1b1e !important;
    color: #e6e6e6 !important;
}

/* 파일 업로드 영역 */
.stFileUploader {
    background-color: #2a2b2e !important;
    border-radius: 12px !important;
    padding: 15px !important;
}

/* 텍스트 색 */
h1, h2, h3, h4, h5, h6, p, label, span, .stTextInput>div>div>input {
    color: #e6e6e6 !important;
}

/* 입력창 배경 */
input[type="text"],
textarea,
.stTextInput>div>div>input {
    background-color: #2a2b2e !important;
    color: #e6e6e6 !important;
    border-radius: 8px;
}

/* 버튼 스타일 */
.stButton button {
    background: linear-gradient(90deg, #4b79cf, #3552a1);
    color: white !important;
    border-radius: 10px;
    padding: 10px 26px;
    border: none;
    font-size: 16px;
    font-weight: 600;
}
.stButton button:hover {
    opacity: 0.9;
}

/* 카드 느낌의 박스 */
.dark-card {
    background-color: #2a2b2e;
    padding: 25px;
    border-radius: 14px;
    box-shadow: 0px 0px 12px rgba(0,0,0,0.4);
}

/* 다운로드 버튼 */
.stDownloadButton button {
    background: #444 !important;
    color: #fff !important;
    border-radius: 10px !important;
    border: 1px solid #666 !important;
}
.stDownloadButton button:hover {
    background: #555 !important;
}
</style>
"""

def main():
    st.set_page_config(
        page_title="Dark Mode Background Remover",
        page_icon="🌙",
        layout="centered"
    )

    # CSS 적용
    st.markdown(DARK_MODE_CSS, unsafe_allow_html=True)

    # 제목
    st.markdown(
        "<h1 style='text-align:center; font-size:40px;'>🌙 Dark Mode Background Remover</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align:center; color:#bbbbbb;'>이미지를 업로드하면 배경을 자동 제거하여 투명 PNG로 변환합니다.</p>",
        unsafe_allow_html=True
    )

    # 업로드 카드
    st.markdown("<div class='dark-card'>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "이미지를 업로드하세요 (PNG / JPG / JPEG)",
        type=["png", "jpg", "jpeg"]
    )
    st.markdown("</div>", unsafe_allow_html=True)

    if uploaded_file is not None:
        input_image = Image.open(uploaded_file).convert("RGBA")

        st.markdown("<h3 style='margin-top:20px;'>📌 원본 이미지</h3>", unsafe_allow_html=True)
        st.image(input_image, use_column_width=True)

        if st.button("✨ 배경 제거하기"):
            with st.spinner("배경 제거 중입니다…"):
                output_image = remove(input_image)

            st.markdown("<h3 style='margin-top:25px;'>🎉 배경 제거 결과</h3>", unsafe_allow_html=True)
            st.image(output_image, use_column_width=True)

            buffer = io.BytesIO()
            output_image.save(buffer, format="PNG")
            img_bytes = buffer.getvalue()

            st.download_button(
                "📥 투명 PNG 다운로드",
                data=img_bytes,
                file_name="removed_background.png",
                mime="image/png"
            )

            st.info("결과물은 PPT / 문서 / 썸네일 제작에 최적화된 **투명 배경 PNG**입니다.")


if __name__ == "__main__":
    main()
