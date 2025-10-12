import pandas as pd
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

# Global dataframe variable
df = None

def load_and_clean():
    """Upload and clean the CSV file"""
    global df
    try:
        file_path = filedialog.askopenfilename(
            title="Select a CSV file",
            filetypes=[("CSV files", "*.csv")]
        )
        if not file_path:
            return

        df = pd.read_csv(file_path)

        # --- CLEANING PROCESS ---
        df.columns = df.columns.str.strip()          # Remove whitespace
        df.dropna(how="all", inplace=True)           # Remove empty rows
        df.drop_duplicates(inplace=True)             # Remove duplicates

        # Fill missing values
        for col in df.columns:
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col].fillna(df[col].median(), inplace=True)
            else:
                if not df[col].mode().empty:
                    df[col].fillna(df[col].mode()[0], inplace=True)

        # Convert to proper datatypes
        for col in df.columns:
            try:
                df[col] = pd.to_numeric(df[col])
            except:
                try:
                    df[col] = pd.to_datetime(df[col])
                except:
                    pass

        # Display cleaned preview
        output.delete("1.0", tk.END)
        output.insert(tk.END, "✅ Data Loaded and Cleaned Successfully\n\n")
        output.insert(tk.END, df.head().to_string(index=False))
        output.insert(tk.END, f"\n\nTotal Rows: {len(df)} | Columns: {len(df.columns)}")
        output.insert(tk.END, "\n\n✅ Missing values handled using Median/Mode.")
        output.insert(tk.END, "\n✅ Ready for Visualization.")

        # Show buttons
        download_button.pack(pady=5)
        visualize_button.pack(pady=5)

    except Exception as e:
        output.delete("1.0", tk.END)
        output.insert(tk.END, f"❌ Error: {str(e)}")

def save_cleaned_file():
    """Save cleaned CSV"""
    global df
    if df is None:
        messagebox.showwarning("No Data", "Please upload and clean a CSV file first.")
        return

    save_path = filedialog.asksaveasfilename(
        title="Save cleaned CSV file as",
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")]
    )
    if save_path:
        df.to_csv(save_path, index=False)
        messagebox.showinfo("File Saved", f"✅ Cleaned file saved at:\n{save_path}")

def save_visualization_pdf():
    """Generate and save data visualization PDF"""
    global df
    if df is None:
        messagebox.showwarning("No Data", "Please upload and clean a CSV file first.")
        return

    save_path = filedialog.asksaveasfilename(
        title="Save Visualization Report as",
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")]
    )
    if not save_path:
        return

    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) < 2:
        messagebox.showwarning("Not Enough Data", "Need at least two numeric columns for visualization.")
        return

    # Create PDF with multiple plots
    with PdfPages(save_path) as pdf:
        plt.figure(figsize=(8, 5))
        sns.histplot(df[numeric_cols[0]], kde=True)
        plt.title(f"Histogram of {numeric_cols[0]}")
        pdf.savefig()
        plt.close()

        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=numeric_cols[0], y=numeric_cols[1], data=df)
        plt.title(f"Scatter Plot: {numeric_cols[0]} vs {numeric_cols[1]}")
        pdf.savefig()
        plt.close()

        plt.figure(figsize=(8, 5))
        sns.stripplot(data=df[numeric_cols])
        plt.title("Strip Plot of Numeric Columns")
        pdf.savefig()
        plt.close()

        plt.figure(figsize=(8, 5))
        sns.boxplot(data=df[numeric_cols])
        plt.title("Box Plot of Numeric Columns")
        pdf.savefig()
        plt.close()

    messagebox.showinfo("Visualization Saved", f"📊 Visualization PDF saved at:\n{save_path}")

# --- GUI SETUP ---
window = tk.Tk()
window.title("CSV Data Cleaner + Visualization Generator")
window.geometry("880x650")

title_label = tk.Label(window, text="CSV Data Cleaner and Visualization Tool", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

load_button = tk.Button(window, text="Upload & Clean CSV", command=load_and_clean,
                        bg="#4CAF50", fg="white", font=("Arial", 12))
load_button.pack(pady=10)

download_button = tk.Button(window, text="Download Cleaned File", command=save_cleaned_file,
                            bg="#2196F3", fg="white", font=("Arial", 12))
download_button.pack_forget()

visualize_button = tk.Button(window, text="Download Visualization PDF", command=save_visualization_pdf,
                             bg="#9C27B0", fg="white", font=("Arial", 12))
visualize_button.pack_forget()

output = scrolledtext.ScrolledText(window, width=100, height=25, font=("Courier", 10))
output.pack(pady=10)

window.mainloop()
