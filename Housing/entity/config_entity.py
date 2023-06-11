from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig"
                                 ,["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])


# data_ingested_config = DataIngestionConfig(dataset_download_url="dasdj",
#                     tgz_download_dir="absfdd",
#                     raw_data_dir="sadsa",
#                     ingested_train_dir="dsbsdb",
#                     ingested_test_dir="dfdjsdjk")

DataValidationConfig = namedtuple("DataValidationConfig",["schema_file_path"])

DataTransformationConfig = namedtuple("DataTransformationConfig",["add_bedroom_per_room",
                                      "transformed_train_dir",
                                      "transformed_test_dir",
                                      "preprocessed_object_file_path"])


ModelTrainerConfig = namedtuple("ModelTrainerConfig",["trainD_model_file_path","base_accuracy"])

ModelEvalutionConfig = namedtuple("ModelEvalutionConfig",["model_evalution_file_path","timr_stamp"])


ModelPusherConfig = namedtuple("ModelPusherConfig",["export_dir_path"])

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig",["artifact_dir"])
