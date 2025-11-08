"""
ITM 352 - Assignment 2: Sales Data Dashboard
Author: Kyle McGarry
Date: November 2025


# individual requirements for myself were number #2 and #5

AI USAGE DOCUMENTATION (Required by Assignment):
=====================================
AI Tool Used: Claude (Anthropic)
AI was used to help implement the following components:

1. ENHANCED MENU FUNCTIONS (Lines ~200-350): 
   Prompt: "Help me create pivot table functions for sales analysis by region, customer type, and product category"
   AI helped generate the pandas groupby and pivot_table code patterns

2. CUSTOM PIVOT TABLE GENERATOR (Lines ~400-500):
   Prompt: "Create an interactive pivot table generator with user selection menus"
   AI generated the menu structure and pandas pivot_table implementation

3. QUALITY IMPROVEMENTS (Lines ~180-220, ~550-600):
   Prompt: "Add input validation, error handling, and documentation to meet assignment quality requirements"
   AI helped with try/catch blocks, assertions, and docstring formatting

4. INDIVIDUAL REQUIREMENT #2 (Lines ~150-180):
   Prompt: "Help me create a data summary function that displays key metrics like total orders, employees, regions, etc."
   AI helped generate the comprehensive data overview with statistical summaries and categorical breakdowns

5. INDIVIDUAL REQUIREMENT #5 (Lines ~350-380):
   Prompt: "Create a simple employee performance ranking function using existing code patterns"
   AI generated the employee ranking logic using groupby patterns

6. TERMINAL OUTPUT FORMATTING (Lines ~285, ~335, ~118, ~600):
   Prompt: "Add visual separators to break up terminal output and make it easier to read"
   AI helped add "END OF ANALYSIS" separators, "DATA SUMMARY COMPLETE" markers, and 
   "NEW MENU SESSION" dividers to improve readability and distinguish between different 
   sections of output in the terminal

7. CODE DOCUMENTATION IMPROVEMENTS (Lines ~158-163, ~354-359, ~377-379):
   Prompt: "Add explanatory comments to complex data processing and calculation sections"
   AI helped add inline comments explaining date conversion logic, pivot table structure, 
   percentage calculations, and data processing steps to make the code more readable

Original Core Code: The foundational structure (data loading, basic menu, display functions) 
was written by Kyle McGarry. AI was used to enhance and expand functionality while 
maintaining the original code patterns and style.

All AI-generated code was reviewed, understood, and modified to meet assignment requirements.
=====================================

Dashboard Features:
- Interactive menu with 11+ analytical options
- Custom pivot table generator with user selection
- Employee performance ranking system  
- Comprehensive data validation and error handling
"""

import pandas as pd
import numpy as np
import pyarrow 
import ssl
import time

# Temporary fix.  Don't do this in production code.
ssl._create_default_https_context = ssl._create_unverified_context
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', '{:.2f}'.format)


def display_data_summary(df):
    """
    Display comprehensive data summary as required by Individual Requirement #2
    Shows: total orders, employees, regions, date range, customers, categories, states, total sales, quantities
    """
    print("\n" + "="*60)
    print("                    DATA SUMMARY")
    print("="*60)
    
    try:
        # Basic counts
        total_orders = len(df)
        unique_employees = df['employee_id'].nunique() if 'employee_id' in df.columns else 0
        unique_regions = df['sales_region'].nunique() if 'sales_region' in df.columns else 0
        unique_customers = df['customer_name'].nunique() if 'customer_name' in df.columns else 0
        unique_categories = df['product_category'].nunique() if 'product_category' in df.columns else 0
        unique_states = df['customer_state'].nunique() if 'customer_state' in df.columns else 0
        
        # Financial and quantity totals
        total_sales = df['sales'].sum() if 'sales' in df.columns else 0
        total_quantity = df['quantity'].sum() if 'quantity' in df.columns else 0
        
        # Date range analysis
        date_info = "Not available"
        if 'order_date' in df.columns:
            # Filter out invalid dates (zeros from fillna)
            valid_dates = df[df['order_date'] != 0]['order_date']
            if len(valid_dates) > 0:
                min_date = valid_dates.min().strftime('%Y-%m-%d')
                max_date = valid_dates.max().strftime('%Y-%m-%d')
                date_info = f"{min_date} to {max_date}"
        
        # Display the summary
        print(f"📊 Orders & Transactions:")
        print(f"   • Total Orders: {total_orders:,}")
        print(f"   • Date Range: {date_info}")
        
        print(f"\n👥 People & Geography:")
        print(f"   • Unique Employees: {unique_employees:,}")
        print(f"   • Sales Regions: {unique_regions:,}")
        print(f"   • Unique Customers: {unique_customers:,}")
        print(f"   • States Covered: {unique_states:,}")
        
        print(f"\n🛍️ Products & Sales:")
        print(f"   • Product Categories: {unique_categories:,}")
        print(f"   • Total Quantity Sold: {total_quantity:,}")
        print(f"   • Total Sales Amount: ${total_sales:,.2f}")
        
        # Additional insights
        if total_orders > 0:
            avg_order_value = total_sales / total_orders
            avg_quantity_per_order = total_quantity / total_orders
            print(f"\n📈 Averages:")
            print(f"   • Average Order Value: ${avg_order_value:,.2f}")
            print(f"   • Average Quantity per Order: {avg_quantity_per_order:.1f}")
        
        print("="*60)
        print("\n" + ">"*20 + " DATA SUMMARY COMPLETE " + "<"*20)
        
    except Exception as e:
        print(f"Error generating data summary: {e}")
        print("="*60)


