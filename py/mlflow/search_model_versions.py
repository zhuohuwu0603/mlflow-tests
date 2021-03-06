import pprint

import mlflow.sklearn
from mlflow.tracking import MlflowClient
import warnings

if __name__ == "__main__":

    warnings.filterwarnings("ignore")
    print(mlflow.__version__)

    # set the tracking server to be localhost with sqlite as tracking store
    local_registry = "sqlite:///mlruns.db"
    print(f"Running local model registry={local_registry}")
    model_name="WeatherForecastModel"
    mlflow.set_tracking_uri(local_registry)

    # Search model versions
    print(f"List of all versions of {model_name} model")
    print("=" * 80)
    client = MlflowClient()
    [pprint.pprint(dict(mv), indent=4) for mv in client.search_model_versions("name='WeatherForecastModel'")]

    # get the maximum version
    model_versions = client.search_model_versions("name='WeatherForecastModel'")
    max_model_version = max([model_version.version for model_version in model_versions])
    print(f"max_version = {max_model_version}")
    print(f"max_version type is = {type(max_model_version)}")
