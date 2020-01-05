# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
ClassifierStacking
"""

__all__ = ["ClassifierStacking"]

import numbers

from ....utils.entrypoints import Component
from ....utils.utils import trace, try_set


class ClassifierStacking(Component):
    """
    **Description**
        Computes the output by training a model on a training set where each instance is a vector containing the outputs of the different models on a training instance, and the instance's label

    :param validation_dataset_proportion: The proportion of instances to be
        selected to test the individual base learner. If it is 0, it uses
        training set.

    :param params: Additional arguments sent to compute engine.

    """

    @trace
    def __init__(
            self,
            validation_dataset_proportion=0.3,
            **params):

        self.validation_dataset_proportion = validation_dataset_proportion
        self.kind = 'EnsembleMulticlassOutputCombiner'
        self.name = 'MultiStacking'
        self.settings = {}

        if validation_dataset_proportion is not None:
            self.settings['ValidationDatasetProportion'] = try_set(
                obj=validation_dataset_proportion,
                none_acceptable=True,
                is_of_type=numbers.Real)

        super(
            ClassifierStacking,
            self).__init__(
            name=self.name,
            settings=self.settings,
            kind=self.kind)