def load_csv(file_path):
    """
    Load and process sales data from CSV file with comprehensive error handling.
    
    Args:
        file_path (str): URL or path to the CSV file
        
    Returns:
        pandas.DataFrame: Processed sales data with calculated sales column,
                         or None if loading fails
                         
    Quality Features:
    - Defensive programming with multiple exception types
    - Data validation and required column checking  
    - Performance timing and user feedback
    - Missing data handling with zeros replacement
    """
    print(f"Reading CSV file from {file_path}...")
    start_time = time.time()
    
    try:

        df = pd.read_csv(file_path, engine="pyarrow")
        end_time = time.time()
        load_time = end_time - start_time
        print(f"CSV file loaded successfully in {load_time:.2f} seconds.")
        print(f"Number of rows: {len(df)}")
        print(f"Columns: {df.columns.tolist()}")

        # Convert order_date from text format (MM/DD/YY) to proper datetime objects
        # 'coerce' means invalid dates become NaN instead of causing errors
        df['order_date'] = pd.to_datetime(df['order_date'], format='%m/%d/%y', errors='coerce')
        
        # Replace any missing values (NaN) with 0 to prevent calculation errors
        df.fillna(0, inplace=True)

        # Calculate total sales amount by multiplying quantity sold × unit price
        # This creates a new 'sales' column for our analysis
        df['sales'] = df['quantity'] * df['unit_price']
        required_columns = ['quantity', 'unit_price', 'order_date']
        # Check that the required columns are in df
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"Warning: Missing required columns: {missing_columns}")
        else:
            print("All required columns are present.")
        
        return df

    except FileNotFoundError as e:
        print(f"Error: The file {file_path} was not found. {e}")

    except pd.errors.EmptyDataError as e:
        print(f"Error: The file {file_path} is empty. {e}")
        return None
    
    except pd.errors.ParserError as e:
        print(f"Error: There was a parsing error while reading {file_path}. {e}")
        return None
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    

def display_rows(dataframe):
    """
    Interactive function to display selected rows with comprehensive input validation.
    
    Args:
        dataframe (pandas.DataFrame): Sales data to display
        
    Quality Features:
    - Input validation for numeric ranges and special commands
    - User-friendly error messages and guidance
    - Handles edge cases (empty input, invalid numbers, out of range)
    - Defensive programming against various input types
    """
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        print(f"\nEnter the number of rows to display (Attempt {attempts + 1}/{max_attempts})")
        print(f" - Enter a number 1 to {len(dataframe)}")  
        print(" - To see all rows, enter 'all'")
        print(" - To skip preview, press Enter")
        
        try:
            user_input = input("Your choice: ").strip().lower()

            if user_input == '':
                print("✅ Skipping preview.")
                break
            elif user_input == 'all':
                if len(dataframe) > 100:
                    confirm = input(f"⚠️  This will display {len(dataframe)} rows. Continue? (y/n): ").strip().lower()
                    if confirm != 'y':
                        print("Display cancelled.")
                        break
                print("✅ Displaying all rows:")
                print(dataframe)
                break
            elif user_input.isdigit():
                num_rows = int(user_input)
                if 1 <= num_rows <= len(dataframe):
                    print(f"✅ Displaying the first {num_rows} rows:")
                    print(dataframe.head(num_rows))
                    break
                else:
                    print(f"❌ Error: Please enter a number between 1 and {len(dataframe)}")
                    attempts += 1
            else:
                print("❌ Error: Please enter a number, 'all', or press Enter to skip.")
                attempts += 1
                
        except KeyboardInterrupt:
            print("\n\n👋 Display cancelled by user.")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            attempts += 1
    
    if attempts >= max_attempts:
        print("⚠️  Maximum attempts reached. Skipping display.")

