import json

import pandas as pd

def getdataquery(conn, listid):
    cur = conn.cursor()
    idss = pd.read_csv(listid)
    pids = tuple(idss['Ids'].tolist())
    print(idss)
    print(type(pids))
    #print(type(pids))

    qu = """SELECT CD.ID AS [ChartId],CD.ChartTime,CD.ValueNum,CD.Error
            ,CD.Warning,CD.Stopped,OT.ID AS [ObservationTypeId]
            ,OT.[Name] AS [ObservationName],RS.ID AS [ResultStatusId]
            ,RS.[Name] AS [ResultStatusName],UM.ID AS [UnitOfMeasureId]
            ,UM.[Name] AS [UnitOfMeasureName]
            FROM Chart_Data AS CD
            INNER JOIN Observation_Type AS OT ON CD.Observation_Type_Id = OT.ID
            INNER JOIN Result_Status AS RS ON CD.Result_Status_Id = RS.ID
            INNER JOIN Unit_Of_Measure AS UM ON CD.Unit_Of_Measure_Id = UM.Id
            WHERE CD.ID IN ({1}) --AND CD.ID IS NOT NULL
            LIMIT 10"""
    qu = qu.format('?', ','.join('?' * len(pids)))  # ('?', ','.join('?' * len(ids)))
    #print(len(pids))
    #print(qu)

    data = pd.read_sql_query(qu, conn, params=(pids))
    result = data.to_json(orient="split")
    parsed = json.loads(result)

    return json.dumps(parsed, indent=4)
