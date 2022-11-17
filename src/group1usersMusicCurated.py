import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={
        "quoteChar": '"',
        "withHeader": True,
        "separator": "\t",
        "optimizePerformance": False,
    },
    connection_type="s3",
    format="csv",
    connection_options={
        "paths": ["s3://group1-data/raw/userCanciones.tsv"],
        "recurse": True,
    },
    transformation_ctx="S3bucket_node1",
)

# Script generated for node Change Schema (Apply Mapping)
ChangeSchemaApplyMapping_node1668094793373 = ApplyMapping.apply(
    frame=S3bucket_node1,
    mappings=[
        ("userid", "string", "userid", "string"),
        ("timestamp", "string", "timestamp", "string"),
        ("artid", "string", "artid", "string"),
        ("artname", "string", "artname", "string"),
    ],
    transformation_ctx="ChangeSchemaApplyMapping_node1668094793373",
)

# Script generated for node Amazon S3
AmazonS3_node1668094819102 = glueContext.write_dynamic_frame.from_options(
    frame=ChangeSchemaApplyMapping_node1668094793373,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": "s3://group1-data/curated/user-music/",
        "partitionKeys": [],
    },
    transformation_ctx="AmazonS3_node1668094819102",
)

job.commit()