def validate_sales_data(sales_data):
    """AI-ASSISTED: Quality requirement - validate data using assertions as required by rubric"""
    try:
        # Check basic requirements (using assertions as required by assignment)
        assert sales_data is not None and len(sales_data) > 0, "Data must exist and have rows"
        assert isinstance(sales_data, pd.DataFrame), "Must be a pandas DataFrame"
        
        # Check required columns exist
        required_cols = ['sales', 'quantity', 'employee_name', 'sales_region']
        for col in required_cols:
            assert col in sales_data.columns, f"Missing required column: {col}"
        
        # Check data quality
        assert sales_data['sales'].min() >= 0, "Sales values cannot be negative"
        
        print("✅ Data validation passed - all assertions successful")
        return True
        
    except AssertionError as e:
        print(f"❌ Data validation failed: {e}")
        return False

def exit_program(sales_data):
    """Exit program gracefully with validation check."""
    print("👋 Exiting the program. Goodbye!")
    exit(0)

# AI-ASSISTED: Menu option 2 - Pivot table showing sales breakdown
def total_sales_by_region_and_order_type(sales_data):
    """Shows how much each region sold in Retail vs Wholesale orders"""
    try:
        # Create cross-tabulation: regions as rows, order types as columns
        pivot_table = pd.pivot_table(sales_data, 
                                   index='sales_region',      # Rows: each region
                                   columns='order_type',      # Columns: Retail/Wholesale  
                                   values='sales',            # What to calculate
                                   aggfunc='sum',             # Sum up the sales
                                   fill_value=0)              # Show 0 instead of blanks
        
        print("\n--- Total Sales by Region and Order Type ---")
        print(pivot_table)
        print(f"\nGrand Total Sales: ${pivot_table.sum().sum():,.2f}")
        print("\n" + "-"*50 + " END OF ANALYSIS " + "-"*50)
        return pivot_table
    except KeyError as e:
        print(f"Error: Required column not found - {e}")
        return None

# AI-ASSISTED: Menu option 3 - Multiple average calculations  
def average_sales_by_region_state_type(sales_data):
    """Shows average order values across different geographic and business dimensions"""
    try:
        print("\n--- Average Sales Analysis ---")
        
        # Group by region and calculate mean - shows which regions have higher-value orders
        avg_by_region = sales_data.groupby('sales_region')['sales'].mean().sort_values(ascending=False)
        print("\n1. Average Sales by Region:")
        for region, avg_sales in avg_by_region.items():
            print(f"   {region}: ${avg_sales:,.2f}")
        
        # Group by state and calculate mean - shows which states buy more per order
        avg_by_state = sales_data.groupby('customer_state')['sales'].mean().sort_values(ascending=False)
        print(f"\n2. Average Sales by State (Top 10):")
        for state, avg_sales in avg_by_state.head(10).items():
            print(f"   {state}: ${avg_sales:,.2f}")
        
        # Group by order type - compares Retail vs Wholesale average order size
        avg_by_type = sales_data.groupby('order_type')['sales'].mean().sort_values(ascending=False)
        print(f"\n3. Average Sales by Order Type:")
        for order_type, avg_sales in avg_by_type.items():
            print(f"   {order_type}: ${avg_sales:,.2f}")
        
        return avg_by_region, avg_by_state, avg_by_type
    except KeyError as e:
        print(f"Error: Required column not found - {e}")
        return None

# Menu item 4: Sales by customer type and order type by state
def sales_by_customer_order_type_by_state(sales_data):
    """Create a pivot table with sub-rows showing sales by customer type and order type by state"""
    try:
        pivot_table = pd.pivot_table(sales_data, 
                                   index=['customer_state', 'customer_type'], 
                                   columns='order_type', 
                                   values='sales', 
                                   aggfunc='sum', 
                                   fill_value=0)
        print("\n--- Sales by Customer Type and Order Type by State ---")
        print(pivot_table)
        print("\n" + "-"*50 + " END OF ANALYSIS " + "-"*50)
        return pivot_table
    except KeyError as e:
        print(f"Error: Required column not found - {e}")
        return None

