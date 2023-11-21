from metaflow import FlowSpec, step, Parameter, pip_base
@pip_base(
    packages={
        "s3fs": '2023.9.0',
    })
class PLPinMatch(FlowSpec):
    app_year = Parameter('year')
    app_month = Parameter('month')
    database = Parameter('db')
    schema = Parameter('schema')
    ml_bucket_name = Parameter('s3')
    ml_prefix = Parameter('prefix')
    
    
    @step
    def start(self):
        import time

        args = {   
            "app_year": self.app_year,
            "app_month": self.app_month,
            "ml_bucket_name": self.ml_bucket_name, 
            "ml_prefix": self.ml_prefix,
            "database": self.database,
            "schema ": self.schema }
        
        print(args)
        time.sleep(40)
        self.next(self.end)
        
    @step
    def end(self):
        print('Successfully finished Ascend Downloading process')

if __name__ == "__main__":
    PLPinMatch()