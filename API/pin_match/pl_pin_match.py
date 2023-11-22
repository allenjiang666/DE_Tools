from metaflow import FlowSpec, step, Parameter, conda_base

# @conda_base(    packages={
#         "s3fs": '2023.9.0',
#     })
class PLPinMatch(FlowSpec):
    date = Parameter('date')
    database = Parameter('db')
    schema = Parameter('schema')
    ml_bucket_name = Parameter('s3')
    ml_prefix = Parameter('prefix')
    
    
    @step
    def start(self):
        import time

        args = {   
            "app_date": self.date,
            "ml_bucket_name": self.ml_bucket_name, 
            "ml_prefix": self.ml_prefix,
            "database": self.database,
            "schema ": self.schema }
        
        print(args)
        time.sleep(20)
        self.next(self.end)
        
    @step
    def end(self):
        print('Successfully finished Ascend Downloading process')

if __name__ == "__main__":
    PLPinMatch()