# Streamlit Community Cloud에 올리는 파일

이 폴더 내용만 GitHub 저장소 **루트**로 푸시합니다.  
예: https://github.com/sk31park/streamlit-test

API와 Ollama는 이 저장소에 없습니다. 수업 PC에서 실행합니다.

| Community Cloud 항목 | 값 |
|----------------------|-----|
| Main file path | `streamlit_app.py` |
| Secrets | `API_URL = "https://xxxx.trycloudflare.com"` |

로컬에서 보려면 `week9-cloud-deploy` 폴더에서 다음을 실행합니다.

```powershell
python -m streamlit run streamlit-cloud/streamlit_app.py
```
