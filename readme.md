# Smartsheet API Data Extraction

Python project for extracting, processing, and exporting data from the Smartsheet API into structured CSV files.

## 📌 Project Overview

This project automates data extraction from Smartsheet workspaces and spreadsheets through HTTP requests.

It retrieves workspaces, spreadsheets, columns, and rows, transforming the API responses into structured Pandas DataFrames and exporting the results as CSV files.

The solution was developed with a modular architecture, separating API requests, data processing, and file export operations.

## 🚀 Features

- **Workspace Extraction:** Retrieves available workspaces using paginated API requests.
- **Spreadsheet Discovery:** Retrieves spreadsheets associated with each workspace.
- **Column Mapping:** Maps column IDs to their corresponding names.
- **Row Extraction:** Retrieves spreadsheet records and maps cell values to their respective columns.
- **Pagination Handling:** Processes large datasets through offset-based pagination.
- **Data Processing:** Converts API responses into Pandas DataFrames.
- **Data Cleaning:** Removes technical metadata columns and empty rows.
- **Filename Normalization:** Removes accents and special characters from workspace and spreadsheet names.
- **CSV Export:** Exports structured datasets using UTF-8 with BOM encoding.

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Application development |
| Requests | HTTP requests and API integration |
| Pandas | Data manipulation and transformation |
| Python Dotenv | Environment variable management |
| Smartsheet API | Data source |

## 📂 Project Structure

```text
API-Smartsheet/
│
├── functions/
│   ├── get_workspace.py
│   ├── get_sheet.py
│   ├── get_columns.py
│   └── get_sheet_line.py
│
├── utils/
│   ├── normalize.py
│   └── export.py
│
├── data/
│   └── (exported CSV files)
│
├── .env
├── .env_example
├── main.py
└── README.md
```

### Module Description

| Module | Description |
|---|---|
| `get_workspace.py` | Retrieves available workspaces. |
| `get_sheet.py` | Retrieves spreadsheets associated with a workspace. |
| `get_columns.py` | Retrieves spreadsheet columns and maps their IDs to column names. |
| `get_sheet_line.py` | Extracts spreadsheet rows and maps cell values to their corresponding columns. |
| `normalize.py` | Normalizes text by removing accents and special characters. |
| `export.py` | Creates output directories and exports DataFrames to CSV files. |
| `main.py` | Orchestrates the complete data extraction and export workflow. |

## ⚙️ Installation and Configuration

### 1. Clone the repository

```bash
git clone https://github.com/dlinoba/API-Smartsheet.git
```

### 2. Navigate to the project directory

```bash
cd API-Smartsheet
```

### 3. Install dependencies

```bash
pip install requests pandas python-dotenv
```

### 4. Configure environment variables

Create a `.env` file in the project root directory, using `.env_example` as a reference.

Configure the following variables:

```env
API_TOKEN=YOUR_SMARTSHEET_API_TOKEN
root_url=YOUR_API_BASE_URL/
```

**Important:** The `root_url` should include a trailing slash because the application appends endpoint paths directly to it.

The application uses Bearer Token authentication.

Never commit your `.env` file or expose your API credentials.

## ▶️ Execution

Run the application with:

```bash
python main.py
```

The extraction workflow follows these steps:

1. Retrieves all available workspaces.
2. Identifies spreadsheets associated with each workspace.
3. Retrieves the columns of each spreadsheet.
4. Extracts all spreadsheet rows using pagination.
5. Maps column IDs to their corresponding column names.
6. Converts the extracted records into Pandas DataFrames.
7. Removes technical metadata columns and completely empty rows.
8. Exports the processed data into CSV files.

## 📊 Data Export Structure

Exported files are automatically organized by workspace.

The output structure follows this pattern:

```text
data/
│
├── Workspace_Name/
│   ├── 12345_Spreadsheet_Name.csv
│   └── 12346_Another_Spreadsheet.csv
│
└── Another_Workspace/
    └── 78901_Project_Tracking.csv
```

Each CSV filename contains the spreadsheet ID and its normalized name.

Directories are created automatically when they do not exist.

## 🔄 Data Processing

The project uses Pandas to transform API responses into structured tabular datasets.

During processing:

- Spreadsheet cell values are mapped using the corresponding column IDs.
- Technical metadata fields are removed from the exported DataFrames:
  - `sheetId`
  - `rowId`
  - `rowNumber`
  - `createdAt`
  - `modifiedAt`
- Completely empty rows are discarded.
- Workspace and spreadsheet names are normalized to create filesystem-friendly paths.
- CSV files are exported using `utf-8-sig` encoding to improve compatibility with Microsoft Excel.

## 🔐 Security

- API credentials are stored in environment variables.
- The `.env` file must not be committed to version control.
- The `.env_example` file should contain only illustrative values.
- API tokens should be kept private and rotated when necessary.

## 👨‍💻 Author

**Deyvid Linoba**

- GitHub: [@dlinoba](https://github.com/dlinoba)
- LinkedIn: [Deyvid Linoba](https://www.linkedin.com/in/deyvid-linoba/)

---

*Developed with Python for automated API integration, data extraction, and structured data export.*
