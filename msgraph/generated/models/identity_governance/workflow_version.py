from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

workflow_base = lazy_import('msgraph.generated.models.identity_governance.workflow_base')

class WorkflowVersion(workflow_base.WorkflowBase):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new workflowVersion and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.identityGovernance.workflowVersion"
        # The version of the workflow.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        self._version_number: Optional[int] = None
    
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
        fields = {
            "version_number": lambda n : setattr(self, 'version_number', n.get_int_value()),
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
    
    @property
    def version_number(self,) -> Optional[int]:
        """
        Gets the versionNumber property value. The version of the workflow.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Returns: Optional[int]
        """
        return self._version_number
    
    @version_number.setter
    def version_number(self,value: Optional[int] = None) -> None:
        """
        Sets the versionNumber property value. The version of the workflow.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Args:
            value: Value to set for the versionNumber property.
        """
        self._version_number = value
    

