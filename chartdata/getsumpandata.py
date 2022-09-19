import json

import pandas as pd


def getsumquery(conn):
    pddata = pd.read_sql(("""SELECT CD.VALUENUM
    , UM.Name AS [UnitOfMeasureName]
    , OT.Name AS [ObservationTypeName]
    FROM Chart_Data AS CD
    INNER JOIN Unit_Of_Measure AS UM ON CD.Unit_Of_Measure_Id = UM.ID
    INNER JOIN Observation_Type AS OT ON CD.Observation_Type_Id = OT.Id
    LEFT JOIN Result_Status AS RS ON CD.Result_Status_Id = RS.ID
    WHERE (RS.NAME <> 'Manual' OR RS.ID IS NULL)
    AND (CD.ERROR <> 1 OR CD.ERROR IS NULL)
    AND (CD.WARNING <> 1 OR CD.WARNING IS NULL)"""), conn, )
    pddata = pddata.groupby(['UnitOfMeasureName', 'ObservationTypeName']).agg({'VALUENUM': ['min', 'max', 'count']})
    pddata.columns = ['MinValue', 'MaxValue', 'NumberOfAdmissions']
    pddata = pddata.reset_index()
    result = pddata.to_json(orient="split")
    parsed = json.loads(result)

    return json.dumps(parsed, indent=4)
