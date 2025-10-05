Streamlit Cloud Deployment

1. Push the repository to GitHub.
2. On Streamlit Cloud, click "New app" and connect the repo and branch.
3. Set the `GEMINI_API_KEY` secret in the app settings.
4. Deploy. The app will run the `streamlit run app.py` command by default.

Notes
- Use the latest Python runtime available in Streamlit Cloud.
- For heavy usage, consider switching to a paid plan or deploying to a VM/container.
