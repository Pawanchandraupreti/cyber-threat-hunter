import pulumi_aws as aws
from pulumi import Output

class ThreatIntelFeed:
    def __init__(self):
        self.bucket = aws.s3.Bucket("threat-data-lake", 
            acl="private",
            versioning=aws.s3.BucketVersioningArgs(enabled=True),
            tags={"Classification": "TLP:AMBER"}
        )


        aws.s3.BucketPolicy("lockdown",
            bucket=self.bucket.id,
            policy=Output.all(self.bucket.arn).apply(lambda arn: f"""{{
                "Version":"2012-10-17",
                "Statement":[{
                    "Effect":"Deny",
                    "Principal":"*",
                    "Action":"s3:*",
                    "Resource":"{arn[0]}",
                    "Condition":{{
                        "NotIpAddress":{{"aws:SourceIp":["10.0.0.0/8"]}}
                    }}
                }]
            }}""")
        )
        

        