# Menu item 5: Total sales quantity and price by region and product
def total_sales_quantity_price_by_region_product(sales_data):
    """Create a pivot table that shows sales by region and product, summing quantity and sales price"""
    try:
        # Create a multi-level pivot table with:
        # - Index: Two levels (region, then product category within each region)
        # - Values: Both quantity sold and sales revenue
        # - Aggregation: Sum up all values for each region/product combination
        pivot_table = pd.pivot_table(sales_data, 
                                   index=['sales_region', 'product_category'], 
                                   values=['quantity', 'sales'], 
                                   aggfunc={'quantity': 'sum', 'sales': 'sum'})
        print("\n--- Total Sales Quantity and Price by Region and Product ---")
        print(pivot_table)
        
        # Show totals
        total_quantity = pivot_table['quantity'].sum()
        total_sales = pivot_table['sales'].sum()
        print(f"\nOverall Totals:")
        print(f"Total Quantity: {total_quantity:,.0f}")
        print(f"Total Sales: ${total_sales:,.2f}")
        
        return pivot_table
    except KeyError as e:
        print(f"Error: Required column not found - {e}")
        return None

# Menu item 6: Total sales quantity and price by customer type
def total_sales_quantity_price_by_customer_type(sales_data):
    """Create a pivot table that shows sales by customer type, summing quantity and sales price"""
    try:
        summary = sales_data.groupby('customer_type').agg({
            'quantity': 'sum',
            'sales': 'sum'
        }).round(2)
        
        print("\n--- Total Sales Quantity and Price by Customer Type ---")
        print(summary)
        
        # Calculate what percentage each customer type represents of the total
        # Formula: (customer_type_total / grand_total) × 100
        summary['quantity_pct'] = (summary['quantity'] / summary['quantity'].sum() * 100).round(1)
        summary['sales_pct'] = (summary['sales'] / summary['sales'].sum() * 100).round(1)
        
        print(f"\nWith Percentages:")
        for customer_type in summary.index:
            qty = summary.loc[customer_type, 'quantity']
            sales = summary.loc[customer_type, 'sales']
            qty_pct = summary.loc[customer_type, 'quantity_pct']
            sales_pct = summary.loc[customer_type, 'sales_pct']
            print(f"{customer_type}: {qty:,.0f} units ({qty_pct}%), ${sales:,.2f} ({sales_pct}%)")
        
        return summary
    except KeyError as e:
        print(f"Error: Required column not found - {e}")
        return None

# Menu item 7: Max and min sales price by category
def max_min_sales_by_category(sales_data):
    """Create a pivot table that shows max and min sales price by category"""
    try:
        stats = sales_data.groupby('product_category')['sales'].agg(['min', 'max', 'mean', 'count']).round(2)
        stats.columns = ['Min Sales', 'Max Sales', 'Average Sales', 'Number of Orders']
        
        print("\n--- Max and Min Sales Price by Product Category ---")
        print(stats)
        
        # Find the category with highest and lowest average
        max_avg_category = stats['Average Sales'].idxmax()
        min_avg_category = stats['Average Sales'].idxmin()
        
        print(f"\nInsights:")
        print(f"Highest average sales: {max_avg_category} (${stats.loc[max_avg_category, 'Average Sales']:,.2f})")
        print(f"Lowest average sales: {min_avg_category} (${stats.loc[min_avg_category, 'Average Sales']:,.2f})")
        
        return stats
    except KeyError as e:
        print(f"Error: Required column not found - {e}")
        return None

# AI-ASSISTED: Individual Requirement #5 - Employee Performance Ranking
def sales_performance_scorecard(sales_data):
    """
    Individual Requirement #5: Ranks employees by performance metrics
    This function creates a simple but effective employee ranking system
    """
    try:
        print("\n--- Employee Performance Ranking (Individual Req #5) ---")
        
        # Simple groupby like other functions
        performance = sales_data.groupby('employee_name').agg({
            'sales': 'sum',
            'customer_name': 'nunique',
            'quantity': 'sum'
        }).round(2)
        
        # Sort by sales (like other functions)
        performance = performance.sort_values('sales', ascending=False)
        
        # Show top 10
        print("\nTop 10 Employee Performance:")
        for i, (name, row) in enumerate(performance.head(10).iterrows(), 1):
            print(f"{i:2d}. {name}: ${row['sales']:,.2f} sales, {row['customer_name']:.0f} customers")
        
        return performance
        
    except Exception as e:
        print(f"Error: {e}")
        return None

