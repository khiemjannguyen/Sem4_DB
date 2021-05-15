from influxdb_client import InfluxDBClient, Point, Bucket, BucketsApi, QueryApi, OrganizationsApi, WriteApi
from influxdb_client.client.write_api import SYNCHRONOUS
from config_getter import get_config

CONFIGS = get_config("db.json")

ORG = CONFIGS["ORG"]
BUCKET = CONFIGS["BUCKET"]
TOKEN = CONFIGS["TOKEN"]
URL = CONFIGS["URL"]

# Create APIs
client = InfluxDBClient(url=URL, token=TOKEN, org=ORG)
write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()
buckets_api = client.buckets_api()
organisation_api = client.organizations_api()


def get_org_id(org_name: str, org_api: OrganizationsApi = organisation_api):
    """
    Gets organization ID of InfluxDB organization name

    Args:
        org_name (str): name of organization of InfluxDB database
        org_api (OrganizationsApi, optional): API of organization of InfluxDB database. Defaults to organisation_api.

    Returns:
        org.id: organization of InfluxDB database
    """
    try:
        orgs = org_api.find_organizations()
        for org in orgs:
            if org.name == org_name:
                return org.id
        return None
    except Exception as e:
        print(e)
        print(f"Failed to get organization id of {org_name}")
        return None


ORG_ID = get_org_id(org_name=ORG)

def bucket_exists(bucket_name: str, buckets_api: BucketsApi = buckets_api):
    """
    Checks whether Bucket exists or not.

    Args:
        bucket_name (str): to be checked Bucket name
        buckets_api (BucketsApi, optional): API of Bucket. Defaults to buckets_api.

    Returns:
        (boolean)
    """
    try:
        bucket = buckets_api.find_bucket_by_name(bucket_name)
        if bucket:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        print(f"Failed to create Bucket {bucket_name}")
        return None

def create_bucket(bucket_name: str, org_id: str = ORG_ID, buckets_api: BucketsApi = buckets_api):
    """
    Creates new Bucket if Bucket with same name doesn't already exists

    Args:
        bucket_name (str): name of InfluxDB Bucket
        org_id (str, optional): organization ID of InfluxDB database. Defaults to ORG_ID.
        buckets_api (BucketsApi, optional): API of organization of InfluxDB database. Defaults to buckets_api.
    """
    try:
        if not bucket_exists(bucket_name):
            buckets_api.create_bucket(Bucket(name=bucket_name, retention_rules=[], org_id=org_id))
    except Exception as e:
        print(e)
        print(f"Failed to create Bucket {bucket_name}")
        return None

def write_points(points: list, bucket_name: str, write_api: WriteApi = write_api):
    """
    Writes point into given InfluxDB Bucket

    Args:
        points (list): point
        bucket_name (str): name of InfluxDB Bucket
        write_api (WriteApi, optional): API for writing into InfluxDB Bucket. Defaults to write_api.
    """
    try:
        write_api.write(bucket=bucket_name, record=points)
    except Exception as e:
        print(e)
        print(f"Failed to write Point into {bucket_name}")
        return None


def get_points(bucket_name: str, measurement: str, key: str, value: str, timedelta: str = "-10y", query_api: QueryApi = query_api):
    """
    Gets point out of InfluxDB Bucket with Query arguments

    Args:
        bucket_name (str): name of InfluxDB Bucket
        measurement (str): measurement
        key (str): key
        value (str): value
        timedelta (str, optional): timeperiod. Defaults to "-10y".
        query_api (QueryApi, optional): API to query points. Defaults to query_api.

    Returns:
        [type]: [description]
    """
    query = "from(bucket: \"" + bucket_name + "\") |> range(start: " + str(timedelta) + ", stop: now()) |> filter(fn: (r) => r[\"_measurement\"] == \"" + measurement + "\") |> filter(fn: (r) => r[\"" + key + "\"] == \"" + value + "\")"
    df = query_api.query_data_frame(query)
    print(df)
    df = df.loc[:, "_time":"_value"]
    df.columns = ["ds", "y"]
    df["ds"] = df["ds"].dt.tz_localize(None)
    return df

