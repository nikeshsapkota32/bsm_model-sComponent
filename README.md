Black-Scholes-Merton Option Pricing Model
Overview
This project is an interactive web application built with Streamlit that calculates the theoretical price of European-style call and put options using the Black-Scholes-Merton (BSM) model. It provides an intuitive interface for users to adjust key financial parameters and instantly see the impact on option prices and risk sensitivities, also known as The Greeks.

🚀 Features
Real-time Pricing: Calculates call and put option prices based on user-defined inputs.

The Greeks: Displays key risk sensitivities including Delta, Gamma, Theta, Vega, and Rho.

Interactive Visualization: Includes a live plot that shows how option prices change with the underlying stock price.

User-Friendly Interface: Built with Streamlit, making it easy to use without any financial or coding knowledge.

📈 The Black-Scholes-Merton Model
The BSM model is a widely-used mathematical model for pricing options. It relies on five main inputs:

S: Current Stock Price

K: Option Strike Price

T: Time to Expiration (in years)

r: Risk-Free Interest Rate

σ: Volatility of the Underlying Asset

🛠️ How to Run the Project
Prerequisites
You need Python 3.7+ installed on your system. It's highly recommended to use a virtual environment.

Installation
Clone the Repository:

Bash

git clone https://github.com/nikeshsapkota32/bsm_model-sComponent.git
cd bsm_model-sComponent
Create and Activate a Virtual Environment:

Bash

# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
Install Required Libraries:

Bash

pip install -r requirements.txt
Running the Application
Once the dependencies are installed, you can run the Streamlit application from your terminal:

Bash

streamlit run app.py
The application will automatically open in your web browser.

🌐 Live Application
You can access the live, hosted version of this application here:

[Link to your Streamlit Community Cloud URL]

👨‍💻 Author
Nikesh Sapkota

GitHub: https://github.com/nikeshsapkota32

LinkedIn: [Link to your LinkedIn profile]
(Consider adding other links like your personal website or portfolio)

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
