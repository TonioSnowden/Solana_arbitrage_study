import pandas as pd

# Define a function to calculate the volume-weighted price and total quantity
def calculate_vwp_and_qty(df, rounded_to='T'):
    # Create a new column 'volume' that represents the volume of each trade
    df['volume'] = df['price'] * df['qty']
    
    # Group by 'time' rounded down to the nearest second
    grouped = df.groupby(df['time'].dt.floor(rounded_to))
    
    # Calculate the volume-weighted price and total quantity for each group
    vwp = (grouped['volume']).sum() / grouped['qty'].sum()
    total_qty = grouped['qty'].sum()
    
    # Return a DataFrame with the 'time', 'price', and 'quantity' columns
    return pd.DataFrame({'time': vwp.index, 'price': vwp.values, 'qty': total_qty.values})