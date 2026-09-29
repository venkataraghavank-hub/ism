# ISM · Manager's Lab

A single Streamlit app and GitHub repository for 20 Information Systems Management sessions. Session 01 is a decision-led Vandelay tutorial. Sessions 02–20 are visible placeholders for future tutorials and simulations.

## Deploy to Streamlit Community Cloud

1. Create **one private GitHub repository**, for example `ism-managers-lab`. Upload the *contents* of this folder to the repository root, including `.streamlit/config.toml` and the `sessions` folder. Do not upload a real `secrets.toml`.
2. In Streamlit Community Cloud, create an app from that repository. Set the main file to `streamlit_app.py` and choose your branch.
3. In the app’s **Settings → Secrets**, enter a new code:

   ```toml
   STUDENT_ACCESS_CODE = "choose-a-new-private-code"
   ```

   Save and reboot the app if prompted. Share the code privately with students. The example file is a template only.
4. Open the Streamlit URL, enter the code and run through Session 01. Add this URL as the ISM card on your existing website when ready.

The code is checked against a private Streamlit secret, rather than placed in the GitHub source. This is a shared classroom gate, not individual identity or strong user authentication. No names, email addresses, scores or responses are saved by the app. Decisions remain in each browser’s Streamlit session and disappear when the session ends or **Exit course** is used. Avoid sharing the access code publicly; change it in Secrets when needed.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# Edit .streamlit/secrets.toml to set your private local code.
streamlit run streamlit_app.py
```

## Extend the same app

Add `sessions/session_02.py` with a `render_session_02()` function, import it in `streamlit_app.py`, replace Session 02's sidebar title, and route `number == 2` to that function. Repeat for subsequent sessions. Commit and push to the same repository; Streamlit redeploys the same app URL. Keep the shared sidebar, theme and access gate in `streamlit_app.py`.

## Session 01 teaching design

Students advise Chris Burns through six decisions: Red Queen and business value; information systems beyond the ERP licence; Tiwana's portfolio; McAfee's function/network/enterprise IT; matching complements; and CCR responsibility. They can switch choices to compare implications. The final page shows their configuration and a brief debrief, without marks.

**Course readings:** Amrit Tiwana, *IT Strategy for Non-IT Managers*, introductory chapter; Andrew McAfee, *Mastering the Three Worlds of Information Technology*; *A Conversation About Information Technology* (2004 and course 2026 edition); Session 1 deck. The app paraphrases rather than redistributes the readings.
