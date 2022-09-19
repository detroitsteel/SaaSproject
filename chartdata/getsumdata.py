import json

import pandas as pd


def getsumquery(conn):
    sdata = pd.read_sql((""";WITH CTE AS 
                (SELECT MIN(CD.VALUENUM) OVER(PARTITION BY UM.Name, OT.Name) AS [MinValue]
                , MAX(CD.VALUENUM) OVER(PARTITION BY UM.Name, OT.Name) AS [MAXValue]
                , UM.Name AS [UnitOfMeasureName]
                , OT.Name AS [ObservationTypeName]
                FROM Chart_Data AS CD
                INNER JOIN Unit_Of_Measure AS UM ON CD.Unit_Of_Measure_Id = UM.ID
                INNER JOIN Observation_Type AS OT ON CD.Observation_Type_Id = OT.Id
                LEFT JOIN Result_Status AS RS ON CD.Result_Status_Id = RS.ID
                WHERE (RS.NAME <> 'Manual' OR RS.ID IS NULL)
                AND (CD.ERROR <> 1 OR CD.ERROR IS NULL)
                AND (CD.WARNING <> 1 OR CD.WARNING IS NULL)
                )
                SELECT COUNT(1) AS [NumberOfAdmissions]
                ,[MinValue]
                ,[MAXValue]
                ,[UnitOfMeasureName]
                ,[ObservationTypeName]
                FROM CTE
                GROUP BY 
                [MinValue]
                ,[MAXValue]
                ,[UnitOfMeasureName]
                ,[ObservationTypeName]
                ORDER BY [NumberOfAdmissions] DESC;"""), conn, )
    result = sdata.to_json(orient="split")
    parsed = json.loads(result)

    return json.dumps(parsed, indent=4)