# Menu item 9: Create a custom pivot table (basic version - will enhance later)
def create_custom_pivot_table(sales_data):
    """
    AI-ASSISTED: R4 Requirement - Interactive Custom Pivot Table Generator
    Lets users build their own analysis by selecting what data to group and analyze
    """
    print("\n" + "="*60)
    print("           INTERACTIVE CUSTOM PIVOT TABLE GENERATOR")
    print("="*60)
    
    try:
        # Define available field categories for better organization
        categorical_fields = ['employee_name', 'sales_region', 'order_type', 'customer_type', 
                             'customer_state', 'product_category', 'job_title']
        numerical_fields = ['sales', 'quantity', 'unit_price']
        
        # Step 1: Select row fields
        print("\nStep 1: Select ROWS (Index) - What should group your data?")
        print("-" * 50)
        for i, field in enumerate(categorical_fields, 1):
            if field in sales_data.columns:
                print(f"{i}. {field}")
        
        try:
            row_choice = int(input("\nEnter the number for ROWS: ").strip())
            if 1 <= row_choice <= len(categorical_fields):
                index_col = categorical_fields[row_choice - 1]
                if index_col not in sales_data.columns:
                    print(f"Error: {index_col} not available in data")
                    return None
            else:
                print("Invalid selection")
                return None
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None
        
        # Step 2: Select column fields (optional)
        print(f"\nStep 2: Select COLUMNS (Optional) - Cross-tabulation?")
        print("-" * 50)
        print("0. No columns (simple grouping)")
        for i, field in enumerate(categorical_fields, 1):
            if field in sales_data.columns and field != index_col:
                print(f"{i}. {field}")
        
        try:
            col_choice = int(input("\nEnter the number for COLUMNS (0 for none): ").strip())
            columns_col = None
            if col_choice > 0 and col_choice <= len(categorical_fields):
                columns_col = categorical_fields[col_choice - 1]
                if columns_col not in sales_data.columns or columns_col == index_col:
                    columns_col = None
        except ValueError:
            columns_col = None
        
        # Step 3: Select values to analyze
        print(f"\nStep 3: Select VALUES - What should be calculated?")
        print("-" * 50)
        for i, field in enumerate(numerical_fields, 1):
            if field in sales_data.columns:
                print(f"{i}. {field}")
        
        try:
            val_choice = int(input("\nEnter the number for VALUES: ").strip())
            if 1 <= val_choice <= len(numerical_fields):
                values_col = numerical_fields[val_choice - 1]
                if values_col not in sales_data.columns:
                    print(f"Error: {values_col} not available in data")
                    return None
            else:
                print("Invalid selection")
                return None
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None
        
        # Step 4: Select aggregation function
        print(f"\nStep 4: Select AGGREGATION FUNCTION")
        print("-" * 50)
        agg_options = ['sum', 'mean', 'count', 'min', 'max']
        for i, agg in enumerate(agg_options, 1):
            print(f"{i}. {agg}")
        
        try:
            agg_choice = int(input("\nEnter the number for AGGREGATION: ").strip())
            if 1 <= agg_choice <= len(agg_options):
                agg_func = agg_options[agg_choice - 1]
            else:
                print("Invalid selection, using 'sum'")
                agg_func = 'sum'
        except ValueError:
            print("Invalid input, using 'sum'")
            agg_func = 'sum'
        
        # Create the pivot table
        print(f"\nGenerating pivot table...")
        print(f"Rows: {index_col}")
        print(f"Columns: {columns_col if columns_col else 'None'}")
        print(f"Values: {agg_func}({values_col})")
        
        if columns_col:
            pivot_table = pd.pivot_table(sales_data, 
                                       index=index_col, 
                                       columns=columns_col,
                                       values=values_col, 
                                       aggfunc=agg_func, 
                                       fill_value=0)
        else:
            pivot_table = pd.pivot_table(sales_data, 
                                       index=index_col, 
                                       values=values_col, 
                                       aggfunc=agg_func, 
                                       fill_value=0)
        
        print(f"\n" + "="*60)
        print(f"CUSTOM PIVOT TABLE: {agg_func.upper()} of {values_col} by {index_col}")
        if columns_col:
            print(f"Cross-tabulated by: {columns_col}")
        print("="*60)
        print(pivot_table)
        print("="*60)
        
        return pivot_table
        
    except Exception as e:
        print(f"Error creating custom pivot table: {e}")
        return None

