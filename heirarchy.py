import pandas as pd

# Assuming the data is loaded into a DataFrame
employees_df = pd.read_csv('all_employee.csv')

# Function to build the managerial chain
def get_manager_chain(employee_id, employees_df):
    chain = []
    current_employee = employee_id
    
    while not pd.isnull(current_employee):
        # Get the manager row for the current employee
        manager_row = employees_df.loc[employees_df['Employee_id'] == current_employee]
        
        if manager_row.empty:
            # If no manager is found, break the loop
            break
        
        # Get the current employee's manager
        current_employee = manager_row['Manager_ID'].values[0]
        
        if pd.notnull(current_employee):
            chain.append(f'"{int(current_employee)}"')  # Add double quotes to each manager ID
    
    return chain

# Apply the function to create the 'manager_chain' column
employees_df['manager_chain'] = employees_df['Employee_id'].apply(lambda x: get_manager_chain(x, employees_df))

# Convert the list of quoted manager IDs into a comma-separated string
employees_df['manager_chain'] = employees_df['manager_chain'].apply(lambda x: ','.join(x))

# Create the final DataFrame with 'Employee_id' and 'manager_chain'
hierarchy_df = employees_df[['Employee_id', 'manager_chain']]

# Save the result to a CSV file
hierarchy_df.to_csv('hierarchy_by_employee.csv', index=False)
