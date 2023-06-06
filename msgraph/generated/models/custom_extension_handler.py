from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package_custom_extension_stage, custom_access_package_workflow_extension, entity

from . import entity

@dataclass
class CustomExtensionHandler(entity.Entity):
    # Indicates which custom workflow extension will be executed at this stage. Nullable. Supports $expand.
    custom_extension: Optional[custom_access_package_workflow_extension.CustomAccessPackageWorkflowExtension] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the stage of the access package assignment request workflow when the access package custom extension runs. The possible values are: assignmentRequestCreated, assignmentRequestApproved, assignmentRequestGranted, assignmentRequestRemoved, assignmentFourteenDaysBeforeExpiration, assignmentOneDayBeforeExpiration, unknownFutureValue.
    stage: Optional[access_package_custom_extension_stage.AccessPackageCustomExtensionStage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomExtensionHandler:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomExtensionHandler
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CustomExtensionHandler()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_package_custom_extension_stage, custom_access_package_workflow_extension, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "customExtension": lambda n : setattr(self, 'custom_extension', n.get_object_value(custom_access_package_workflow_extension.CustomAccessPackageWorkflowExtension)),
            "stage": lambda n : setattr(self, 'stage', n.get_enum_value(access_package_custom_extension_stage.AccessPackageCustomExtensionStage)),
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
        writer.write_object_value("customExtension", self.custom_extension)
        writer.write_enum_value("stage", self.stage)
    

