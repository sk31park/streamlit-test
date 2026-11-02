"""실습 5 — Streamlit Community Cloud에 올리는 화면.

이 폴더만 GitHub 저장소 루트로 푸시한다.
Ollama는 이 화면 서버에 없다. 질문은 API_URL 의 /chat 으로 보내고,
그 API가 떠 있는 PC의 Ollama가 답을 만든다.
"""

from __future__ import annotations

import os

import httpx
import streamlit as st


def default_api_url() -> str:
    url = os.getenv("API_URL", "").strip()
    if url:
        return url
    try:
        secret = str(st.secrets.get("API_URL", "")).strip()
    except Exception:
        secret = ""
    if secret:
        return secret
    return "http://127.0.0.1:8000"


def main() -> None:
    st.set_page_config(page_title="Week9 API 화면")
    st.title("Week9 API 화면")
    st.caption("이 화면에는 모델이 없습니다. Ollama는 API가 켜진 PC에서만 동작합니다.")

    api_url = st.text_input("API 주소", value=default_api_url()).strip().rstrip("/")
    if "streamlit.app" in api_url or api_url.endswith(":8501"):
        st.warning("API 주소는 FastAPI입니다. Streamlit 주소를 넣지 마세요.")

    if st.button("연결 확인"):
        try:
            response = httpx.get(f"{api_url}/health", timeout=20.0)
            st.write(response.status_code, response.json())
        except httpx.HTTPError as exc:
            st.error(f"API에 연결하지 못했습니다. Tunnel 주소인지 확인하세요. ({exc.__class__.__name__})")

    message = st.chat_input("질문")
    if message:
        try:
            response = httpx.post(
                f"{api_url}/chat",
                json={"message": message},
                timeout=120.0,
            )
            response.raise_for_status()
            body = response.json()
        except httpx.HTTPError as exc:
            st.error(f"질문을 보내지 못했습니다. ({exc.__class__.__name__})")
            return
        error = str(body.get("error") or "").strip()
        if error:
            st.error(error)
        else:
            st.write(body.get("reply", ""))


if __name__ == "__main__":
    main()
