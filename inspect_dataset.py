import pandas as pd
import os

dataset_folder = "dataset"

# List all csv files
csv_files = [file for file in os.listdir(dataset_folder) if file.endswith(".csv")]

print("CSV Files Found:\n")

for file in csv_files:

    print("=" * 50)
    print(f"FILE: {file}")

    path = os.path.join(dataset_folder, file)

    try:
        df = pd.read_csv(path)

        # Show columns
        print("\nColumns:")
        print(df.columns.tolist())

        # Show dataset shape
        print("\nShape:")
        print(df.shape)

        # Show missing values
        print("\nMissing Values:")
        print(df.isnull().sum())

        # Show first 3 rows
        print("\nFirst 3 Rows:")
        print(df.head(3))

        # Show label distribution if label column exists
        possible_label_columns = ['label', 'Label', 'class', 'Class', 'target']

        found_label = False

        for col in possible_label_columns:
            if col in df.columns:

                print(f"\nLabel Distribution ({col}):")
                print(df[col].value_counts())

                found_label = True
                break

        if not found_label:
            print("\nNo label column detected.")

    except Exception as e:
        print(f"Error reading {file}: {e}")