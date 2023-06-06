from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import workflow_base

from . import workflow_base

@dataclass
class WorkflowVersion(workflow_base.WorkflowBase):
    odata_type = "#microsoft.graph.identityGovernance.workflowVersion"
    # The version of the workflow.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    version_number: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkflowVersion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkflowVersion
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkflowVersion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import workflow_base

        fields: Dict[str, Callable[[Any], None]] = {
            "versionNumber": lambda n : setattr(self, 'version_number', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("versionNumber", self.version_number)
    

