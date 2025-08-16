COVID-19 Spread Rate Forecast 

Target objectives

Produce a reproducible data pipeline that ingests, cleans and standardizes COVID-19 case, death, testing and vaccination data for time-series analysis. 

Define and validate core analytics measures (New Cases, New Deaths, Spread Rate %, Total Doses, demographic vaccination splits) for dashboards and aggregated reporting. 

Build a scalable Power BI model with well-designed relationships, helper tables (7-day rolling averages) and optimized measures for interactive exploration. 

Implement a Python forecasting component (additive Holt–Winters exponential smoothing) to extend the Spread Rate % horizon and quantify uncertainty for short-to-medium term planning. 

Base use of this forecast

Forecast target: daily Spread Rate % (historical overlay + forward projection). The forecast is produced by an additive Holt–Winters model and packaged with an uncertainty band to communicate confidence. 

Primary consumers: dashboard viewers and decision-makers who need a short-to-medium term view of epidemic trajectory for situational awareness, resource planning, and trend annotation. 

High level flow: Cleaned time-series → compute Spread Rate % and supporting measures → run Python Holt–Winters script → import forecast into Power BI and overlay with historical visuals.

Important repository notes (new)

Firstly: all the project-based main files are uploaded onto the main branch (switch to main to view all notebooks, scripts, Power BI files and docs).

Secondly: all the CSV data imported from kaggle.com is uploaded to the folder named csv-data-uesd (open that folder to inspect the raw CSVs used during ingestion).

These two points ensure the main logic and notebooks live on main, and source CSVs are centrally located under csv-data-uesd.
