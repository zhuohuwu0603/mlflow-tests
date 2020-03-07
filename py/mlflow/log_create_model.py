import os
import shutil
from pprint import pprint as pp


from random import random, randint
import mlflow.sklearn
from mlflow import log_metric, log_param, log_artifacts
from sklearn.ensemble import RandomForestRegressor
from mlflow.tracking import MlflowClient
from mlflow.exceptions import MlflowException
import warnings

if __name__ == "__main__":

    warnings.filterwarnings("ignore")
    print(mlflow.__version__)

    # set the tracking server to be localhost with sqlite as tracking store
    local_registry = "sqlite:///mlruns.db"
    print(f"Running local model registry={local_registry}")
    model_name = "WeatherForecastModel"
    # model_name = "sk-learn-random-forest-reg-model"
    mlflow.set_tracking_uri(local_registry)
    with mlflow.start_run(run_name="LOCAL_REGISTRY") as run:
        params = {"n_estimators": 3, "random_state": 0}
        sk_learn_rfr = RandomForestRegressor(params)

        # Log parameters and metrics using the MLflow APIs
        mlflow.log_params(params)
        log_param("param_1", randint(0, 100))
        log_metric("metric_1", random())
        log_metric("metric_2", random() + 1)
        log_metric("metric_33", random() + 2)
        # Log and register the model at the same time
        mlflow.sklearn.log_model(
                    sk_model = sk_learn_rfr,
                    artifact_path = "sklearn-model",
                    registered_model_name="WeatherForecastModel")
        if not os.path.exists("outputs"):
            os.makedirs("outputs")
        with open("outputs/test.txt", "w") as f:
            f.write("Looks, like I logged to the local store!")

        log_artifacts("outputs")
        shutil.rmtree('outputs')
        run_id = run.info.run_uuid
    #
    # register with model registry
    # on a local host
    #
    client = MlflowClient()
    try:
        client.create_registered_model("WeatherForecastModel")
    except MlflowException as ex:
        print(ex)
    # Get a list of specific versions of the named models
    print(f"List of Model = {model_name} and Versions")
    print("=" * 80)
    [pp(dict(mv), indent=4) for mv in client.search_model_versions("name='WeatherForecastModel'")]
