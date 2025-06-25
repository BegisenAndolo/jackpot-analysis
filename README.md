
## 📊 Current Project Status: Excel + Python Integration

### 🔁 Monte Carlo Simulation (Excel VBA)

We are currently using **Excel VBA** to simulate football match outcomes using a Monte Carlo engine. Each simulation involves:

* **17-match slip generation** based on blended probabilities
* **5 predictive models**: Historical, Odds, H2H, Form, and Venue
* **Random weight assignment** per simulation using a **Dirichlet distribution**, ensuring all 5 weights sum to 1
* 1000 simulations logged per run in the `Simulations_Log` sheet
* Each simulation logs:

  * The outcomes for all 17 matches
  * The weights used to blend the model probabilities
* A recommended slip is selected based on predefined logic, and its accuracy is tracked week to week

### 📈 Statistical Analysis (Python)

We have begun analyzing the results of the Excel simulation using **Python**, focusing on:

* Importing simulation results (`.csv` file)
* Cleaning and inspecting the data
* Performing **correlation analysis** between the weights used and the number of correct picks per simulation
* Identifying which weight combinations (e.g., high Venue weight) correlate with better accuracy

### 🔬 Current Experiment

* We replaced uniform random weights with **Dirichlet-generated weights** to maintain a natural and statistically correct blend.
* The impact is being tracked over the next 4 weeks by comparing:

  * Highest number of correct picks
  * Average performance of the top slip
  * Spread of weight profiles in successful slips

---

### 🗂 Folder Structure (Work in Progress)

```
football-predictor-webdata/
│
├── data/
│   └── simulation_results.csv      # Exported from Excel for analysis
│
├── scripts/
│   └── correlation_analysis.py     # Python file for weight-performance analysis
│
├── README.md                       # This file (project overview)
└── ...
