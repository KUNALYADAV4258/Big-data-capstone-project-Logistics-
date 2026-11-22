# Data Sources – Smart Logistics Analytics

## Project Overview
Project: Smart Logistics Analytics – Supply Chain and Delivery Optimization

This project uses three CSV datasets to study logistics operations, warehouse performance, shipment status, and delivery delays.

## Dataset 1: Logistics Warehouse Dataset

- File name: `logistics_dataset.csv`
- Records: 3,204
- Columns: 23
- Data includes: Inventory levels, reorder points, demand, warehouse locations, picking time, and fulfilment information.
- Source: https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis?utm_source=chatgpt.com

## Dataset 2: Smart Logistics Dataset

- File name: `smart_logistics_dataset.csv`
- Records: 1,000
- Columns: 16
- Data includes: Shipment status, location coordinates, inventory levels, traffic status, temperature, humidity, and logistics delays.
- Source: www.kaggle.com/datasets/ziya07/logistics-warehouse-dataset?utm_source=chatgpt.com
## Dataset 3: DataCo Supply Chain Dataset

- File name: `DataCoSupplyChainDataset-selected-columns.csv`
- Records: 74,544
- Columns: 10
- Data includes: Shipping days, delivery status, late delivery risk, sales, and customer information.
- Source: www.kaggle.com/datasets/ziya07/logistics-warehouse-dataset?utm_source=chatgpt.com
## Extraction Verification

All three CSV files were successfully accessed using a Python script.

The script verified:
- File availability
- Column names
- Number of records
- File sizes

The original datasets were kept unchanged.

## Storage Plan

Platform: Databricks

Storage type: Unity Catalog Volume

Purpose: Store the original CSV files as raw data for the next stage of the project.
