import dlt

@dlt.resource
def users():
    yield[
        {"id":1, "name":"Anushka"},
        {"id":2, "name":"Urmila"}
    ]
    
pipeline = dlt.pipeline(
    pipeline_name = "test_pipeline",
    destination = "postgres",
    dataset_name = "test_dataset"
)

load_info = pipeline.run(users())
print(load_info)