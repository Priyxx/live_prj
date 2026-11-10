# RentSplit — Flat Expense Calculator

A free, responsive Flask demo website based on the original `rent_sys.py` calculation.

## Calculation
- Electricity cost = electricity units × charge per unit
- Total expenses = rent + food + electricity cost
- Per-person amount = total expenses // number of people

The final calculation intentionally preserves the original Python program's integer floor-division (`//`) behaviour.

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Create and activate a virtual environment (optional but recommended).
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the website:

   ```bash
   python app.py
   ```

6. Open http://127.0.0.1:5000

## Deploy free on Render
1. Push this project folder to a GitHub repository.
2. In Render, choose **New → Web Service** and connect the repository.
3. Choose the **Free** instance.
4. Set:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
5. Deploy. Render provides a free `onrender.com` URL.
https://live-prj.onrender.com
Note: Render free web services may spin down after inactivity, so the first request after a quiet period can take longer.

## Notes
- No database or account is needed for this calculator demo.
- Calculations are performed when the form is submitted and are not stored.
- The app validates that the number of people is greater than zero.
