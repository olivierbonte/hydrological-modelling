# %% Imports
import pandas as pd
from conf import (
    DISCHARGE_RAW_DIR,
    POTENTIAL_EVAPOTRANSPIRATION_RAW_DIR,
    PRECIPITATION_RAW_DIR,
    STATION_ID_MAARKE_KERKEM,
    STATION_ID_NEDERZWALM,
    STATION_ID_WAREGEM,
    TIMESPACING_DICT,
)
from pywaterinfo import Waterinfo

PRECIPITATION_RAW_DIR.mkdir(parents=True, exist_ok=True)
DISCHARGE_RAW_DIR.mkdir(parents=True, exist_ok=True)
POTENTIAL_EVAPOTRANSPIRATION_RAW_DIR.mkdir(parents=True, exist_ok=True)
vmm = Waterinfo("vmm", cache=True)


# %% Helper functions
def _parse_date_columns(
    df: pd.DataFrame, date_cols: list = ["from", "to"]
) -> pd.DataFrame:
    """Parse specified date columns in a DataFrame into pandas datetime objects."""
    df = df.copy()
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col])
    return df


# %% Nederzwalm/Zwalmbeek (L06_342)
station_info_nz = _parse_date_columns(vmm.get_timeseries_list(STATION_ID_NEDERZWALM))

## Catchment precipitation
station_info_nz_precip = station_info_nz.query(
    "stationparameter_longname == 'Precipitation of catchment' and ts_name == 'Rro.DagTot'"
)

ts_id_nz_precip = station_info_nz_precip["ts_id"].values[0]
df_nz_precip = (
    vmm.get_timeseries_values(
        ts_id=ts_id_nz_precip,
        start=station_info_nz_precip["from"].dt.date.values[0],
        end=station_info_nz_precip["to"].dt.date.values[0],
    )
    .reset_index()
    .assign(
        Timestamp=lambda df: pd.to_datetime(pd.to_datetime(df["Timestamp"]).dt.date)
    )
    .set_index("Timestamp")
)
_time_spacing = station_info_nz_precip["ts_spacing"].values[0]
df_nz_precip.to_csv(
    PRECIPITATION_RAW_DIR
    / f"precipitation_{STATION_ID_NEDERZWALM}_{TIMESPACING_DICT[_time_spacing]}.csv"
)
station_info_nz_precip.to_csv(
    PRECIPITATION_RAW_DIR
    / f"precipitation_meta_{STATION_ID_NEDERZWALM}_{TIMESPACING_DICT[_time_spacing]}.csv",
    index=False,
)

## Discharge
station_info_nz_discharge = station_info_nz.query(
    "stationparameter_longname == 'River Discharge' and ts_shortname == 'Day.Mean'"
)
ts_id_nz_discharge = station_info_nz_discharge["ts_id"].values[0]
df_nz_discharge = (
    vmm.get_timeseries_values(
        ts_id=ts_id_nz_discharge,
        start=station_info_nz_discharge["from"].dt.date.values[0],
        end=station_info_nz_discharge["to"].dt.date.values[0],
    )
    .reset_index()
    .assign(
        Timestamp=lambda df: pd.to_datetime(pd.to_datetime(df["Timestamp"]).dt.date)
    )
    .set_index("Timestamp")
)
_time_spacing = station_info_nz_discharge["ts_spacing"].values[0]
df_nz_discharge.to_csv(
    DISCHARGE_RAW_DIR
    / f"discharge_{STATION_ID_NEDERZWALM}_{TIMESPACING_DICT[_time_spacing]}.csv"
)
station_info_nz_discharge.to_csv(
    DISCHARGE_RAW_DIR
    / f"discharge_meta_{STATION_ID_NEDERZWALM}_{TIMESPACING_DICT[_time_spacing]}.csv",
    index=False,
)

# %% Maarke-Kerkem (P06_014)
station_info_mk = _parse_date_columns(vmm.get_timeseries_list(STATION_ID_MAARKE_KERKEM))
station_info_mk_precip = station_info_mk.query(
    "stationparameter_longname == 'Precipitation' and ts_shortname == 'Day.Total'"
)
ts_id_mk_precip = station_info_mk_precip["ts_id"].values[0]
df_mk_precip = (
    vmm.get_timeseries_values(
        ts_id=ts_id_mk_precip,
        start=station_info_mk_precip["from"].dt.date.values[0],
        end=station_info_mk_precip["to"].dt.date.values[0],
    )
    .reset_index()
    .assign(
        Timestamp=lambda df: pd.to_datetime(pd.to_datetime(df["Timestamp"]).dt.date)
    )
    .set_index("Timestamp")
)
_time_spacing = station_info_mk_precip["ts_spacing"].values[0]
df_mk_precip.to_csv(
    PRECIPITATION_RAW_DIR
    / f"precipitation_{STATION_ID_MAARKE_KERKEM}_{TIMESPACING_DICT[_time_spacing]}.csv"
)
station_info_mk_precip.to_csv(
    PRECIPITATION_RAW_DIR
    / f"precipitation_meta_{STATION_ID_MAARKE_KERKEM}_{TIMESPACING_DICT[_time_spacing]}.csv",
    index=False,
)

# %% Waregem (ME05_019)
station_info_waregem = _parse_date_columns(vmm.get_timeseries_list(STATION_ID_WAREGEM))
station_info_waregem_potential_evapotranspiration = station_info_waregem.query(
    "stationparameter_longname == 'Potential Evapotranspiration' and ts_shortname == 'Day.Total.Penman'"
)
ts_id_waregem_pet = station_info_waregem_potential_evapotranspiration["ts_id"].values[0]
df_waregem_pet = (
    vmm.get_timeseries_values(
        ts_id=ts_id_waregem_pet,
        start=station_info_waregem_potential_evapotranspiration["from"].dt.date.values[
            0
        ],
        end=station_info_waregem_potential_evapotranspiration["to"].dt.date.values[0],
    )
    .reset_index()
    .assign(
        Timestamp=lambda df: pd.to_datetime(pd.to_datetime(df["Timestamp"]).dt.date)
    )
    .set_index("Timestamp")
)
_time_spacing = station_info_waregem_potential_evapotranspiration["ts_spacing"].values[
    0
]
df_waregem_pet.to_csv(
    POTENTIAL_EVAPOTRANSPIRATION_RAW_DIR
    / f"potential_evapotranspiration_{STATION_ID_WAREGEM}_{TIMESPACING_DICT[_time_spacing]}.csv"
)
station_info_waregem_potential_evapotranspiration.to_csv(
    POTENTIAL_EVAPOTRANSPIRATION_RAW_DIR
    / f"potential_evapotranspiration_meta_{STATION_ID_WAREGEM}_{TIMESPACING_DICT[_time_spacing]}.csv",
    index=False,
)

# %%
