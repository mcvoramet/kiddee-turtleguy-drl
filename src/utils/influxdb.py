from influxdb import InfluxDBClient


class InfluxDBParameterLogger:
    
        def __init__(self, host, port, database):
            self.client = InfluxDBClient(host, port)
            self.client.create_database(database)
    
        def insert_data(self, timestamp: int, datapoint_name: str, data: dict):
            json_body = [
                {
                    "measurement": "parameters",
                    "time": timestamp,
                    "fields": {
                        datapoint_name : data
                    }
                }
            ]
    
            self.client.write_points(json_body)
    
