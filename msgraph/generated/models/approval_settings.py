from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import approval_stage

@dataclass
class ApprovalSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # One of SingleStage, Serial, Parallel, NoApproval (default). NoApproval is used when isApprovalRequired is false.
    approval_mode: Optional[str] = None
    # If approval is required, the one or two elements of this collection define each of the stages of approval. An empty array if no approval is required.
    approval_stages: Optional[List[approval_stage.ApprovalStage]] = None
    # Indicates whether approval is required for requests in this policy.
    is_approval_required: Optional[bool] = None
    # Indicates whether approval is required for a user to extend their assignment.
    is_approval_required_for_extension: Optional[bool] = None
    # Indicates whether the requestor is required to supply a justification in their request.
    is_requestor_justification_required: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApprovalSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ApprovalSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ApprovalSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import approval_stage

        fields: Dict[str, Callable[[Any], None]] = {
            "approvalMode": lambda n : setattr(self, 'approval_mode', n.get_str_value()),
            "approvalStages": lambda n : setattr(self, 'approval_stages', n.get_collection_of_object_values(approval_stage.ApprovalStage)),
            "isApprovalRequired": lambda n : setattr(self, 'is_approval_required', n.get_bool_value()),
            "isApprovalRequiredForExtension": lambda n : setattr(self, 'is_approval_required_for_extension', n.get_bool_value()),
            "isRequestorJustificationRequired": lambda n : setattr(self, 'is_requestor_justification_required', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("approvalMode", self.approval_mode)
        writer.write_collection_of_object_values("approvalStages", self.approval_stages)
        writer.write_bool_value("isApprovalRequired", self.is_approval_required)
        writer.write_bool_value("isApprovalRequiredForExtension", self.is_approval_required_for_extension)
        writer.write_bool_value("isRequestorJustificationRequired", self.is_requestor_justification_required)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

