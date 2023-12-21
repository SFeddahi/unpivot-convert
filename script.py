import pandas as pd

def read_excel_files(source_path, target_path):
    # Read the source Excel file
    source_df = pd.read_excel(source_path)
    
    # Read each sheet in the target Excel file into a dictionary of dataframes
    target_dfs = pd.read_excel(target_path, sheet_name=None)
    
    return source_df, target_dfs

def update_target(target_dfs, source_df):
    for _, row in source_df.iterrows():
        catalog_number = row["CATALOG_NO"]
        category = row["Category"]
        feature_name = row["Feature name"]
        existing_value = row["Existing value"] # these existing and enriched values are optional in case of data enriched unpivoted tables
        enriched_value = row["Enriched value"]

        if category in target_dfs:
            category_df = target_dfs[category]
            matched_column = next(
                (col.lower() for col in category_df.columns if col.lower() == feature_name.lower()), None
            )

            if matched_column:
                value_to_update = existing_value if pd.notna(existing_value) else enriched_value
                if pd.notna(value_to_update):
                    row_index = category_df[category_df["CATALOG_NO"] == catalog_number].index
                    if not row_index.empty:
                        if not pd.api.types.is_string_dtype(category_df[matched_column]):
                            category_df[matched_column] = category_df[matched_column].astype(str)
                        target_dfs[category].at[row_index[0], matched_column] = str(value_to_update) if pd.notna(value_to_update) else ""
        else:
            print(f"Category '{category}' not found in Target.")

    return target_dfs

def save_updated_excel(target_dfs, output_path):
    # Create Excel writer
    writer = pd.ExcelWriter(output_path, engine="xlsxwriter")
    
    # Write each dataframe to a different sheet
    for sheet_name, df in target_dfs.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)
    
    # Save the Excel file
    writer.save()

def main(source_path, target_path, output_path):
    # Read input files
    source_df, target_dfs = read_excel_files(source_path, target_path)
    
    # Update target dataframes based on source data
    updated_target_dfs = update_target(target_dfs, source_df)
    
    # Save the updated data to an output Excel file
    save_updated_excel(updated_target_dfs, output_path)

# Example usage
# main('path_to_Source.xlsx', 'path_to_Target.xlsx', 'path_to_output_file.xlsx')
