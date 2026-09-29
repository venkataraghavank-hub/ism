"""One Streamlit app for all 20 Information Systems Management sessions."""
from __future__ import annotations

import hmac
import html
import os

import streamlit as st

from sessions.session_01 import render_session_01

st.set_page_config(page_title="ISM | Manager's Lab", page_icon="🧭", layout="wide", initial_sidebar_state="expanded")

SESSION_NAMES = [
    "The manager's IT problem", "Session 02", "Session 03", "Session 04", "Session 05",
    "Session 06", "Session 07", "Session 08", "Session 09", "Session 10",
    "Session 11", "Session 12", "Session 13", "Session 14", "Session 15",
    "Session 16", "Session 17", "Session 18", "Session 19", "Session 20",
]

CSS = """
<style>
:root{--navy:#082b61;--blue:#2670b8;--teal:#13a4aa;--ink:#17324d;--muted:#647f9d;--line:#dbe7f3}
.stApp{background:#f3f9ff;color:var(--ink)}
.block-container{max-width:1250px;padding:1.25rem 2.1rem 3rem}
header[data-testid="stHeader"]{background:transparent}#MainMenu,footer{visibility:hidden}
[data-testid="stSidebar"]{background:var(--navy)}
[data-testid="stSidebar"] *{color:#eef7ff}
[data-testid="stSidebar"] .stButton button{border:1px solid rgba(255,255,255,.16);background:rgba(255,255,255,.07);border-radius:10px;text-align:left;justify-content:flex-start;min-height:2.5rem}
[data-testid="stSidebar"] .stButton button:hover{background:#14508f;border-color:#57b7c4}
[data-testid="stSidebar"] .stButton button[kind="primary"]{background:#13a4aa;color:#fff;border-color:#13a4aa}
[data-testid="stSidebar"] .stButton button p{font-size:.86rem}
.hero{padding:.15rem .1rem 1rem}.eyebrow{font-size:.78rem;font-weight:800;letter-spacing:.13em;color:var(--blue)}
.hero h1{font-size:clamp(2rem,3vw,2.8rem);line-height:1.06;color:var(--navy);letter-spacing:-.035em;margin:.4rem 0}
.hero p{font-size:1.06rem;color:#587596;max-width:900px;margin:.15rem 0}
.notice{padding:.85rem 1rem;border-left:4px solid var(--teal);border-radius:9px;background:#eaf7f9;color:#365d82;margin:.2rem 0 1.2rem}
.access{text-align:center}.access h1{color:var(--navy);margin:.4rem 0}.access p{color:#587596}
[data-testid="stVerticalBlockBorderWrapper"]{background:#fff;border:1px solid #dce8f4!important;border-radius:18px!important;box-shadow:0 10px 30px rgba(18,59,112,.07)}
.stage{font-size:.77rem;font-weight:800;letter-spacing:.12em;color:#137f89;text-transform:uppercase}
.prompt{font-size:1.45rem;line-height:1.28;font-weight:750;color:var(--navy);margin:.4rem 0 1rem}
.case{padding:1rem 1.15rem;border-radius:12px;background:#edf5fe;border:1px solid #d6e7f6;color:#274f74;margin-bottom:1rem}
.debrief{padding:1rem 1.15rem;border-radius:12px;background:#eaf9f8;border-left:4px solid var(--teal);color:#215360;margin:.7rem 0 1rem}
.compact{color:#62819d;font-size:.9rem}.section{color:var(--navy);font-weight:800;font-size:1.16rem}
div.stButton>button[kind="primary"]{background:var(--teal);border:0;border-radius:10px;min-height:2.8rem;font-weight:700}
div.stButton>button[kind="primary"]:hover{background:#0b9299;border:0}
.stRadio label{line-height:1.35}
@media(max-width:800px){.block-container{padding:1rem}}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


def expected_code() -> str:
    try:
        configured = st.secrets.get("STUDENT_ACCESS_CODE", "") or st.secrets.get("APP_ACCESS_CODE", "")
    except Exception:
        configured = ""
    return str(configured or os.getenv("STUDENT_ACCESS_CODE", "") or os.getenv("APP_ACCESS_CODE", ""))


def require_access() -> None:
    if st.session_state.get("ism_access_granted"):
        return
    _, center, _ = st.columns([1, 1.25, 1])
    with center, st.container(border=True):
        st.markdown('<div class="access"><div class="eyebrow">INFORMATION SYSTEMS MANAGEMENT</div><h1>Manager’s Lab</h1><p>Enter the course access code to begin.</p></div>', unsafe_allow_html=True)
        entered = st.text_input("Course access code", type="password")
        if st.button("Enter the course", type="primary", use_container_width=True):
            code = expected_code()
            if code and hmac.compare_digest(entered, code):
                st.session_state.ism_access_granted = True
                st.rerun()
            st.error("Incorrect code. Please try again.")
        if not expected_code():
            st.warning("The course owner has not configured an access code yet.")
    st.stop()


require_access()
st.session_state.setdefault("ism_session", 1)
with st.sidebar:
    st.markdown("### ISM · Manager's Lab")
    st.caption("20 sessions · one course app")
    st.markdown("---")
    for number, name in enumerate(SESSION_NAMES, 1):
        label = f"{number:02d}  {name}" if number == 1 else f"{number:02d}  {name}  ·  Soon"
        if st.button(label, key=f"nav_{number}", type="primary" if st.session_state.ism_session == number else "secondary", use_container_width=True):
            st.session_state.ism_session = number
            st.rerun()
    st.markdown("---")
    if st.button("Exit course", use_container_width=True):
        st.session_state.clear()
        st.rerun()

number = st.session_state.ism_session
if number == 1:
    render_session_01()
else:
    st.markdown(f'<div class="hero"><div class="eyebrow">SESSION {number:02d}</div><h1>{html.escape(SESSION_NAMES[number-1])}</h1><p>This session’s interactive tutorial will be added here.</p></div>', unsafe_allow_html=True)
    st.info("The course app keeps one repository and one Streamlit URL as new sessions are added.")
    if st.button("Go to Session 01", type="primary"):
        st.session_state.ism_session = 1
        st.rerun()
