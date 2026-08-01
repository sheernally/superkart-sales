# SuperKart Sales Prediction — Free-Tier Deployment (Render + Streamlit Cloud)

No paid plan required anywhere in this path. Total time: ~15 minutes, mostly waiting on
build logs.

## 0. Revoke the old Hugging Face token first
If you haven't already: https://huggingface.co/settings/tokens → revoke `SheernallyProjectToken`.
It was pasted into a chat transcript and should not be trusted anymore, regardless of
whether you still use Hugging Face for anything else.

## 1. Push this folder to a new GitHub repo
```bash
cd superkart-deploy
git init
git add .
git commit -m "SuperKart sales prediction - backend + frontend"
git branch -M main
git remote add origin https://github.com/<your-username>/superkart-sales.git
git push -u origin main
```
(Create the empty repo first at https://github.com/new — public or private both work for
Render/Streamlit Cloud's free tiers.)

## 2. Deploy the backend on Render (free Web Service)
1. Go to https://render.com → sign up/log in with GitHub (no card needed for free tier).
2. **New +** → **Web Service** → connect your `superkart-sales` repo.
3. Settings:
   - **Root Directory:** `backend`
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn -w 4 -b 0.0.0.0:$PORT app:superkart_api`
   - **Instance Type:** Free
4. Click **Create Web Service**. Wait for the build to finish (a few minutes).
5. Copy the URL Render gives you, e.g. `https://superkart-sales-backend.onrender.com`.
6. Sanity check: visit `https://<your-render-url>/` in a browser — you should see
   "Welcome to the SuperKart Sales Prediction API!"

**Free tier caveat:** the service spins down after ~15 minutes of no traffic and takes
30–50 seconds to wake up on the next request. That's expected — not a bug.

## 3. Deploy the frontend on Streamlit Community Cloud (free)
1. Go to https://share.streamlit.io → sign in with GitHub.
2. **New app** → pick the `superkart-sales` repo, branch `main`.
3. **Main file path:** `frontend/app.py`
4. Click **Deploy**. Wait for the build.
5. Once it's live, open the app, expand the sidebar, and paste your real Render URL +
   `/v1/predict` into the "API URL" field — e.g.
   `https://superkart-sales-backend.onrender.com/v1/predict`
   (Better: edit `BACKEND_URL` in `frontend/app.py` directly and push, so it's correct
   by default and you don't have to set it every visit.)

## 4. What to submit
Once both are live, send me the two URLs:
- Backend (Render): `https://....onrender.com`
- Frontend (Streamlit Cloud): `https://....streamlit.app`

I'll drop them into the notebook's deployment section and the PPTX's Deployment slide,
and give you the final files.
