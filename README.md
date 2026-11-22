# Smart Logistics and Supply Chain Intelligence

A big data capstone project that takes logistics, warehouse, and fleet data through a Databricks Delta Lake Medallion workflow and presents curated outputs in Power BI.

## Project at a glance

- **Sources:** order history, warehouse inventory and SKU data, and IoT fleet telematics
- **Processing:** Databricks Delta Live Tables with Bronze, Silver, and Gold layers
- **Outputs:** four Gold CSV marts and a Power BI report with operational dashboard pages
- **Topics:** delivery performance, warehouse picking and stock risk, fleet utilization and delays

## Data sources

| Domain | Input file | Scale shown in project materials |
| --- | --- | ---: |
| Orders | `DataCoSupplyChainDataset.csv` | 180,519 order records |
| Warehouse | `logistics_dataset.csv` | 3,204 warehouse SKUs |
| Fleet / IoT | `smart_logistics_dataset.csv` | 1,000 GPS pings |

The architecture diagram also includes an Open-Meteo weather enrichment stage. The diagrams describe weather and route context such as precipitation, wind, and weather severity.

## Data workflow

1. **Land** the CSV inputs in Databricks storage using Unity Catalog / DBFS.
2. **Bronze** stores raw Delta tables and ingestion metadata.
3. **Silver** applies cleaning, validation, type handling, standard naming, and deduplication.
4. **Gold** produces aggregated marts for reporting.
5. **Serve** the Gold exports to Power BI.

The supplied DLT lineage screenshot reports 9 of 9 materialized views healthy and 184,723 total ingested records. The input counts above sum to the same total.

## Gold data marts

- `gold_shipment_delivery_kpis.csv` — delivery, order, sales, profit, delay, and on-time/late-risk measures by month, market, and shipping mode.
- `gold_warehouse_zone_efficiency.csv` — SKU and inventory measures by warehouse zone, category, and picking tier.
- `gold_fleet_telematics_delays.csv` — fleet utilization, waiting time, traffic, delay, and environmental measures.
- `gold_daily_executive_metrics.csv` — daily market-level order, sales, profit, delay, and OTIF measures.

## Power BI report

The supplied Power BI file is `Logistics Dashboard.pbix`. The screenshot set contains executive delivery, warehouse operations, fleet telematics, and DLT lineage views. The visible dashboard snapshots include 181K orders, $36.78M sales, 103K delayed orders, 3K warehouse SKUs, 844K inventory units, 240 SKUs at stockout risk, 10 fleet assets, 79.55% average utilization, and 566 delay incidents. Values are snapshot aggregates and may change with filters. Confirm KPI definitions and aggregation settings before using a displayed measure as a business target or service-level rate.

## Folder layout

The project materials are organized as follows (folder names may differ in your local copy):

```text
project/
├── raw data/                 # three source CSV files
├── gold layer csv data/      # four curated Gold CSV exports
├── Logistics Dashboard.pbix  # Power BI report
├── Logistics_Architecture_Diagram.png
├── etl pipeline.png
├── dash 1.png ... dash 4.png
├── Smart_Logistics_Capstone_Report.docx
└── README.md
```

## Refresh and use

1. Confirm the input CSV paths and schemas in the Databricks workspace.
2. Run the configured Databricks pipeline and review the DLT lineage and data-quality status.
3. Export or refresh the four Gold CSV outputs.
4. Update the Power BI data-source paths if the exports moved, then refresh the report.
5. Review filters and KPI definitions before sharing screenshots or conclusions.

The supplied project materials do not include a runnable notebook or pipeline source script in this handoff, so exact cluster setup, credentials, and one-click commands depend on the Databricks workspace configuration.

## Notes

- The report summarizes the project artifacts and dashboard screenshots supplied with the capstone.
- Dashboard numbers are presented as displayed snapshots, not independently re-computed metrics.
- The on-time card on the executive page is labeled as an average measure; validate its definition and unit in the Power BI model before describing it as a percentage.
