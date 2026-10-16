# NAVTTC AI/ML/Deep Learning - Course Tasks

Solutions to the practical tasks of the NAVTTC AI/ML/Deep Learning course, one file per task, in the same order as the course outline (Annexure-I).

**Status:** Tasks 1 to 52 completed.

## Contents

- [Setup](#setup)
- [Python basics (Tasks 3-19)](#python-basics-tasks-3-19)
- [Functions, data types and exceptions (Tasks 20-27)](#functions-data-types-and-exceptions-tasks-20-27)
- [NumPy (Tasks 28-40)](#numpy-tasks-28-40)
- [Pandas (Tasks 41-48)](#pandas-tasks-41-48)
- [Statistics (Tasks 49-50)](#statistics-tasks-49-50)
- [Machine learning (Tasks 51-52)](#machine-learning-tasks-51-52)
- [How to run](#how-to-run)

## Setup

| Task | File | Topic |
|---|---|---|
| 1 | task_01_installation.md | Anaconda, PyTorch, TensorFlow, Git Bash, VS Code and PyCharm installation |
| 2 | task_02_linux_commands.md | Linux commands practised in Git Bash |

## Python basics (Tasks 3-19)

| Task | File | Topic |
|---|---|---|
| 3 | task_03_add_two_numbers.py | Add two numbers |
| 4 | task_04_add_numbers_from_user.py | Add two numbers taken from the user |
| 5 | task_05_square_root.py | Square root of a number |
| 6 | task_06_complex_square_root.py | Square root of a complex number |
| 7 | task_07_celsius_to_fahrenheit.py | Celsius to Fahrenheit |
| 8 | task_08_area_of_triangle.py | Area of a triangle |
| 9 | task_09_quadratic_equation.py | Solve a quadratic equation |
| 10 | task_10_kilometers_to_miles.py | Kilometers to miles |
| 11 | task_11_if_statement.py | if statement |
| 12 | task_12_if_else.py | if-else statement |
| 13 | task_13_nested_if.py | Nested if |
| 14 | task_14_if_elif_else.py | if-elif-else ladder |
| 15 | task_15_for_loops.py | for loops |
| 16 | task_16_while_loops.py | while loops |
| 17 | task_17_break_statement.py | break statement |
| 18 | task_18_continue_statement.py | continue statement |
| 19 | task_19_looping_techniques.py | enumerate, zip, items, reversed, sorted |

## Functions, data types and exceptions (Tasks 20-27)

| Task | File | Topic |
|---|---|---|
| 20 | task_20_user_defined_function.py | User defined functions |
| 21 | task_21_list_data_type_in_python.py | List |
| 22 | task_22_tuple_data_type_in_python.py | Tuple |
| 23 | task_23_string_data_type_in_python.py | String |
| 24 | task_24_set_data_type_in_python.py | Set |
| 25 | task_25_dictionary_data_type_in_python.py | Dictionary |
| 26 | task_26_exception_handling.py | Exception handling |
| 27 | task_27_user_defined_exception_handling_in_python.py | User defined exceptions |

## NumPy (Tasks 28-40)

| Task | File | Topic |
|---|---|---|
| 28 | task_28_numpy_create_array.py | Creating arrays |
| 29 | task_29_numpy_array_indexing.py | Array indexing |
| 30 | task_30_array_slicing.py | Array slicing |
| 31 | task_31_numpy_data_types.py | Data types |
| 32 | task_32_numpy_array_copy_vs_view.py | Copy vs view |
| 33 | task_33_numpy_array_shape.py | Array shape |
| 34 | task_34_numpy_array_reshaping.py | Reshaping arrays |
| 35 | task_35_numpy_array_iterating.py | Iterating arrays |
| 36 | task_36_numpy_joining_array.py | Joining arrays |
| 37 | task_37_numpy_splitting_array.py | Splitting arrays |
| 38 | task_38_numpy_searching_arrays.py | Searching arrays |
| 39 | task_39_numpy_sorting_arrays.py | Sorting arrays |
| 40 | task_40_random_numbers_in_numpy.py | Random numbers |

## Pandas (Tasks 41-48)

| Task | File | Topic |
|---|---|---|
| 41 | task_41_pandas_basics.py | Pandas basics |
| 42 | task_42_installation_of_pandas.py | Installing Pandas |
| 43 | task_43_pandas_series.py | Series |
| 44 | task_44_pandas_dataframes.py | DataFrames |
| 45 | task_45_pandas_read_csv.py | Reading CSV files |
| 46 | task_46_(data_analysis).py | Analysing data |
| 47 | task_47_pandas_cleaning_data.py | Cleaning data (empty cells, wrong format, wrong data, duplicates) |
| 48 | task_48_pandas_correlations.py | Correlations |

## Statistics (Tasks 49-50)

| Task | File | Topic |
|---|---|---|
| 49 | task_49_mean_median_mode.py | Mean, median and mode |
| 50 | task_50_standard_deviation.py | Standard deviation |

## Machine learning (Tasks 51-52)

| Task | File | Topic |
|---|---|---|
| 51 | task_51_implement_linear_reression.py | Linear regression with scikit-learn |
| 52 (part 1) | task_52_part_1_five_regression_modules.py | Five regression modules: NumPy, SciPy, statsmodels, scikit-learn, Seaborn |
| 52 (part 2) | task_52_part_2_logistic_regression.py | Logistic regression (Pima Indians Diabetes dataset) |

## How to run

Install the libraries used by Tasks 20-52:

```
pip install numpy pandas scipy matplotlib seaborn scikit-learn statsmodels
```

Run any task:

```
python task_03_add_two_numbers.py
```

Notes:

- Tasks 45-48 read a CSV file. Keep that file in the same folder as the script.
- Tasks 51-52 load their dataset from the internet; the scripts include a built-in fallback if the download fails.
- Several files were exported from Google Colab notebooks, so a few lines (such as `display(...)`) work best when run in Jupyter or Colab.
- TensorFlow runs in a separate Python 3.11 environment (see Task 1).