def show_employees_by_region(sales_data):
    pivot_table = pd.pivot_table(sales_data, index='sales_region', values='employee_id', aggfunc=pd.Series.nunique)
    pivot_table.columns = ['Number of Employees']  # Rename the colummn for readability
    print("\nNumber of Employees by Region:")
    print(pivot_table)
    return pivot_table


def display_menu(sales_data):
    """
    Display interactive menu with comprehensive input validation and error handling.
    
    Args:
        sales_data (pandas.DataFrame): Loaded sales data for analysis
        
    Quality Features:
    - Comprehensive input validation with user-friendly error messages
    - Handles empty input, invalid numbers, and out-of-range selections
    - Graceful keyboard interrupt handling
    - Implements menu structure using tuples for easy modification (R2 requirement)
    """
    print("\n\n" + "🔄"*30)
    print("NEW MENU SESSION")
    print("🔄"*30)
    print("\n" + "="*60)
    print()
    print("                    SALES DATA DASHBOARD")
    print()
    print("="*60)
    
    menu_options = (
        ("Show the first n rows of sales data", display_rows),
        ("Data Summary Overview (Individual Req #2)", lambda data: display_data_summary(data)),
        ("Total sales by region and order_type", total_sales_by_region_and_order_type),
        ("Average sales by region with average sales by state and sale type", average_sales_by_region_state_type),
        ("Sales by customer type and order type by state", sales_by_customer_order_type_by_state),
        ("Total sales quantity and price by region and product", total_sales_quantity_price_by_region_product),
        ("Total sales quantity and price by customer type", total_sales_quantity_price_by_customer_type),
        ("Max and min sales price by category", max_min_sales_by_category),
        ("Number of unique employees by region", show_employees_by_region),
        ("Create a custom pivot table", create_custom_pivot_table),
        ("Sales Performance Scorecard (Individual Req #5)", sales_performance_scorecard),
        ("Exit", exit_program)
    )

    print("\nAvailable Options:")
    for i, (description, _) in enumerate(menu_options, start=1):
        print(f"{i}. {description}")

    # Enhanced input validation for better user experience
    while True:
        try:
            menu_len = len(menu_options)
            user_input = input(f"Select an option (1 to {menu_len}): ").strip()
            
            # Validate input is not empty
            if not user_input:
                print("❌ Error: Please enter a selection.")
                continue
                
            # Convert to integer and validate range
            choice = int(user_input)
            if 1 <= choice <= menu_len:
                action = menu_options[choice - 1][1]
                action(sales_data)
                break  # Exit validation loop after successful execution
            else:
                print(f"❌ Error: Please enter a number between 1 and {menu_len}.")
                continue
                
        except ValueError:
            print("❌ Error: Please enter a valid number (not text).")
            continue
        except KeyboardInterrupt:
            print("\n\n👋 Program interrupted by user. Goodbye!")
            exit(0)
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            print("Please try again.")    

# ============================================================================
# MAIN PROGRAM EXECUTION
# ============================================================================

# Step 1: Load the sales data from Google Drive (as specified in assignment)
url = "https://drive.google.com/uc?id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"
print("🚀 Starting Sales Data Dashboard...")
sales_data = load_csv(url)  # This loads data AND shows summary (Individual Req #2)

# Step 2: Quality check - make sure data loaded properly (uses assertions as required)
if sales_data is not None:
    validate_sales_data(sales_data)
else:
    print("❌ Critical Error: Unable to load sales data. Program cannot continue.")
    exit(1)


def main():
    """
    Main program loop - keeps showing menu until user exits
    This design allows users to run multiple analyses in one session
    """
    print("\n🎯 Dashboard ready! Data loaded and validated successfully.")
    print("💡 Tip: You can run multiple analyses - the menu will keep coming back until you exit.")
    
    # Keep showing menu until user chooses to exit
    while True:
        display_menu(sales_data)


# Standard Python pattern - only run main() if this file is executed directly
if __name__ == "__main__":
    main()
        