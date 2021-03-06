# mlflow-tests

Some simple tests to check API usage for the OSS documentation

[experiment_local_store.py](experiment_local_store.py) creates:
 * creates a model
 * logs the model
 * lists all registered models
 * searches and lists versions of the a registered model
 
 [log_reg_model.py](log_reg_model.py)
  * creates a model
  * logs the model
  * registers the model with a run_id, which create a new version of loggeed model
  * create a new version of the model with run_id
  * searches and lists versions of the a registered model
  
  [log_create_model.py](log_create_model.py)
  * creates a model
  * logs the model
  * attempts to register a model, which will fail
  * searches and lists versions of the a registered model
  
  [del_model.py](del_model.py)
  * takes a version of the model and deletes it
  * searches and lists versions of the a registered model 
  
  [del_all_reg_models.py](del_all_reg_models.py)
  * deletes all versions of a registered model
  
  [archive_model_versions.py](archive_model_versions.py)
  * takes a list model's versions and archives them
  * searches and lists versions of the a registered model; their stage should
  indicate as "Archived."
  
  [list_models.py](list_models.py)
   * List all registered models
   * search versions of a model
   
  [search_model_versions.py](search_model_versions.py)
   * search versions of a regsitered model
   
   [rename_reg_model.py](rename_reg_model.py)
    * rename a regisrtered model.
    * takes two command line arguments: old_model_name, new_model_name
