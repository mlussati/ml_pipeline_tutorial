import argparse
import pathlib
import sys
import time

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import logging
    import omegaconf

from ml_pipeline import config, dataset_factory, model_factory, utils


def pipeline_task(task_func):
    task_func.is_task = True
    return task_func

class MLPipeline:
    def __init__(
            self: "MLPipeline", project_config_path: str, logger: "logging.Logger"
    ) -> None:
        self.logger = logger

        project_config_path = pathlib.Path(project_config_path)
        self.config = config.Config(
            project_config_path.parent.parent, project_config_path.stem
        )
        self.config.load()
        #TODO CONTINUE.....
