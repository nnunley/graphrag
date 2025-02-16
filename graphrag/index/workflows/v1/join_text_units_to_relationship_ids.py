# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""A module containing build_steps method definition."""

from graphrag.index.config import PipelineWorkflowConfig, PipelineWorkflowStep

workflow_name = "join_text_units_to_relationship_ids"


def build_steps(
    _config: PipelineWorkflowConfig,
) -> list[PipelineWorkflowStep]:
    """
    Create a join table from text unit ids to relationship ids.

    ## Dependencies
    * `workflow:create_final_relationships
    """
    return [
        {
            "verb": "join_text_units_to_relationship_ids",
            "args": {
                "select_columns": ["id", "text_unit_ids"],
                "unroll_column": "text_unit_ids",
                "aggregate_groupby": ["text_unit_ids"],
                "aggregate_aggregations": [
                    {
                        "column": "id",
                        "operation": "array_agg_distinct",
                        "to": "relationship_ids",
                    },
                    {
                        "column": "text_unit_ids",
                        "operation": "any",
                        "to": "id",
                    },
                ],
                "final_select_columns": ["id", "relationship_ids"],
            },
            "input": {"source": "workflow:create_final_relationships"},
        },
    ]
