# Titanic Dataset Analysis 🛳️

This Jupyter Notebook performs exploratory data analysis (EDA) on the Titanic dataset using Python and the Pandas library. The goal is to understand patterns and insights from the passenger data aboard the Titanic.

## 📂 Dataset

The dataset used is `Titanic-Dataset.csv`, which includes information such as:
- Passenger class
- Name
- Sex
- Age
- Survival status
- Fare
- Cabin and Embarked port

## 🛠️ Tools & Libraries

The following Python libraries are used in this notebook:

- `pandas` — for data manipulation and analysis
- `matplotlib` / `seaborn` — (if used) for visualization

## 🧮 Steps Performed

1. **Data Loading**  
   Loaded Titanic data using `pandas.read_csv`.

2. **Initial Exploration**  
   - Displayed first few rows
   - Checked for missing values

3. **Data Cleaning**  
   - Handled null values
   - Converted data types (if required)

4. **Data Visualization** *(Optional)*  
   - Plotted survival rate by gender, class, etc.

## 📊 Sample Output

```python
 First 5 Rows:
   PassengerId  Survived  Pclass  ...  Fare  Cabin  Embarked
0            1         0       3  ...  7.25   NaN        S
...
```

## 📎 Requirements

To run this notebook, install the following (using pip or conda):

```bash
pip install pandas matplotlib seaborn
```

## ✅ How to Run

1. Clone the repository
2. Make sure `Titanic-Dataset.csv` is in the same directory as the notebook
3. Open the `.ipynb` file with Jupyter Lab or Jupyter Notebook
4. Run the cells

---

📌 **Note:** This is a beginner-friendly project to learn data exploration techniques using Python.
